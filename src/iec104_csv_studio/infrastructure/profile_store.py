"""JSON persistence for editable IEC104 audit profiles."""

from __future__ import annotations

import json
import os
import re
import tempfile
from dataclasses import replace
from pathlib import Path
from typing import Any

from iec104_csv_studio.domain.audit_rules import (
    AuditRuleProfile,
    replace_profiles,
)
from iec104_csv_studio.infrastructure.application_paths import config_directory

PROFILE_NAME = re.compile(r"^[A-Z][A-Z0-9_]{1,63}$")
COMMAND_PHASES = ("SELECT", "EXECUTE", "CANCEL")
_BOOLEAN_FIELDS = (
    "master_monitor_allow_read",
    "master_monitor_allow_write",
    "master_command_allow_read",
    "master_command_allow_write",
    "slave_monitor_allow_read",
    "slave_monitor_allow_write",
)


def _decimal(value: str, field: str, *, minimum: int = 0) -> str:
    text = value.strip()
    if not (text.isascii() and text.isdecimal()) or int(text) < minimum:
        raise ValueError(f"{field} deve ser um inteiro >= {minimum}; recebido {value!r}.")
    return str(int(text))


def _boolean(value: str, field: str) -> str:
    text = value.strip().casefold()
    if text not in {"true", "false"}:
        raise ValueError(f"{field} deve ser True ou False; recebido {value!r}.")
    return "True" if text == "true" else "False"


def _phase(value: str, field: str) -> str:
    text = value.strip().upper()
    if text not in COMMAND_PHASES:
        raise ValueError(f"{field} deve ser um de {', '.join(COMMAND_PHASES)}; recebido {value!r}.")
    return text


def validate_profile(profile: AuditRuleProfile) -> AuditRuleProfile:
    """Reject values that would crash the auditor or produce invalid E3 objects."""
    flags = {field: _boolean(getattr(profile, field), field) for field in _BOOLEAN_FIELDS}
    block_size = _decimal(profile.block_size, "block_size", minimum=1)
    if len(profile.element_order) != int(block_size):
        raise ValueError(
            f"element_order possui {len(profile.element_order)} itens, mas block_size é "
            f"{block_size}."
        )
    if len({item.casefold() for item in profile.element_order}) != len(profile.element_order):
        raise ValueError("element_order não pode repetir elementos.")
    mapping = tuple(
        (_decimal(asdu, "ASDU do mapa N2", minimum=1), _decimal(n2, f"N2 do ASDU {asdu}"))
        for asdu, n2 in profile.master_monitor_n2_by_asdu
    )
    return replace(
        profile,
        expected_advise_type=_decimal(profile.expected_advise_type, "advise_type"),
        block_b2=_decimal(profile.block_b2, "block_b2"),
        block_size=block_size,
        high_priority_asdus=tuple(
            _decimal(item, "high_priority_asdus", minimum=1) for item in profile.high_priority_asdus
        ),
        master_monitor_n2_by_asdu=mapping,
        master_command_phase=_phase(profile.master_command_phase, "master_command_phase"),
        master_setpoint_phase=_phase(profile.master_setpoint_phase, "master_setpoint_phase"),
        master_bitstring_phase=_phase(profile.master_bitstring_phase, "master_bitstring_phase"),
        master_monitor_allow_read=flags["master_monitor_allow_read"],
        master_monitor_allow_write=flags["master_monitor_allow_write"],
        master_command_allow_read=flags["master_command_allow_read"],
        master_command_allow_write=flags["master_command_allow_write"],
        slave_monitor_allow_read=flags["slave_monitor_allow_read"],
        slave_monitor_allow_write=flags["slave_monitor_allow_write"],
    )


def _items(value: object, default: tuple[str, ...]) -> tuple[str, ...]:
    if isinstance(value, str):
        values = [item.strip() for item in value.split(",")]
    elif isinstance(value, (list, tuple)):
        values = [str(item).strip() for item in value]
    else:
        return default
    result = tuple(item for item in values if item)
    return result or default


def _mapping(value: object) -> tuple[tuple[str, str], ...]:
    if isinstance(value, dict):
        return tuple((str(key), str(item)) for key, item in value.items())
    if isinstance(value, str):
        pairs: list[tuple[str, str]] = []
        for fragment in value.split(","):
            key, separator, item = fragment.partition(":")
            if separator and key.strip() and item.strip():
                pairs.append((key.strip(), item.strip()))
        if pairs:
            return tuple(pairs)
    return AuditRuleProfile(name="DEFAULT").master_monitor_n2_by_asdu


