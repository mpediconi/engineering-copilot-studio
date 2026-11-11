"""Canonical domain model skeleton.

These dataclasses deliberately contain no CSV, Qt, or Excel concerns. Concrete
parsing and semantic projection are introduced in later phases.
"""

from dataclasses import dataclass, field

from .e3_models import E3CSVDocument
from .enums import (
    CommandPhase,
    DataFamily,
    Direction,
    DriverRole,
    IEC104Function,
    Priority,
    TimestampFormat,
)


@dataclass(frozen=True, slots=True)
class IEC104Address:
    station: str
    asdu: str
    ioa: str


@dataclass(frozen=True, slots=True)
class IEC104Point:
    address: IEC104Address
    function: IEC104Function = IEC104Function.UNKNOWN
    direction: Direction = Direction.UNKNOWN
    data_family: DataFamily = DataFamily.UNKNOWN
    priority: Priority = Priority.UNKNOWN
    command_phase: CommandPhase = CommandPhase.NOT_APPLICABLE
    timestamp_format: TimestampFormat = TimestampFormat.UNKNOWN
    source_path: str = ""
    raw_n1: str = ""
    raw_n2: str = ""
    raw_n3: str = ""
    raw_n4: str = ""
    source: "IEC104SourceReference | None" = None


@dataclass(frozen=True, slots=True)
class IEC104Command:
    address: IEC104Address
    function: IEC104Function = IEC104Function.COMMAND
    phase: CommandPhase = CommandPhase.UNKNOWN
    source_path: str = ""
    data_family: DataFamily = DataFamily.UNKNOWN
    direction: Direction = Direction.UNKNOWN
    timestamp_format: TimestampFormat = TimestampFormat.UNKNOWN
    raw_n1: str = ""
    raw_n2: str = ""
    raw_n3: str = ""
    raw_n4: str = ""
    source: "IEC104SourceReference | None" = None


@dataclass(frozen=True, slots=True)
class IEC104SourceReference:
    object_type: str
    path_name: str
    original_row_index: int


@dataclass(frozen=True, slots=True)
class IEC104Block:
    address: IEC104Address
    function: IEC104Function
    data_family: DataFamily
    timestamp_format: TimestampFormat = TimestampFormat.UNKNOWN
    raw_b1: str = ""
    raw_b2: str = ""
    raw_b3: str = ""
    raw_b4: str = ""
    raw_size: str = ""
    source: IEC104SourceReference | None = None
    element_paths: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class IEC104ClassificationEvidence:
    code: str
    description: str
    weight: float
    matched_objects: int


@dataclass(frozen=True, slots=True)
class IEC104ClassificationResult:
    role: DriverRole
    confidence: float
    master_score: float
    slave_score: float
    evidences: tuple[IEC104ClassificationEvidence, ...] = ()
    warnings: tuple[str, ...] = ()


@dataclass(slots=True)
class IEC104CanonicalDocument:
    """IEC104 projection retaining its lossless E3 source document."""

    source_document: E3CSVDocument
    points: list[IEC104Point] = field(default_factory=list)
    commands: list[IEC104Command] = field(default_factory=list)
    blocks: list[IEC104Block] = field(default_factory=list)
    ignored_objects: list[IEC104SourceReference] = field(default_factory=list)
    unclassified_objects: list[IEC104SourceReference] = field(default_factory=list)
    classification: IEC104ClassificationResult | None = None

    @property
    def iec104_object_count(self) -> int:
        return len(self.points) + len(self.commands) + len(self.blocks)


@dataclass(frozen=True, slots=True)
class IEC104Hierarchy:
    path: str
    parent_path: str | None
    name: str


@dataclass(slots=True)
class IEC104Document:
    role: DriverRole = DriverRole.UNKNOWN
    points: list[IEC104Point] = field(default_factory=list)
    commands: list[IEC104Command] = field(default_factory=list)
    hierarchy: list[IEC104Hierarchy] = field(default_factory=list)
