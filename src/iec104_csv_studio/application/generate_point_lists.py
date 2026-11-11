"""Application services for generating Master and Slave point-list workbooks."""

from dataclasses import dataclass
from pathlib import Path

from iec104_csv_studio.application.conversion_pipeline import ensure_distinct_paths
from iec104_csv_studio.domain.auditor import IEC104Auditor
from iec104_csv_studio.domain.classification import classify_and_build
from iec104_csv_studio.domain.enums import DriverRole
from iec104_csv_studio.domain.point_lists import PointListBuilder, PointListType
from iec104_csv_studio.infrastructure.e3_csv_reader import read_e3_csv
from iec104_csv_studio.infrastructure.excel_point_list_renderer import ExcelPointListRenderer


@dataclass(frozen=True, slots=True)
class PointListGenerationResult:
    output_path: Path
    list_type: PointListType
    point_counts: dict[str, int]
    diagnostic_counts: dict[str, int]
    profile: str
    role: str = ""

    @property
    def role_mismatch(self) -> bool:
        """Acquisition lists come from a Master; distribution lists from a Slave."""
        expected = (
            DriverRole.MASTER if self.list_type is PointListType.ACQUISITION else DriverRole.SLAVE
        )
        return self.role != expected.value


def generate_point_list(
    input_path: str | Path,
    output_path: str | Path,
    list_type: PointListType,
    profile: str = "PROJECT_PROFILE",
    import_columns: tuple[str, ...] | None = None,
) -> PointListGenerationResult:
    source = Path(input_path)
    ensure_distinct_paths(source, output_path)
    document = read_e3_csv(source, import_columns)
    canonical = classify_and_build(document)
    role = canonical.classification.role if canonical.classification else None
    audit = IEC104Auditor().audit(document, profile, role, canonical)
    point_list = PointListBuilder().build(
        document, canonical, audit, list_type, source_filename=source.name
    )
    target = ExcelPointListRenderer().render(point_list, output_path)
    diagnostic_counts = {
        severity: sum(1 for item in point_list.diagnostics if item["Severity"] == severity)
        for severity in ("INFO", "WARNING", "ERROR", "BLOCKING")
    }
    return PointListGenerationResult(
        target,
        list_type,
        point_list.point_counts,
        diagnostic_counts,
        profile,
        (role or DriverRole.UNKNOWN).value,
    )


def generate_acquisition_point_list(
    input_path: str | Path,
    output_path: str | Path,
    profile: str = "PROJECT_PROFILE",
    import_columns: tuple[str, ...] | None = None,
) -> PointListGenerationResult:
    return generate_point_list(
        input_path, output_path, PointListType.ACQUISITION, profile, import_columns
    )


def generate_distribution_point_list(
    input_path: str | Path,
    output_path: str | Path,
    profile: str = "PROJECT_PROFILE",
    import_columns: tuple[str, ...] | None = None,
) -> PointListGenerationResult:
    return generate_point_list(
        input_path, output_path, PointListType.DISTRIBUTION, profile, import_columns
    )
