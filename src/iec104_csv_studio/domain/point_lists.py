"""Intermediate point-list model, independent from XLSX."""

from collections import defaultdict
from dataclasses import dataclass
from enum import StrEnum
from typing import Any

from .audit_models import DiagnosticSeverity, IEC104AuditReport
from .e3_models import E3CSVDocument, E3Object
from .enums import DataFamily, IEC104Function, TimestampFormat
from .models import IEC104Block, IEC104CanonicalDocument, IEC104Command, IEC104Point


class PointListType(StrEnum):
    ACQUISITION = "ACQUISITION"
    DISTRIBUTION = "DISTRIBUTION"


class PointListSectionName(StrEnum):
    DISCRETOS = "Discretos"
    ANALOGICOS = "Analogicos"
    COMANDOS = "Comandos"
    SETPOINTS = "SetPoints"
    UNKNOWN = "Unknown"


@dataclass(frozen=True, slots=True)
class PointListRow:
    values: dict[str, Any]
    source_path: str
    object_type: str
    section: PointListSectionName
    status: str = "OK"
    validation_codes: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class PointListSection:
    name: PointListSectionName
    columns: tuple[str, ...]
    rows: tuple[PointListRow, ...]


@dataclass(frozen=True, slots=True)
class PointListDocument:
    list_type: PointListType
    source_filename: str
    profile: str
    metadata: dict[str, Any]
    sections: tuple[PointListSection, ...]
    hierarchy_rows: tuple[dict[str, Any], ...]
    equipment_rows: tuple[dict[str, Any], ...]
    driver_rows: tuple[dict[str, Any], ...]
    diagnostics: tuple[dict[str, Any], ...]

    @property
    def point_counts(self) -> dict[str, int]:
        return {section.name.value: len(section.rows) for section in self.sections}

    @property
    def total_listed(self) -> int:
        return sum(self.point_counts.values())


ACQUISITION_COLUMNS = (
    "Item",
    "Rev.",
    "Nível 1",
    "Nível 2",
    "Nível 3",
    "Nível 4",
    "Nível 5",
    "Nome",
    "Descrição",
    "Mult.",
    "Offset",
    "Ação",
    "SBO",
    "End. Aq.",
    "Tipo",
    "N1",
    "N2",
    "N3",
    "N4",
    "Driver dist.",
    "ASDU",
    "Endereço",
    "Station",
    "IOA",
    "Timestamp",
    "AllowRead",
    "AllowWrite",
    "AdviseType",
    "ObjectType",
    "SourcePath",
    "ValidationStatus",
    "ValidationCodes",
)
DISTRIBUTION_COLUMNS = ACQUISITION_COLUMNS + (
    "B1",
    "B2",
    "B3",
    "B4",
    "Size",
    "ElementSummary",
)


def _source_map(document: E3CSVDocument) -> dict[int, E3Object]:
    return {obj.original_row_index: obj for obj in document.objects}


def _value(obj: E3Object | None, field: str) -> str:
    return "" if obj is None else (obj.property_value(field) or "")


def _hierarchy(source: E3Object | None, driver_root: str) -> tuple[str, ...]:
    raw = _value(source, "Name") or _value(source, "PathName")
    if driver_root and raw.startswith(driver_root + "."):
        raw = raw[len(driver_root) + 1 :]
    parts = tuple(part for part in raw.split(".") if part)
    return parts[:5] if len(parts) <= 5 else (*parts[:4], ".".join(parts[4:]))


def _driver_root(document: E3CSVDocument) -> str:
    drivers = [obj for obj in document.objects if obj.object_type == "IODriver"]
    return _value(drivers[0], "Name") if drivers else ""


_SEVERITY_RANK = {
    DiagnosticSeverity.INFO: 0,
    DiagnosticSeverity.WARNING: 1,
    DiagnosticSeverity.ERROR: 2,
    DiagnosticSeverity.BLOCKING: 3,
}


