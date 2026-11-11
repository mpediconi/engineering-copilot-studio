"""Robust low-level reader for Elipse E3 CSV exports."""

import csv
import hashlib
import io
from pathlib import Path
from typing import TextIO

from iec104_csv_studio.domain.e3_models import (
    E3CSVDocument,
    E3Diagnostic,
    E3Object,
    E3Property,
    SourceMetadata,
)

_DELIMITERS = ";,\t|"
_DEFAULT_FIELD_LIMIT = 10 * 1024 * 1024
_OBJECT_TYPE_NAMES = ("objecttype", "object type", "type", "tipo")
_PATH_NAMES = ("pathname", "path name", "path", "caminho", "nome completo")
_NAME_NAMES = ("name", "nome")
_UTF8_BOM = b"\xef\xbb\xbf"
_UTF16_BOMS = (b"\xff\xfe", b"\xfe\xff")


def _read_text(raw: bytes, path: Path) -> tuple[str, str, bool]:
    """Decode bytes, removing any BOM from the text and recording it separately."""
    if raw.startswith(_UTF8_BOM):
        try:
            return raw[len(_UTF8_BOM) :].decode("utf-8"), "utf-8", True
        except UnicodeDecodeError as error:
            raise UnicodeError(f"{path}: BOM UTF-8 presente, mas o conteúdo é inválido.") from error
    if raw.startswith(_UTF16_BOMS):
        try:
            # The utf-16 codec consumes the BOM and keeps the byte order.
            return raw.decode("utf-16"), "utf-16", True
        except UnicodeDecodeError as error:
            raise UnicodeError(
                f"{path}: BOM UTF-16 presente, mas o conteúdo é inválido."
            ) from error
    for encoding in ("utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(encoding), encoding, False
        except UnicodeDecodeError:
            continue
    raise UnicodeError(f"Não foi possível detectar o encoding de {path}")


def _detect_newline(text: str) -> str:
    if "\r\n" in text:
        return "\r\n"
    if "\r" in text and "\n" not in text:
        return "\r"
    return "\n"


def _first_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line
    return ""


def _detect_delimiter(text: str) -> str:
    """Prefer the delimiter that exposes a known E3 header; fall back to sniffing."""
    header_line = _first_line(text)
    known = {_normalise(name) for name in (*_OBJECT_TYPE_NAMES, *_PATH_NAMES, *_NAME_NAMES)}
    best: tuple[int, int, str] | None = None
    for delimiter in _DELIMITERS:
        fields = next(csv.reader([header_line], delimiter=delimiter), [])
        matches = sum(_normalise(field) in known for field in fields)
        if matches and (best is None or (matches, len(fields)) > best[:2]):
            best = (matches, len(fields), delimiter)
    if best is not None:
        return best[2]
    try:
        return csv.Sniffer().sniff(text[:8192], delimiters=_DELIMITERS).delimiter
    except csv.Error:
        if not header_line:
            return ";"
        return max(_DELIMITERS, key=lambda delimiter: header_line.count(delimiter))


def _normalise(value: str) -> str:
    return "".join(value.casefold().split())


def _find_header(headers: list[str], candidates: tuple[str, ...]) -> int | None:
    normalised: dict[str, int] = {}
    for index, header in enumerate(headers):
        normalised.setdefault(_normalise(header), index)
    for candidate in candidates:
        if _normalise(candidate) in normalised:
            return normalised[_normalise(candidate)]
    return None


def _parent_path(path_name: str) -> str | None:
    for separator in ("\\", "/", "|", "."):
        if separator in path_name:
            parent, _, _ = path_name.rpartition(separator)
            return parent or None
    return None


def _structural_path(name: str, path_name: str) -> str:
    """Use the exported full Name when available, otherwise PathName.

    E3 exports commonly store the full hierarchy in ``Name`` while
    ``PathName`` is the container or is empty for event objects. Both raw
    values remain unchanged on E3Object.
    """
    if any(separator in name for separator in ("\\", "/", "|", ".")):
        return name
    return path_name


def _field(values: list[str], index: int | None) -> str:
    return "" if index is None else values[index]


def _parse_text(
    text: str,
    encoding: str,
    has_bom: bool,
    sha256: str = "",
    delimiter: str | None = None,
) -> E3CSVDocument:
    newline = _detect_newline(text)
    if not text.strip():
        return E3CSVDocument(
            [],
            [],
            SourceMetadata(encoding, ";", newline, has_bom, sha256),
            [E3Diagnostic("CSV_EMPTY", "ERROR", "O arquivo CSV está vazio.")],
        )

    csv.field_size_limit(max(csv.field_size_limit(), _DEFAULT_FIELD_LIMIT))
    delimiter = delimiter or _detect_delimiter(text)
    source = SourceMetadata(encoding, delimiter, newline, has_bom, sha256)
    diagnostics: list[E3Diagnostic] = []
    # newline="" keeps quoted line breaks inside fields and ignores Unicode
    # separators (U+2028, U+0085...) that str.splitlines() would split on.
    reader = csv.reader(io.StringIO(text, newline=""), delimiter=delimiter)
    headers: list[str] | None = None
    for values in reader:
        if values:
            headers = values
            break
    if headers is None:
        return E3CSVDocument(
            [],
            [],
            source,
            [E3Diagnostic("HEADER_MISSING", "ERROR", "O CSV não possui cabeçalho.")],
        )

    headers = [header.strip() for header in headers]
    if not any(headers):
        diagnostics.append(E3Diagnostic("HEADER_MISSING", "ERROR", "O cabeçalho está vazio."))
    if len({header.casefold() for header in headers}) != len(headers):
        diagnostics.append(
            E3Diagnostic("HEADER_DUPLICATE", "WARNING", "Há nomes de coluna duplicados.")
        )

    object_type_index = _find_header(headers, _OBJECT_TYPE_NAMES)
    path_index = _find_header(headers, _PATH_NAMES)
    name_index = _find_header(headers, _NAME_NAMES)
    path_header = headers[path_index] if path_index is not None else None
    if object_type_index is None:
        diagnostics.append(
            E3Diagnostic("OBJECT_TYPE_MISSING", "ERROR", "A coluna ObjectType não foi encontrada.")
        )
    if path_index is None:
        diagnostics.append(
            E3Diagnostic("PATH_NAME_MISSING", "ERROR", "A coluna PathName não foi encontrada.")
        )
    if name_index is None:
        diagnostics.append(
            E3Diagnostic("NAME_MISSING", "ERROR", "A coluna Name não foi encontrada.")
        )

    objects: list[E3Object] = []
    for row_index, values in enumerate(reader, start=2):
        if not values:
            continue
        if len(values) != len(headers):
            diagnostics.append(
                E3Diagnostic(
                    "INVALID_ROW",
                    "ERROR",
                    f"Linha com {len(values)} campos; esperado {len(headers)}.",
                    row_index,
                )
            )
            values = (values + [""] * len(headers))[: len(headers)]
        object_type = _field(values, object_type_index)
        path_name = _field(values, path_index)
        name = _field(values, name_index) or (path_name.rsplit("\\", 1)[-1] if path_name else "")
        if not object_type:
            diagnostics.append(
                E3Diagnostic("OBJECT_TYPE_EMPTY", "ERROR", "ObjectType vazio.", row_index)
            )
        if not path_name and not name:
            diagnostics.append(
                E3Diagnostic("PATH_NAME_INVALID", "ERROR", "PathName e Name vazios.", row_index)
            )
        # Build properties by column position so duplicated headers keep their own values.
        properties = [E3Property(header, values[index]) for index, header in enumerate(headers)]
        structural_path = _structural_path(name, path_name)
        objects.append(
            E3Object(
                object_type=object_type,
                path_name=path_name,
                name=name,
                parent_path=_parent_path(structural_path) if structural_path else None,
                properties=properties,
                original_row_index=row_index,
                raw_values=list(values),
            )
        )

    paths = {value for obj in objects for value in (obj.path_name, obj.name) if value}
    for obj in objects:
        if obj.parent_path and obj.parent_path not in paths:
            diagnostics.append(
                E3Diagnostic(
                    "ORPHAN_PARENT",
                    "WARNING",
                    f"ParentPath não encontrado: {obj.parent_path}.",
                    obj.original_row_index,
                    path_header,
                )
            )

    return E3CSVDocument(
        headers=headers,
        objects=objects,
        source=source,
        diagnostics=diagnostics,
    )


def read_e3_csv(path: str | Path, columns: tuple[str, ...] | None = None) -> E3CSVDocument:
    """Read an E3 CSV without interpreting IEC104 semantics."""
    source_path = Path(path)
    if not source_path.exists():
        raise FileNotFoundError(source_path)

    raw = source_path.read_bytes()
    text, encoding, has_bom = _read_text(raw, source_path)
    document = _parse_text(text, encoding, has_bom, hashlib.sha256(raw).hexdigest())
    if columns is None or not document.headers:
        return document

    selected = {name.casefold() for name in columns}
    for candidates in (_OBJECT_TYPE_NAMES, _PATH_NAMES, _NAME_NAMES):
        index = _find_header(document.headers, candidates)
        if index is not None:
            selected.add(document.headers[index].casefold())
    projected_headers = [header for header in document.headers if header.casefold() in selected]
    for obj in document.objects:
        obj.properties = [prop for prop in obj.properties if prop.name.casefold() in selected]
        obj.raw_values = [prop.value for prop in obj.properties]
    document.headers = projected_headers
    return document


def read_e3_csv_text(text_stream: TextIO, *, delimiter: str | None = None) -> E3CSVDocument:
    """Read CSV text from a stream, useful for tests and callers without a file."""
    text = text_stream.read()
    has_bom = text.startswith("﻿")
    if has_bom:
        text = text[1:]
    return _parse_text(
        text,
        "utf-8",
        has_bom,
        hashlib.sha256(text.encode("utf-8")).hexdigest(),
        delimiter,
    )
