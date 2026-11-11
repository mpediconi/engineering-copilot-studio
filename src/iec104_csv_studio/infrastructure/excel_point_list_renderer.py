"""XLSX renderer for the intermediate IEC104 point-list document."""

import os
import tempfile
from pathlib import Path
from typing import Any

from openpyxl import Workbook
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

from iec104_csv_studio.domain.point_lists import PointListDocument
from iec104_csv_studio.infrastructure.e3_csv_writer import replace_atomically


def _write(sheet: Any, row: int, column: int, value: Any) -> Any:
    """Write CSV-derived data as inert text: no formulas, no illegal XML characters."""
    if isinstance(value, str):
        value = ILLEGAL_CHARACTERS_RE.sub("", value)
    cell = sheet.cell(row, column, value)
    if isinstance(value, str) and cell.data_type == "f":
        # openpyxl treats any string starting with "=" as a formula (CWE-1236).
        cell.data_type = "s"
    return cell


class ExcelPointListRenderer:
    """Render point-list models without reinterpreting IEC104 semantics."""

    _TITLE_FILL = PatternFill("solid", fgColor="1F4E78")
    _HEADER_FILL = PatternFill("solid", fgColor="5B9BD5")
    _WARNING_FILL = PatternFill("solid", fgColor="FFF2CC")
    _ERROR_FILL = PatternFill("solid", fgColor="F4CCCC")

    def render(self, point_list: PointListDocument, output_path: str | Path) -> Path:
        target = Path(output_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        workbook = Workbook()
        workbook.remove(workbook.active)
        self._cover(workbook, point_list)
        self._table(
            workbook,
            "Hierarquias",
            ("Nível", "Nome", "Parent", "Path", "Quantidade de Pontos"),
            point_list.hierarchy_rows,
        )
        self._table(
            workbook,
            "Descrição equipamentos",
            ("Equipamento", "Tipo", "Hierarquia", "Descrição", "Quantidade de Pontos"),
            point_list.equipment_rows,
        )
        self._table(
            workbook,
            "Configuração do Driver",
            tuple(point_list.driver_rows[0].keys()) if point_list.driver_rows else (),
            point_list.driver_rows,
        )
        for section in point_list.sections:
            self._point_section(workbook, section.name.value, section.columns, section.rows)
        diagnostic_columns = (
            "Severity",
            "Code",
            "Category",
            "Path",
            "ObjectType",
            "Station",
            "ASDU",
            "IOA",
            "Actual",
            "Expected",
            "Message",
            "Suggested Action",
        )
        self._table(workbook, "Diagnosticos", diagnostic_columns, point_list.diagnostics)
        temporary_path: Path | None = None
        try:
            with tempfile.NamedTemporaryFile(
                prefix=f".{target.name}.",
                suffix=".tmp",
                dir=target.parent,
                delete=False,
            ) as handle:
                temporary_path = Path(handle.name)
            workbook.save(temporary_path)
            with temporary_path.open("rb+") as stream:
                os.fsync(stream.fileno())
            replace_atomically(temporary_path, target)
            temporary_path = None
        finally:
            if temporary_path is not None:
                temporary_path.unlink(missing_ok=True)
        return target

    def _cover(self, workbook: Workbook, point_list: PointListDocument) -> None:
        sheet = workbook.create_sheet("CAPA")
        sheet["A1"] = "IEC104 CSV Studio"
        sheet["A1"].font = Font(size=18, bold=True, color="FFFFFF")
        sheet["A1"].fill = self._TITLE_FILL
        sheet.merge_cells("A1:D1")
        rows = [
            ("Lista", point_list.list_type.value),
            ("Arquivo fonte", point_list.source_filename),
            ("Perfil", point_list.profile),
            ("Role detectado", point_list.metadata.get("role", "")),
            ("Encoding", point_list.metadata.get("encoding", "")),
            ("Delimiter", point_list.metadata.get("delimiter", "")),
            ("Objetos", point_list.metadata.get("object_count", "")),
            ("Pontos IEC104", point_list.metadata.get("point_count", "")),
        ]
        for index, (label, value) in enumerate(rows, start=3):
            _write(sheet, index, 1, label).font = Font(bold=True)
            _write(sheet, index, 2, value)
        sheet.column_dimensions["A"].width = 24
        sheet.column_dimensions["B"].width = 48

    def _point_section(
        self, workbook: Workbook, name: str, columns: tuple[str, ...], rows: tuple[Any, ...]
    ) -> None:
        sheet = workbook.create_sheet(name)
        sheet["A1"] = name
        sheet["A1"].font = Font(size=14, bold=True, color="FFFFFF")
        sheet["A1"].fill = self._TITLE_FILL
        sheet.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(columns))
        sheet["A2"] = (
            "Valores brutos preservados do E3; ValidationStatus e ValidationCodes vêm da auditoria."
        )
        sheet.merge_cells(start_row=2, start_column=1, end_row=2, end_column=len(columns))
        for column, header in enumerate(columns, start=1):
            cell = sheet.cell(4, column, header)
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = self._HEADER_FILL
            cell.alignment = Alignment(wrap_text=True, vertical="center")
        for row_number, row in enumerate(rows, start=5):
            values = dict(row.values)
            values["ValidationStatus"] = row.status
            values["ValidationCodes"] = ", ".join(row.validation_codes)
            for column, header in enumerate(columns, start=1):
                cell = _write(sheet, row_number, column, values.get(header, ""))
                cell.alignment = Alignment(
                    vertical="top",
                    wrap_text=header
                    in {"Descrição", "SourcePath", "ValidationCodes", "ElementSummary"},
                )
            status_cell = sheet.cell(row_number, columns.index("ValidationStatus") + 1)
            if row.status in {"ERROR", "BLOCKING"}:
                status_cell.fill = self._ERROR_FILL
            elif row.status == "WARNING":
                status_cell.fill = self._WARNING_FILL
        self._format_table(sheet, len(columns), 4, len(rows) + 4)

    def _table(
        self,
        workbook: Workbook,
        name: str,
        columns: tuple[str, ...],
        rows: list[dict[str, Any]] | tuple[dict[str, Any], ...],
    ) -> None:
        sheet = workbook.create_sheet(name)
        for column, header in enumerate(columns, start=1):
            cell = sheet.cell(1, column, header)
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = self._HEADER_FILL
        for row_number, row in enumerate(rows, start=2):
            for column, header in enumerate(columns, start=1):
                _write(sheet, row_number, column, row.get(header, ""))
        self._format_table(sheet, len(columns), 1, len(rows) + 1)

    @staticmethod
    def _format_table(sheet: Any, column_count: int, header_row: int, last_row: int) -> None:
        if column_count:
            sheet.freeze_panes = f"A{header_row + 1}"
            sheet.auto_filter.ref = f"A{header_row}:{get_column_letter(column_count)}{last_row}"
        for column in range(1, column_count + 1):
            letter = get_column_letter(column)
            maximum = max(
                (len(str(sheet.cell(row, column).value or "")) for row in range(1, last_row + 1)),
                default=10,
            )
            sheet.column_dimensions[letter].width = min(max(maximum + 2, 10), 42)
