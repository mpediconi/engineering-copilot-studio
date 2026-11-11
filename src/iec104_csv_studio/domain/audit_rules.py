"""Profile-backed rules for the IEC104 auditor."""

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AuditRuleProfile:
    name: str
    expected_advise_type: str = "0"
    master_monitor_allow_read: str = "True"
    master_monitor_allow_write: str = "False"
    master_command_allow_read: str = "False"
    master_command_allow_write: str = "False"
    slave_monitor_allow_read: str = "False"
    slave_monitor_allow_write: str = "True"
    block_b2: str = "6"
    block_size: str = "4"
    element_order: tuple[str, ...] = ("CMD", "SE", "COT", "QU")
    high_priority_asdus: tuple[str, ...] = ("2",)
    master_monitor_n2_by_asdu: tuple[tuple[str, str], ...] = (
        ("2", "6"),
        ("13", "5"),
        ("14", "5"),
        ("15", "6"),
    )
    master_command_phase: str = "EXECUTE"
    master_setpoint_phase: str = "SELECT"
    master_bitstring_phase: str = "EXECUTE"

    def master_n2_for_asdu(self, asdu: str) -> str | None:
        return dict(self.master_monitor_n2_by_asdu).get(asdu)


PROJECT_PROFILE = AuditRuleProfile(name="PROJECT_PROFILE")
ELIPSE_DOCUMENTED_PROFILE = AuditRuleProfile(
    name="ELIPSE_DOCUMENTED",
    block_b2="4",
    element_order=("CMD", "COT", "SE", "QU"),
)

_PROFILES: dict[str, AuditRuleProfile] = {
    PROJECT_PROFILE.name: PROJECT_PROFILE,
    ELIPSE_DOCUMENTED_PROFILE.name: ELIPSE_DOCUMENTED_PROFILE,
}


def replace_profiles(profiles: Iterable[AuditRuleProfile]) -> None:
    """Replace the runtime registry with validated immutable profiles."""
    values = tuple(profiles)
    if not values:
        raise ValueError("Ao menos um profile IEC104 deve estar registrado.")
    _PROFILES.clear()
    _PROFILES.update((profile.name, profile) for profile in values)


def profile_names() -> tuple[str, ...]:
    return tuple(_PROFILES)


def get_profile(name: str) -> AuditRuleProfile:
    try:
        return _PROFILES[name]
    except KeyError as error:
        raise ValueError(f"Perfil de regras desconhecido: {name}") from error
