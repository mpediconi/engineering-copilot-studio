"""Lossless, low-level representations of an Elipse E3 CSV document."""

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class SourceMetadata:
    """Physical properties needed to reproduce a CSV document."""

    encoding: str
    delimiter: str
    newline: str = "\n"
    has_bom: bool = False
    sha256: str = ""


@dataclass(frozen=True, slots=True)
class E3Property:
    """A property retaining its original column name and string value."""

    name: str
    value: str


@dataclass(slots=True)
class E3Object:
    """One exported E3 object, without IEC104 interpretation."""

    object_type: str
    path_name: str
    name: str
    parent_path: str | None
    properties: list[E3Property] = field(default_factory=list)
    original_row_index: int = 0
    raw_values: list[str] = field(default_factory=list)
    _lookup: dict[str, str] | None = field(default=None, init=False, repr=False, compare=False)
    _lookup_source: tuple[int, int] = field(default=(0, 0), init=False, repr=False, compare=False)

    def property_value(self, name: str) -> str | None:
        """Return the first property matching a column name (case-insensitive)."""
        key = (id(self.properties), len(self.properties))
        if self._lookup is None or self._lookup_source != key:
            lookup: dict[str, str] = {}
            for prop in self.properties:
                lookup.setdefault(prop.name.casefold(), prop.value)
            self._lookup = lookup
            self._lookup_source = key
        return self._lookup.get(name.casefold())


@dataclass(slots=True)
class E3CSVDocument:
    """Parsed CSV document and all source metadata required for round-trip."""

    headers: list[str]
    objects: list[E3Object]
    source: SourceMetadata
    diagnostics: list["E3Diagnostic"] = field(default_factory=list)


@dataclass(frozen=True, slots=True)
class E3Diagnostic:
    """Structured parser diagnostic; parsing continues whenever possible."""

    code: str
    severity: str
    message: str
    row: int | None = None
    column: str | None = None
    object_path: str | None = None

    @property
    def row_index(self) -> int | None:
        """Backward-compatible name used by early phase-1 callers."""
        return self.row