class _DiagnosticIndex:
    """Index audit diagnostics by source path and address for O(1) row lookups."""

    def __init__(self, report: IEC104AuditReport) -> None:
        self.by_path: dict[str, list[Any]] = defaultdict(list)
        self.by_address: dict[object, list[Any]] = defaultdict(list)
        for diagnostic in report.diagnostics:
            if diagnostic.source_path:
                self.by_path[diagnostic.source_path].append(diagnostic)
            if diagnostic.address is not None:
                self.by_address[diagnostic.address].append(diagnostic)

    def severity_for(self, source_path: str, address: object) -> tuple[str, tuple[str, ...]]:
        matched = {
            id(item): item
            for item in (
                *(self.by_path.get(source_path, ()) if source_path else ()),
                *self.by_address.get(address, ()),
            )
        }.values()
        if not matched:
            return "OK", ()
        severity = max((item.severity for item in matched), key=lambda item: _SEVERITY_RANK[item])
        return severity.value, tuple(sorted({item.code for item in matched}))


def _friendly_type(function: IEC104Function, family: DataFamily, timestamp: TimestampFormat) -> str:
    family_names = {
        DataFamily.SINGLE_POINT: "Single Point",
        DataFamily.DOUBLE_POINT: "Double Point",
        DataFamily.NORMALIZED_VALUE: "Normalized Value",
        DataFamily.SCALED_VALUE: "Scaled Value",
        DataFamily.FLOAT: "Float",
        DataFamily.INTEGRATED_TOTAL: "Integrated Total",
        DataFamily.STEP_POSITION: "Step Position",
        DataFamily.SINGLE_COMMAND: "Single Command",
        DataFamily.DOUBLE_COMMAND: "Double Command",
        DataFamily.REGULATING_STEP_COMMAND: "Regulating Step Command",
        DataFamily.SETPOINT_NORMALIZED: "Normalized SetPoint",
        DataFamily.SETPOINT_SCALED: "Scaled SetPoint",
        DataFamily.SETPOINT_FLOAT: "Float SetPoint",
        DataFamily.BITSTRING: "Bitstring Command",
    }
    label = family_names.get(family, function.value)
    if family is DataFamily.BITSTRING and function is IEC104Function.MONITORING:
        label = "Bitstring"
    return f"{label} + {timestamp.value}" if timestamp is not TimestampFormat.NONE else label


