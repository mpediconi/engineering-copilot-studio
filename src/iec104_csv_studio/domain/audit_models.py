"""Immutable diagnostic and audit report contracts."""

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any

from .models import IEC104Address


class DiagnosticSeverity(StrEnum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    BLOCKING = "BLOCKING"


class DiagnosticCategory(StrEnum):
    STRUCTURE = "STRUCTURE"
    OBJECT = "OBJECT"
    ADDRESS = "ADDRESS"
    IEC104 = "IEC104"
    COMMAND = "COMMAND"
    PROPERTY = "PROPERTY"
    PROFILE = "PROFILE"
    CROSS_VALIDATION = "CROSS_VALIDATION"


@dataclass(frozen=True, slots=True)
class IEC104Diagnostic:
    code: str
    severity: DiagnosticSeverity
    category: DiagnosticCategory
    message: str
    source_path: str = ""
    object_type: str = ""
    address: IEC104Address | None = None
    rule_profile: str = ""
    details: dict[str, Any] = field(default_factory=dict)
    suggested_action: str = ""
    row_index: int | None = None
    related_paths: tuple[str, ...] = ()
    expected_value: str | None = None
    actual_value: str | None = None


@dataclass(frozen=True, slots=True)
class AuditSummary:
    info_count: int = 0
    warning_count: int = 0
    error_count: int = 0
    blocking_count: int = 0


@dataclass(frozen=True, slots=True)
class IEC104AuditReport:
    document_role: str
    profile: str
    diagnostics: tuple[IEC104Diagnostic, ...]
    statistics: dict[str, int] = field(default_factory=dict)

    @property
    def summary(self) -> AuditSummary:
        counts = {severity: 0 for severity in DiagnosticSeverity}
        for diagnostic in self.diagnostics:
            counts[diagnostic.severity] += 1
        return AuditSummary(
            info_count=counts[DiagnosticSeverity.INFO],
            warning_count=counts[DiagnosticSeverity.WARNING],
            error_count=counts[DiagnosticSeverity.ERROR],
            blocking_count=counts[DiagnosticSeverity.BLOCKING],
        )

    @property
    def has_blocking_errors(self) -> bool:
        return self.summary.blocking_count > 0

    @property
    def has_errors(self) -> bool:
        return self.summary.error_count > 0 or self.has_blocking_errors

    def diagnostics_by_code(self, code: str) -> tuple[IEC104Diagnostic, ...]:
        return tuple(item for item in self.diagnostics if item.code == code)

    def diagnostics_by_severity(self, severity: DiagnosticSeverity) -> tuple[IEC104Diagnostic, ...]:
        return tuple(item for item in self.diagnostics if item.severity is severity)


@dataclass(frozen=True, slots=True)
class IEC104CrossValidationReport:
    diagnostics: tuple[IEC104Diagnostic, ...]
    statistics: dict[str, int]
