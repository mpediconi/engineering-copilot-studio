"""Loss-preserving low-level E3 CSV writer."""

import csv
import os
import tempfile
import time
from collections.abc import Callable
from pathlib import Path

from iec104_csv_studio.domain.e3_models import E3CSVDocument

_REPLACE_ATTEMPTS = 5


def _target_encoding(document: E3CSVDocument) -> str:
    encoding = document.source.encoding.casefold().replace("_", "-")
    if encoding in {"utf-8", "utf8", "utf-8-sig"}:
        return "utf-8-sig" if document.source.has_bom else "utf-8"
    if encoding.startswith("utf-16"):
        # Python's utf-16 codec writes the BOM, preserving the source layout.
        return "utf-16"
    return document.source.encoding


def replace_atomically(temporary_path: Path, destination: Path) -> None:
    """Replace ``destination`` retrying briefly while another process holds it.

    Windows refuses ``os.replace`` while the destination is open (e.g. in Excel).
    """
    for attempt in range(_REPLACE_ATTEMPTS):
        try:
            os.replace(temporary_path, destination)
            return
        except PermissionError as error:
            if attempt == _REPLACE_ATTEMPTS - 1:
                raise PermissionError(
                    f"{error} — não foi possível substituir {destination}. "
                    "Feche o arquivo em outros programas (ex.: Excel) e tente novamente."
                ) from error
            time.sleep(0.1 * (attempt + 1))


def write_e3_csv(
    document: E3CSVDocument,
    path: str | Path,
    columns: tuple[str, ...] | None = None,
    verify: Callable[[Path], None] | None = None,
) -> None:
    """Write all headers or an explicit ordered projection of document columns.

    ``verify`` receives the fully written temporary file and may raise to abort
    the replacement, leaving any existing destination untouched.
    """
    destination = Path(path)
    headers = list(columns) if columns is not None else document.headers
    encoding = _target_encoding(document)
    newline = document.source.newline or "\n"
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            newline="",
            encoding=encoding,
            prefix=f".{destination.name}.",
            suffix=".tmp",
            dir=destination.parent,
            delete=False,
        ) as stream:
            temporary_path = Path(stream.name)
            writer = csv.writer(stream, delimiter=document.source.delimiter, lineterminator=newline)
            row_number = 1
            try:
                writer.writerow(headers)
                for index, obj in enumerate(document.objects, start=2):
                    row_number = index
                    if columns is None:
                        writer.writerow([prop.value for prop in obj.properties])
                    else:
                        writer.writerow([obj.property_value(header) or "" for header in headers])
            except UnicodeEncodeError as error:
                character = error.object[error.start : error.end]
                raise ValueError(
                    f"O caractere {character!r} (linha {row_number}) não pode ser gravado "
                    f"com o encoding {encoding}."
                ) from error
            stream.flush()
            os.fsync(stream.fileno())
        if verify is not None:
            verify(temporary_path)
        replace_atomically(temporary_path, destination)
        temporary_path = None
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