class PointListBuilder:
    """Build point-list rows from canonical objects and audit diagnostics."""

    def build(
        self,
        document: E3CSVDocument,
        canonical: IEC104CanonicalDocument,
        audit: IEC104AuditReport,
        list_type: PointListType,
        source_filename: str = "",
    ) -> PointListDocument:
        source_by_row = _source_map(document)
        source_by_path: dict[str, E3Object] = {}
        for obj in document.objects:
            source_by_path.setdefault(obj.path_name, obj)
        diagnostics = _DiagnosticIndex(audit)
        driver_root = _driver_root(document)
        rows_by_section: dict[PointListSectionName, list[PointListRow]] = {
            section: [] for section in PointListSectionName
        }
        if list_type is PointListType.ACQUISITION:
            for point in canonical.points:
                rows_by_section[self._section_for_point(point)].append(
                    self._point_row(
                        point,
                        source_by_row.get(point.source.original_row_index if point.source else -1),
                        driver_root,
                        diagnostics,
                    )
                )
            for command in canonical.commands:
                rows_by_section[self._section_for_function(command.function)].append(
                    self._command_row(
                        command,
                        source_by_row.get(
                            command.source.original_row_index if command.source else -1
                        ),
                        driver_root,
                        diagnostics,
                    )
                )
        else:
            for point in canonical.points:
                rows_by_section[self._section_for_point(point)].append(
                    self._point_row(
                        point,
                        source_by_row.get(point.source.original_row_index if point.source else -1),
                        driver_root,
                        diagnostics,
                    )
                )
            for block in canonical.blocks:
                rows_by_section[self._section_for_function(block.function)].append(
                    self._block_row(block, source_by_path, driver_root, diagnostics)
                )
        ordered = (
            PointListSectionName.DISCRETOS,
            PointListSectionName.ANALOGICOS,
            PointListSectionName.COMANDOS,
            PointListSectionName.SETPOINTS,
            PointListSectionName.UNKNOWN,
        )
        sections = tuple(
            PointListSection(
                name=section,
                columns=(
                    DISTRIBUTION_COLUMNS
                    if list_type is PointListType.DISTRIBUTION
                    else ACQUISITION_COLUMNS
                ),
                rows=tuple(sorted(rows_by_section[section], key=self._sort_key)),
            )
            for section in ordered
            if rows_by_section[section]
        )
        hierarchy_rows = self._hierarchy_rows(canonical, source_by_row, driver_root)
        equipment_rows = self._equipment_rows(hierarchy_rows)
        driver_rows = self._driver_rows(document, canonical, audit, list_type, source_filename)
        diagnostic_rows = [self._diagnostic_row(item) for item in audit.diagnostics]
        known_paths = {item.get("Path", "") for item in diagnostic_rows}
        for item in canonical.unclassified_objects:
            if item.path_name not in known_paths:
                diagnostic_rows.append(
                    {
                        "Severity": DiagnosticSeverity.WARNING.value,
                        "Code": "POINT_NOT_CLASSIFIED",
                        "Category": "IEC104",
                        "Path": item.path_name,
                        "ObjectType": item.object_type,
                        "Station": "",
                        "ASDU": "",
                        "IOA": "",
                        "Actual": "",
                        "Expected": "",
                        "Message": (
                            "Objeto IEC104 não classificado e mantido fora das listas de pontos."
                        ),
                        "Suggested Action": "Revisar a semântica do objeto antes de exportar.",
                    }
                )
        return PointListDocument(
            list_type=list_type,
            source_filename=source_filename,
            profile=audit.profile,
            metadata={
                "encoding": document.source.encoding,
                "delimiter": document.source.delimiter,
                "object_count": len(document.objects),
                "point_count": canonical.iec104_object_count,
                "role": audit.document_role,
            },
            sections=sections,
            hierarchy_rows=tuple(hierarchy_rows),
            equipment_rows=tuple(equipment_rows),
            driver_rows=tuple(driver_rows),
            diagnostics=tuple(diagnostic_rows),
        )

    @staticmethod
    def _section_for_point(point: IEC104Point) -> PointListSectionName:
        if point.data_family in {
            DataFamily.SINGLE_POINT,
            DataFamily.DOUBLE_POINT,
            DataFamily.BITSTRING,
        }:
            return PointListSectionName.DISCRETOS
        if point.data_family in {
            DataFamily.NORMALIZED_VALUE,
            DataFamily.SCALED_VALUE,
            DataFamily.FLOAT,
            DataFamily.INTEGRATED_TOTAL,
            DataFamily.STEP_POSITION,
        }:
            return PointListSectionName.ANALOGICOS
        return PointListSectionName.UNKNOWN

    @staticmethod
    def _section_for_function(function: IEC104Function) -> PointListSectionName:
        if function is IEC104Function.COMMAND:
            return PointListSectionName.COMANDOS
        if function is IEC104Function.SETPOINT:
            return PointListSectionName.SETPOINTS
        return PointListSectionName.UNKNOWN

    @staticmethod
    def _sort_key(row: PointListRow) -> tuple[str, str, str, str]:
        return (
            ".".join(str(row.values.get(f"Nível {index}", "")) for index in range(1, 6)),
            str(row.values.get("Station", "")),
            str(row.values.get("ASDU", "")),
            str(row.values.get("IOA", "")),
        )

    def _base_values(self, source: E3Object | None, driver_root: str) -> dict[str, Any]:
        levels = _hierarchy(source, driver_root)
        values: dict[str, Any] = {
            f"Nível {index}": (levels[index - 1] if index <= len(levels) else "")
            for index in range(1, 6)
        }
        values.update(
            {
                "Nome": _value(source, "Name"),
                "Descrição": _value(source, "DocString"),
                "Driver aq.": _value(source, "DriverName"),
                "Driver dist.": _value(source, "DriverName"),
                "AllowRead": _value(source, "AllowRead"),
                "AllowWrite": _value(source, "AllowWrite"),
                "AdviseType": _value(source, "AdviseType"),
                "ObjectType": _value(source, "ObjectType"),
                "SourcePath": _value(source, "PathName"),
            }
        )
        return values

    def _point_row(
        self, point: IEC104Point, source: E3Object | None, root: str, audit: _DiagnosticIndex
    ) -> PointListRow:
        values = self._base_values(source, root)
        values.update(
            {
                "Item": values.get("Nome", ""),
                "End. Aq.": point.address.ioa,
                "Tipo": _friendly_type(point.function, point.data_family, point.timestamp_format),
                "N1": point.raw_n1,
                "N2": point.raw_n2,
                "N3": point.raw_n3,
                "N4": point.raw_n4,
                "ASDU": point.address.asdu,
                "Endereço": f"{point.address.station} / {point.address.asdu} / {point.address.ioa}",
                "Station": point.address.station,
                "IOA": point.address.ioa,
                "Timestamp": point.timestamp_format.value,
                "Mult.": _value(source, "EUHigh"),
                "Offset": _value(source, "EULow"),
            }
        )
        status, codes = audit.severity_for(
            point.source.path_name if point.source else "", point.address
        )
        return PointListRow(
            values,
            point.source.path_name if point.source else "",
            "IOTag",
            self._section_for_point(point),
            status,
            codes,
        )

    def _command_row(
        self, command: IEC104Command, source: E3Object | None, root: str, audit: _DiagnosticIndex
    ) -> PointListRow:
        values = self._base_values(source, root)
        values.update(
            {
                "Item": values.get("Nome", ""),
                "Ação": command.phase.value,
                "SBO": command.phase.value == "SELECT",
                "End. Aq.": command.address.ioa,
                "Tipo": _friendly_type(
                    command.function, command.data_family, command.timestamp_format
                ),
                "N1": command.raw_n1,
                "N2": command.raw_n2,
                "N3": command.raw_n3,
                "N4": command.raw_n4,
                "ASDU": command.address.asdu,
                "Endereço": (
                    f"{command.address.station} / {command.address.asdu} / {command.address.ioa}"
                ),
                "Station": command.address.station,
                "IOA": command.address.ioa,
                "Timestamp": command.timestamp_format.value,
            }
        )
        status, codes = audit.severity_for(
            command.source.path_name if command.source else "", command.address
        )
        return PointListRow(
            values,
            command.source.path_name if command.source else "",
            "IOTag",
            self._section_for_function(command.function),
            status,
            codes,
        )

    def _block_row(
        self,
        block: IEC104Block,
        source_by_path: dict[str, E3Object],
        root: str,
        audit: _DiagnosticIndex,
    ) -> PointListRow:
        source = source_by_path.get(block.source.path_name if block.source else "")
        values = self._base_values(source, root)
        elements = []
        for path in block.element_paths:
            element = source_by_path.get(path)
            if element is not None:
                elements.append(
                    f"{_value(element, 'Index')}:{_value(element, 'Name').rsplit('.', 1)[-1]} "
                    f"[{element.path_name}]"
                )
        values.update(
            {
                "Item": values.get("Nome", ""),
                "End. Aq.": block.address.ioa,
                "Tipo": _friendly_type(block.function, block.data_family, block.timestamp_format),
                "ASDU": block.address.asdu,
                "Endereço": f"{block.address.station} / {block.address.asdu} / {block.address.ioa}",
                "Station": block.address.station,
                "IOA": block.address.ioa,
                "Timestamp": block.timestamp_format.value,
                "B1": block.raw_b1,
                "B2": block.raw_b2,
                "B3": block.raw_b3,
                "B4": block.raw_b4,
                "Size": block.raw_size,
                "ElementSummary": " | ".join(elements),
            }
        )
        status, codes = audit.severity_for(
            block.source.path_name if block.source else "", block.address
        )
        return PointListRow(
            values,
            block.source.path_name if block.source else "",
            "IOBlock",
            self._section_for_function(block.function),
            status,
            codes,
        )

    def _hierarchy_rows(
        self, canonical: IEC104CanonicalDocument, source_by_row: dict[int, E3Object], root: str
    ) -> list[dict[str, Any]]:
        paths: set[tuple[str, ...]] = set()
        quantities: dict[tuple[str, ...], int] = {}
        for item in (*canonical.points, *canonical.commands):
            source = getattr(item, "source", None)
            if source and source.original_row_index in source_by_row:
                levels = _hierarchy(source_by_row[source.original_row_index], root)
                for index in range(1, len(levels) + 1):
                    prefix = tuple(levels[:index])
                    paths.add(prefix)
                    quantities[prefix] = quantities.get(prefix, 0) + 1
        for block in canonical.blocks:
            if block.source and block.source.original_row_index in source_by_row:
                levels = _hierarchy(source_by_row[block.source.original_row_index], root)
                for index in range(1, len(levels) + 1):
                    prefix = tuple(levels[:index])
                    paths.add(prefix)
                    quantities[prefix] = quantities.get(prefix, 0) + 1
        return [
            {
                "Nível": len(path),
                "Nome": path[-1],
                "Parent": ".".join(path[:-1]),
                "Path": ".".join(path),
                "Quantidade de Pontos": quantities[path],
            }
            for path in sorted(paths)
        ]

    @staticmethod
    def _equipment_rows(hierarchy_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
        return [
            {
                "Equipamento": row["Nome"],
                "Tipo": "UNKNOWN",
                "Hierarquia": row["Path"],
                "Descrição": "",
                "Quantidade de Pontos": row["Quantidade de Pontos"],
            }
            for row in hierarchy_rows
        ]

    @staticmethod
    def _driver_rows(
        document: E3CSVDocument,
        canonical: IEC104CanonicalDocument,
        audit: IEC104AuditReport,
        list_type: PointListType,
        source_filename: str,
    ) -> list[dict[str, Any]]:
        driver = next((obj for obj in document.objects if obj.object_type == "IODriver"), None)
        confidence = canonical.classification.confidence if canonical.classification else ""
        return [
            {
                "Arquivo": source_filename,
                "Tipo detectado": audit.document_role,
                "Confidence": confidence,
                "Driver Role": audit.document_role,
                "Encoding": document.source.encoding,
                "Delimiter": document.source.delimiter,
                "Quantidade de objetos": len(document.objects),
                "Quantidade de pontos IEC104": canonical.iec104_object_count,
                "Profile": audit.profile,
                "ListType": list_type.value,
                "DriverName": _value(driver, "Name"),
            }
        ]

    @staticmethod
    def _diagnostic_row(diagnostic: Any) -> dict[str, Any]:
        return {
            "Severity": diagnostic.severity.value,
            "Code": diagnostic.code,
            "Category": diagnostic.category.value,
            "Path": diagnostic.source_path,
            "ObjectType": diagnostic.object_type,
            "Station": diagnostic.address.station if diagnostic.address else "",
            "ASDU": diagnostic.address.asdu if diagnostic.address else "",
            "IOA": diagnostic.address.ioa if diagnostic.address else "",
            "Actual": diagnostic.actual_value or "",
            "Expected": diagnostic.expected_value or "",
            "Message": diagnostic.message,
            "Suggested Action": diagnostic.suggested_action,
        }
