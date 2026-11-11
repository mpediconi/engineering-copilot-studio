"""Steps shared by both conversion directions: dry-run, gates and verified writing."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any

from iec104_csv_studio.domain.audit_models import (
    DiagnosticSeverity,
    IEC104AuditReport,
    IEC104Diagnostic,
)
from iec104_csv_studio.domain.auditor import (
    IEC104Auditor,
    IEC104CrossValidator,
    audit_target_structure,
)
from iec104_csv_studio.domain.classification import address_key, classify_and_build
from iec104_csv_studio.domain.e3_models import E3CSVDocument
from iec104_csv_studio.domain.enums import DriverRole
from iec104_csv_studio.domain.models import IEC104CanonicalDocument
from iec104_csv_studio.infrastructure.e3_csv_reader import read_e3_csv
from iec104_csv_studio.infrastructure.e3_csv_writer import write_e3_csv

if TYPE_CHECKING:
    from iec104_csv_studio.application.master_to_slave import ConversionPlan


@dataclass(slots=True)
class TargetEvaluation:
    canonical: IEC104CanonicalDocument
    audit: IEC104AuditReport
    cross_validation: dict[str, int]


def source_gate_codes(plan: ConversionPlan, source_audit: IEC104AuditReport) -> None:
    """Copy source diagnostics into the plan buckets without duplicates."""
    for diagnostic in source_audit.diagnostics:
        if diagnostic.severity is DiagnosticSeverity.WARNING:
            plan.warnings.append(diagnostic.code)
        elif diagnostic.severity is DiagnosticSeverity.ERROR:
            plan.errors.append(diagnostic.code)
        elif diagnostic.severity is DiagnosticSeverity.BLOCKING:
            plan.blocking_errors.append(diagnostic.code)


def evaluate_target(
    plan: ConversionPlan,
    source: IEC104CanonicalDocument,
    target_document: E3CSVDocument,
    profile: str,
    target_role: DriverRole,
) -> TargetEvaluation:
    """Audit the materialized target and enforce source→target invariants on the plan."""
    target = classify_and_build(target_document)
    base = IEC104Auditor().audit(target_document, profile, target_role, target)
    diagnostics: tuple[IEC104Diagnostic, ...] = (
        *base.diagnostics,
        *audit_target_structure(target_document),
    )
    audit = IEC104AuditReport(base.document_role, base.profile, diagnostics, base.statistics)
    cross = IEC104CrossValidator().compare(source, target).statistics

    source_monitoring = {address_key(item.address) for item in source.points}
    target_monitoring = {address_key(item.address) for item in target.points}
    source_commands = {address_key(item.address) for item in source.commands} | {
        address_key(item.address) for item in source.blocks
    }
    target_commands = {address_key(item.address) for item in target.commands} | {
        address_key(item.address) for item in target.blocks
    }
    missing_monitoring = source_monitoring - target_monitoring
    missing_commands = source_commands - target_commands
    if missing_monitoring:
        plan.blocking_errors.append(f"CROSS_MISSING_MONITORING:{len(missing_monitoring)}")
    if missing_commands:
        plan.blocking_errors.append(f"CROSS_MISSING_COMMANDS:{len(missing_commands)}")
    plan.target_audit = audit
    plan.cross_validation = cross
    return TargetEvaluation(target, audit, cross)


def read_source(
    source: str | Path, import_columns: tuple[str, ...] | None
) -> tuple[E3CSVDocument, IEC104CanonicalDocument, DriverRole]:
    document = read_e3_csv(source, import_columns)
    canonical = classify_and_build(document)
    role = canonical.classification.role if canonical.classification else DriverRole.UNKNOWN
    return document, canonical, role


def ensure_distinct_paths(source: str | Path, target: str | Path) -> None:
    source_path = Path(source).resolve()
    target_path = Path(target).resolve()
    if source_path == target_path or (
        target_path.exists() and source_path.exists() and source_path.samefile(target_path)
    ):
        raise ValueError("O arquivo de destino não pode ser o próprio CSV de origem.")


def ensure_expected_source(plan: ConversionPlan, expected_sha256: str | None) -> None:
    if expected_sha256 and plan.source_sha256 != expected_sha256:
        raise ValueError(
            "O CSV de origem foi alterado depois da geração do plano. Gere o plano novamente."
        )


def write_verified(
    target_document: E3CSVDocument,
    target: str | Path,
    export_columns: tuple[str, ...] | None,
) -> Path:
    """Write the target and re-read it before replacing the destination file."""

    def identity(name: str, path_name: str) -> str:
        # Mirrors the reader fallback used when Name is empty.
        return name or (path_name.rsplit("\\", 1)[-1] if path_name else "")

    expected = [
        (obj.object_type, identity(obj.name, obj.path_name)) for obj in target_document.objects
    ]

    def verify(written: Path) -> None:
        document = read_e3_csv(written)
        structural = [item for item in document.diagnostics if item.code == "INVALID_ROW"]
        actual = [(obj.object_type, obj.name) for obj in document.objects]
        if structural or actual != expected:
            raise ValueError(
                "Verificação pós-gravação falhou: o CSV gravado não corresponde ao destino "
                "auditado. O arquivo de destino não foi alterado."
            )

    path = Path(target)
    write_e3_csv(target_document, path, export_columns, verify=verify)
    return path


def blocking_total(plan: Any) -> int:
    return len(plan.blocking_errors) + (
        plan.target_audit.summary.blocking_count if plan.target_audit is not None else 0
    )
