"""Resolve editable application data in source and packaged layouts."""

from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path


def _project_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _local_data_root() -> Path:
    base = os.environ.get("LOCALAPPDATA") or os.environ.get("APPDATA")
    return (Path(base) if base else Path.home() / ".local" / "share") / "IEC104 CSV Studio"


def _bundled_directory(name: str) -> Path | None:
    candidates = (
        Path(getattr(sys, "_MEIPASS", "")) / name if hasattr(sys, "_MEIPASS") else None,
        Path(sys.prefix) / "share" / "iec104-csv-studio" / name,
    )
    return next(
        (candidate for candidate in candidates if candidate is not None and candidate.is_dir()),
        None,
    )


def _editable_directory(name: str) -> Path:
    override = os.environ.get(f"IEC104_CSV_STUDIO_{name.upper()}_DIR")
    if override:
        target = Path(override).expanduser().resolve()
        target.mkdir(parents=True, exist_ok=True)
        return target

    # The source tree is only used when running unfrozen; a packaged app must not
    # write next to its executable (e.g. under Program Files).
    if not getattr(sys, "frozen", False):
        source = _project_root() / name
        if source.is_dir():
            return source

    target = _local_data_root() / name
    seed = _bundled_directory(name)
    if seed is not None and not any(target.glob("*")):
        # Seed on first use, and again if a previous copy was interrupted empty.
        shutil.copytree(seed, target, dirs_exist_ok=True)
    else:
        target.mkdir(parents=True, exist_ok=True)
    return target


def config_directory() -> Path:
    """Return the writable configuration directory."""
    return _editable_directory("config")


def application_settings() -> dict[str, object]:
    """Read optional application settings with safe built-in defaults."""
    defaults: dict[str, object] = {
        "version": 1,
        "default_profile": "PROJECT_PROFILE",
    }
    source = config_directory() / "app.json"
    if not source.is_file():
        return defaults
    try:
        payload = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return defaults
    return {**defaults, **payload} if isinstance(payload, dict) else defaults


def golden_files_directory() -> Path:
    """Return the writable Golden Files directory."""
    return _editable_directory("golden_files")