def profile_from_mapping(payload: dict[str, Any]) -> AuditRuleProfile:
    """Validate and translate a JSON/UI payload into an immutable domain profile."""
    name = str(payload.get("name") or payload.get("id") or "").strip().upper()
    if not PROFILE_NAME.fullmatch(name):
        raise ValueError("Nome do profile deve usar A-Z, 0-9 e sublinhado.")
    defaults = AuditRuleProfile(name=name)
    profile = AuditRuleProfile(
        name=name,
        expected_advise_type=str(
            payload.get("expected_advise_type", payload.get("advise_type", "0"))
        ),
        master_monitor_allow_read=str(
            payload.get("master_monitor_allow_read", defaults.master_monitor_allow_read)
        ),
        master_monitor_allow_write=str(
            payload.get("master_monitor_allow_write", defaults.master_monitor_allow_write)
        ),
        master_command_allow_read=str(
            payload.get("master_command_allow_read", defaults.master_command_allow_read)
        ),
        master_command_allow_write=str(
            payload.get("master_command_allow_write", defaults.master_command_allow_write)
        ),
        slave_monitor_allow_read=str(
            payload.get("slave_monitor_allow_read", defaults.slave_monitor_allow_read)
        ),
        slave_monitor_allow_write=str(
            payload.get("slave_monitor_allow_write", defaults.slave_monitor_allow_write)
        ),
        block_b2=str(payload.get("block_b2", defaults.block_b2)),
        block_size=str(payload.get("block_size", defaults.block_size)),
        element_order=_items(payload.get("element_order"), defaults.element_order),
        high_priority_asdus=_items(
            payload.get("high_priority_asdus"), defaults.high_priority_asdus
        ),
        master_monitor_n2_by_asdu=_mapping(payload.get("master_monitor_n2_by_asdu")),
        master_command_phase=str(
            payload.get("master_command_phase", defaults.master_command_phase)
        ).upper(),
        master_setpoint_phase=str(
            payload.get("master_setpoint_phase", defaults.master_setpoint_phase)
        ).upper(),
        master_bitstring_phase=str(
            payload.get("master_bitstring_phase", defaults.master_bitstring_phase)
        ).upper(),
    )
    return validate_profile(profile)


def profile_to_mapping(profile: AuditRuleProfile) -> dict[str, Any]:
    return {
        "id": profile.name,
        "version": 1,
        "description": f"Profile IEC104 editável {profile.name}.",
        "advise_type": profile.expected_advise_type,
        "master_monitor_allow_read": profile.master_monitor_allow_read,
        "master_monitor_allow_write": profile.master_monitor_allow_write,
        "master_command_allow_read": profile.master_command_allow_read,
        "master_command_allow_write": profile.master_command_allow_write,
        "slave_monitor_allow_read": profile.slave_monitor_allow_read,
        "slave_monitor_allow_write": profile.slave_monitor_allow_write,
        "block_b2": profile.block_b2,
        "block_size": profile.block_size,
        "element_order": list(profile.element_order),
        "high_priority_asdus": list(profile.high_priority_asdus),
        "master_monitor_n2_by_asdu": dict(profile.master_monitor_n2_by_asdu),
        "master_command_phase": profile.master_command_phase,
        "master_setpoint_phase": profile.master_setpoint_phase,
        "master_bitstring_phase": profile.master_bitstring_phase,
        "notes": [],
    }


class ProfileStore:
    """Load, save and remove profiles from the writable config directory."""

    def __init__(self, directory: Path | None = None) -> None:
        self.directory = directory or config_directory() / "profiles"
        self.directory.mkdir(parents=True, exist_ok=True)
        self._profiles: dict[str, AuditRuleProfile] = {}
        self._paths: dict[str, Path] = {}
        self.errors: list[str] = []

    def load(self) -> tuple[AuditRuleProfile, ...]:
        """Load valid profiles; invalid files are reported in ``errors``, not fatal."""
        profiles: list[AuditRuleProfile] = []
        paths: dict[str, Path] = {}
        errors: list[str] = []
        for path in sorted(self.directory.glob("*.json")):
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
                if not isinstance(payload, dict):
                    raise ValueError("o conteúdo deve ser um objeto JSON.")
                profile = profile_from_mapping(payload)
            except (OSError, ValueError, TypeError) as error:
                errors.append(f"{path.name}: {error}")
                continue
            if profile.name in paths:
                first = paths[profile.name].name
                errors.append(f"{path.name}: profile {profile.name} já definido em {first}.")
                continue
            profiles.append(profile)
            paths[profile.name] = path
        self.errors = errors
        if not profiles:
            profiles = [AuditRuleProfile(name="PROJECT_PROFILE")]
        self._profiles = {profile.name: profile for profile in profiles}
        self._paths = paths
        replace_profiles(profiles)
        return tuple(self._profiles.values())

    def names(self) -> tuple[str, ...]:
        return tuple(self._profiles)

    def get(self, name: str) -> AuditRuleProfile:
        return self._profiles[name]

    def save(self, payload: dict[str, Any]) -> AuditRuleProfile:
        profile = profile_from_mapping(payload)
        document = profile_to_mapping(profile)
        target = self._paths.get(profile.name, self.directory / f"{profile.name.casefold()}.json")
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{target.stem}-", suffix=".tmp", dir=self.directory
        )
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
                json.dump(document, stream, ensure_ascii=False, indent=2)
                stream.write("\n")
            os.replace(temporary_name, target)
        except Exception:
            Path(temporary_name).unlink(missing_ok=True)
            raise
        self.load()
        return self._profiles[profile.name]

    def remove(self, name: str) -> None:
        if name not in self._profiles:
            raise ValueError(f"Profile desconhecido: {name}")
        if len(self._profiles) == 1:
            raise ValueError("Não é possível remover o último profile.")
        target = self._paths.get(name, self.directory / f"{name.casefold()}.json")
        target.unlink(missing_ok=True)
        self.load()
