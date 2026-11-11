"""Persistence for Golden File assignments and column defaults."""

from __future__ import annotations

import json
import os
import tempfile
import time
from pathlib import Path
from typing import Any

from iec104_csv_studio.infrastructure.application_paths import config_directory

GOLDEN_ROLES = ("MASTER", "SLAVE")
MANDATORY_COLUMNS = (
    "ObjectType",
    "Name",
    "PathName",
    "N1",
    "N2",
    "N3",
    "N4",
    "B1",
    "B2",
    "B3",
    "B4",
    "Size",
    "Index",
)
# Columns read by classification, audit, conversion and point lists. They are
# always loaded, even when the user selects a narrower import projection.
SEMANTIC_COLUMNS = (
    "AllowRead",
    "AllowWrite",
    "AdviseType",
    "PathContainer",
    "DocString",
    "DriverName",
    "EUHigh",
    "EULow",
)
# Structural columns that every exported E3 CSV must keep.
EXPORT_REQUIRED_COLUMNS = (*MANDATORY_COLUMNS, "PathContainer")


def _column_names(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    result: list[str] = []
    for item in value:
        name = str(item).strip()
        if name and name not in result:
            result.append(name)
    return result


class DataSetupStore:
    """Atomically persist user-managed data setup defaults."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = path or config_directory() / "data_setup.json"
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._data: dict[str, Any] = {}
        self.load()

    @staticmethod
    def _defaults() -> dict[str, Any]:
        return {
            "version": 1,
            "golden_assignments": {
                "MASTER": "MasterIEC104 modelo.CSV",
                "SLAVE": "SlaveIEC104 modelo.CSV",
            },
            "column_defaults": {
                "import_columns": [],
                "export_columns": [],
            },
        }

    def load(self) -> dict[str, Any]:
        defaults = self._defaults()
        if self.path.is_file():
            try:
                payload = json.loads(self.path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                payload = {}
        else:
            payload = {}
        assignments = payload.get("golden_assignments", {})
        columns = payload.get("column_defaults", {})
        self._data = {
            "version": 1,
            "golden_assignments": {
                role: str(assignments.get(role, defaults["golden_assignments"][role]))
                for role in GOLDEN_ROLES
            },
            "column_defaults": {
                "import_columns": _column_names(columns.get("import_columns", [])),
                "export_columns": _column_names(columns.get("export_columns", [])),
            },
        }
        return self._data

    @property
    def assignments(self) -> dict[str, str]:
        return dict(self._data["golden_assignments"])

    @property
    def import_columns(self) -> tuple[str, ...]:
        return tuple(self._data["column_defaults"]["import_columns"])

    @property
    def export_columns(self) -> tuple[str, ...]:
        return tuple(self._data["column_defaults"]["export_columns"])

    def assign_golden(self, role: str, filename: str) -> None:
        normalized = role.strip().upper()
        if normalized not in GOLDEN_ROLES:
            raise ValueError(f"Papel Golden inválido: {role}")
        if not filename or Path(filename).name != filename:
            raise ValueError("O Golden File deve ser identificado apenas pelo nome do arquivo.")
        self._data["golden_assignments"][normalized] = filename
        self._save()

    def forget_golden(self, filename: str) -> None:
        for role, assigned in self._data["golden_assignments"].items():
            if assigned == filename:
                self._data["golden_assignments"][role] = ""
        self._save()

    def save_columns(self, import_columns: object, export_columns: object) -> None:
        imported = _column_names(import_columns)
        exported = _column_names(export_columns)
        self._data["column_defaults"] = {
            "import_columns": imported,
            "export_columns": exported,
        }
        self._save()

    def effective_export_columns(self, available: tuple[str, ...]) -> tuple[str, ...] | None:
        """Return selected target columns while retaining structural IEC104 fields."""
        selected = {name.casefold() for name in self.export_columns}
        if not selected:
            return None
        required = {name.casefold() for name in EXPORT_REQUIRED_COLUMNS}
        return tuple(
            name for name in available if name.casefold() in selected or name.casefold() in required
        )

    def effective_import_columns(self) -> tuple[str, ...] | None:
        """Return the input projection plus fields required by IEC104 processing."""
        if not self.import_columns:
            return None
        values = list(self.import_columns)
        present = {name.casefold() for name in values}
        for name in (*MANDATORY_COLUMNS, *SEMANTIC_COLUMNS):
            if name.casefold() not in present:
                values.append(name)
                present.add(name.casefold())
        return tuple(values)

    def _save(self) -> None:
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{self.path.stem}-", suffix=".tmp", dir=self.path.parent
        )
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
                json.dump(self._data, stream, ensure_ascii=False, indent=2)
                stream.write("\n")
            for attempt in range(5):
                try:
                    os.replace(temporary_name, self.path)
                    break
                except PermissionError:
                    if attempt == 4:
                        raise
                    time.sleep(0.02 * (attempt + 1))
        except Exception:
            Path(temporary_name).unlink(missing_ok=True)
            raise
