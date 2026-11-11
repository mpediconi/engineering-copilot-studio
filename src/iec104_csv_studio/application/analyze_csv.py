"""Application-facing analysis services consumed by the desktop UI."""

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from iec104_csv_studio.domain.audit_models import IEC104AuditReport
from iec104_csv_studio.domain.auditor import IEC104Auditor, IEC104CrossValidator
from iec104_csv_studio.domain.classification import classify_and_build
from iec104_csv_studio.domain.enums import DriverRole, IEC104Function
from iec104_csv_studio.domain.models import IEC104CanonicalDocument
from iec104_csv_studio.infrastructure.e3_csv_reader import read_e3_csv


@dataclass(frozen=True, slots=True)
class AnalysisResult:
    path: Path
    document: Any
    canonical: IEC104CanonicalDocument
    audit: IEC104AuditReport

    @property
    def role(self) -> DriverRole:
        return (
            self.canonical.classification.role
            if self.canonical.classification
            else DriverRole.UNKNOWN
        )

    @property
    def confidence(self) -> float:
        return self.canonical.classification.confidence if self.canonical.classification else 0.0

    @property
    def monitoring_count(self) -> int:
        return len(self.canonical.points)

    @property
    def command_count(self) -> int:
        items = self.canonical.commands or self.canonical.blocks
        return sum(item.function is IEC104Function.COMMAND for item in items)

    @property
    def setpoint_count(self) -> int:
        items = self.canonical.commands or self.canonical.blocks
        return sum(item.function is IEC104Function.SETPOINT for item in items)

    @property
    def asdu_breakdown(self) -> tuple[dict[str, str | int], ...]:
        items: tuple[Any, ...] = (
            *self.canonical.points,
            *self.canonical.commands,
            *self.canonical.blocks,
        )
        counts = Counter(item.address.asdu for item in items)
        rows: list[dict[str, str | int]] = []
        first_by_asdu: dict[str, Any] = {}
        for item in items:
            first_by_asdu.setdefault(item.address.asdu, item)
        for asdu, count in sorted(
            counts.items(),
            key=lambda item: (
                int(item[0]) if item[0].isascii() and item[0].isdecimal() else 999,
                item[0],
            ),
        ):
            matching = first_by_asdu[asdu]
            rows.append(
                {
                    "ASDU": asdu,
                    "Function": matching.function.value,
                    "DataFamily": matching.data_family.value,
                    "Timestamp": matching.timestamp_format.value,
                    "Quantity": count,
                }
            )
        return tuple(rows)


def analyze_csv(
    path: str | Path,
    profile: str = "PROJECT_PROFILE",
    import_columns: tuple[str, ...] | None = None,
) -> AnalysisResult:
    source = Path(path)
    document = read_e3_csv(source, import_columns)
    canonical = classify_and_build(document)
    role = canonical.classification.role if canonical.classification else DriverRole.UNKNOWN
    audit = IEC104Auditor().audit(document, profile, role, canonical)
    return AnalysisResult(source, document, canonical, audit)


def compare_analyses(left: AnalysisResult, right: AnalysisResult) -> dict[str, int]:
    return IEC104CrossValidator().compare(left.canonical, right.canonical).statistics
