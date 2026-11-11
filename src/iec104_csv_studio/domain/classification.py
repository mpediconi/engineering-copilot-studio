"""Semantic IEC104 projection and Master/Slave classification."""

from collections import Counter
from dataclasses import dataclass

from .e3_models import E3CSVDocument, E3Object
from .enums import (
    CommandPhase,
    DataFamily,
    Direction,
    DriverRole,
    IEC104Function,
    Priority,
    TimestampFormat,
)
from .models import (
    IEC104Address,
    IEC104Block,
    IEC104CanonicalDocument,
    IEC104ClassificationEvidence,
    IEC104ClassificationResult,
    IEC104Command,
    IEC104Point,
    IEC104SourceReference,
)

_MON = IEC104Function.MONITORING
_CMD = IEC104Function.COMMAND
_SET = IEC104Function.SETPOINT

# Keys are IEC 60870-5-101/104 Type IDs as exported in N3/B3.
ASDU_SEMANTICS = {
    "1": (_MON, DataFamily.SINGLE_POINT, TimestampFormat.NONE),
    "2": (_MON, DataFamily.SINGLE_POINT, TimestampFormat.CP24),
    "3": (_MON, DataFamily.DOUBLE_POINT, TimestampFormat.NONE),
    "4": (_MON, DataFamily.DOUBLE_POINT, TimestampFormat.CP24),
    "5": (_MON, DataFamily.STEP_POSITION, TimestampFormat.NONE),
    "6": (_MON, DataFamily.STEP_POSITION, TimestampFormat.CP24),
    "7": (_MON, DataFamily.BITSTRING, TimestampFormat.NONE),
    "8": (_MON, DataFamily.BITSTRING, TimestampFormat.CP24),
    "9": (_MON, DataFamily.NORMALIZED_VALUE, TimestampFormat.NONE),
    "10": (_MON, DataFamily.NORMALIZED_VALUE, TimestampFormat.CP24),
    "11": (_MON, DataFamily.SCALED_VALUE, TimestampFormat.NONE),
    "12": (_MON, DataFamily.SCALED_VALUE, TimestampFormat.CP24),
    "13": (_MON, DataFamily.FLOAT, TimestampFormat.NONE),
    "14": (_MON, DataFamily.FLOAT, TimestampFormat.CP24),
    "15": (_MON, DataFamily.INTEGRATED_TOTAL, TimestampFormat.NONE),
    "16": (_MON, DataFamily.INTEGRATED_TOTAL, TimestampFormat.CP24),
    "21": (_MON, DataFamily.NORMALIZED_VALUE, TimestampFormat.NONE),
    "30": (_MON, DataFamily.SINGLE_POINT, TimestampFormat.CP56),
    "31": (_MON, DataFamily.DOUBLE_POINT, TimestampFormat.CP56),
    "32": (_MON, DataFamily.STEP_POSITION, TimestampFormat.CP56),
    "33": (_MON, DataFamily.BITSTRING, TimestampFormat.CP56),
    "34": (_MON, DataFamily.NORMALIZED_VALUE, TimestampFormat.CP56),
    "35": (_MON, DataFamily.SCALED_VALUE, TimestampFormat.CP56),
    "36": (_MON, DataFamily.FLOAT, TimestampFormat.CP56),
    "37": (_MON, DataFamily.INTEGRATED_TOTAL, TimestampFormat.CP56),
    "45": (_CMD, DataFamily.SINGLE_COMMAND, TimestampFormat.NONE),
    "46": (_CMD, DataFamily.DOUBLE_COMMAND, TimestampFormat.NONE),
    "47": (_CMD, DataFamily.REGULATING_STEP_COMMAND, TimestampFormat.NONE),
    "48": (_SET, DataFamily.SETPOINT_NORMALIZED, TimestampFormat.NONE),
    "49": (_SET, DataFamily.SETPOINT_SCALED, TimestampFormat.NONE),
    "50": (_SET, DataFamily.SETPOINT_FLOAT, TimestampFormat.NONE),
    "51": (_CMD, DataFamily.BITSTRING, TimestampFormat.NONE),
    "58": (_CMD, DataFamily.SINGLE_COMMAND, TimestampFormat.CP56),
    "59": (_CMD, DataFamily.DOUBLE_COMMAND, TimestampFormat.CP56),
    "60": (_CMD, DataFamily.REGULATING_STEP_COMMAND, TimestampFormat.CP56),
    "61": (_SET, DataFamily.SETPOINT_NORMALIZED, TimestampFormat.CP56),
    "62": (_SET, DataFamily.SETPOINT_SCALED, TimestampFormat.CP56),
    "63": (_SET, DataFamily.SETPOINT_FLOAT, TimestampFormat.CP56),
    "64": (_CMD, DataFamily.BITSTRING, TimestampFormat.CP56),
}
MONITORING_FAMILIES = {
    key: value for key, value in ASDU_SEMANTICS.items() if value[0] is IEC104Function.MONITORING
}
COMMAND_FAMILIES = {
    key: value for key, value in ASDU_SEMANTICS.items() if value[0] is not IEC104Function.MONITORING
}


@dataclass(frozen=True, slots=True)
class OrphanSummary:
    object_type: str
    quantity: int
    classification: str
    reason: str


def asdu_semantics(asdu: str) -> tuple[IEC104Function, DataFamily, TimestampFormat]:
    return ASDU_SEMANTICS.get(
        asdu,
        (IEC104Function.UNKNOWN, DataFamily.UNKNOWN, TimestampFormat.UNKNOWN),
    )


def numeric_value(value: str) -> int | None:
    """Parse a strictly decimal ASCII field (no sign, spaces or Unicode digits)."""
    if value and value.isascii() and value.isdecimal():
        return int(value)
    return None


def address_key(address: IEC104Address) -> tuple[str, str, str]:
    """Comparison key that treats ``0100`` and ``100`` as the same number."""

    def canonical(value: str) -> str:
        number = numeric_value(value)
        return str(number) if number is not None else value

    return canonical(address.station), canonical(address.asdu), canonical(address.ioa)


def source_reference(obj: E3Object) -> IEC104SourceReference:
    return IEC104SourceReference(obj.object_type, obj.path_name, obj.original_row_index)


def _value(obj: E3Object, name: str) -> str:
    return obj.property_value(name) or ""


def _direction(obj: E3Object) -> Direction:
    readable = _value(obj, "AllowRead").casefold() == "true"
    writable = _value(obj, "AllowWrite").casefold() == "true"
    if readable and writable:
        return Direction.BIDIRECTIONAL
    if readable:
        return Direction.RECEIVE
    if writable:
        return Direction.SEND
    return Direction.UNKNOWN


def _priority(raw_n2: str) -> Priority:
    if raw_n2 == "6":
        return Priority.HIGH
    if raw_n2 in {"4", "5"}:
        return Priority.LOW
    if raw_n2 == "0":
        return Priority.NOT_APPLICABLE
    return Priority.UNKNOWN


def _command_phase(raw_n2: str) -> CommandPhase:
    return {
        "10": CommandPhase.SELECT,
        "11": CommandPhase.EXECUTE,
        "12": CommandPhase.CANCEL,
    }.get(raw_n2, CommandPhase.UNKNOWN)


def _address(obj: E3Object, station_field: str, asdu_field: str, ioa_field: str) -> IEC104Address:
    return IEC104Address(
        _value(obj, station_field), _value(obj, asdu_field), _value(obj, ioa_field)
    )


def _point_from_tag(obj: E3Object) -> IEC104Point | IEC104Command | None:
    raw_n1, raw_n2, raw_n3, raw_n4 = (_value(obj, field) for field in ("N1", "N2", "N3", "N4"))
    semantic = asdu_semantics(raw_n3)
    if semantic[0] is IEC104Function.UNKNOWN or not raw_n4:
        return None
    function, data_family, timestamp_format = semantic
    address = IEC104Address(raw_n1, raw_n3, raw_n4)
    source = source_reference(obj)
    if function is IEC104Function.MONITORING:
        return IEC104Point(
            address=address,
            function=function,
            direction=_direction(obj),
            data_family=data_family,
            priority=_priority(raw_n2),
            timestamp_format=timestamp_format,
            source_path=obj.path_name,
            raw_n1=raw_n1,
            raw_n2=raw_n2,
            raw_n3=raw_n3,
            raw_n4=raw_n4,
            source=source,
        )
    return IEC104Command(
        address=address,
        function=function,
        phase=_command_phase(raw_n2),
        data_family=data_family,
        direction=_direction(obj),
        timestamp_format=timestamp_format,
        source_path=obj.path_name,
        raw_n1=raw_n1,
        raw_n2=raw_n2,
        raw_n3=raw_n3,
        raw_n4=raw_n4,
        source=source,
    )


def build_canonical_document(document: E3CSVDocument) -> IEC104CanonicalDocument:
    """Project IEC104-bearing E3 objects without changing source data."""
    canonical = IEC104CanonicalDocument(source_document=document)
    block_keys: list[tuple[str, ...]] = []
    elements_by_parent: dict[str, list[tuple[int, str]]] = {}
    for obj in document.objects:
        source = source_reference(obj)
        if obj.object_type == "IOTag":
            semantic = _point_from_tag(obj)
            if isinstance(semantic, IEC104Point):
                canonical.points.append(semantic)
            elif isinstance(semantic, IEC104Command):
                canonical.commands.append(semantic)
            else:
                canonical.unclassified_objects.append(source)
        elif obj.object_type == "IOBlock":
            raw_b3 = _value(obj, "B3")
            function, family, timestamp_format = asdu_semantics(raw_b3)
            block = IEC104Block(
                address=IEC104Address(_value(obj, "B1"), raw_b3, _value(obj, "B4")),
                function=function,
                data_family=family,
                timestamp_format=timestamp_format,
                raw_b1=_value(obj, "B1"),
                raw_b2=_value(obj, "B2"),
                raw_b3=raw_b3,
                raw_b4=_value(obj, "B4"),
                raw_size=_value(obj, "Size"),
                source=source,
            )
            canonical.blocks.append(block)
            block_keys.append(tuple(dict.fromkeys(key for key in (obj.name, obj.path_name) if key)))
        elif obj.object_type == "IOBlockElement":
            raw_index = _value(obj, "Index")
            try:
                index = int(raw_index or "-1")
            except ValueError:
                index = -1
            elements_by_parent.setdefault(obj.parent_path or "", []).append((index, obj.path_name))
        else:
            canonical.ignored_objects.append(source)
    for block, keys in zip(canonical.blocks, block_keys, strict=True):
        elements = [element for key in keys for element in elements_by_parent.get(key, [])]
        object.__setattr__(block, "element_paths", tuple(path for _, path in sorted(elements)))
    return canonical


def summarize_orphans(document: E3CSVDocument) -> tuple[OrphanSummary, ...]:
    """Classify parser orphan diagnostics without treating all as errors."""
    orphan_objects = {
        diagnostic.row
        for diagnostic in document.diagnostics
        if diagnostic.code == "ORPHAN_PARENT" and diagnostic.row is not None
    }
    by_type = Counter(
        obj.object_type for obj in document.objects if obj.original_row_index in orphan_objects
    )
    result: list[OrphanSummary] = []
    for object_type, quantity in sorted(by_type.items()):
        if object_type == "AgSimple":
            result.append(
                OrphanSummary(
                    object_type,
                    quantity,
                    "EXTERNAL_REFERENCE",
                    "*.Links.Value referencia coleção Links não exportada como objeto.",
                )
            )
        else:
            result.append(
                OrphanSummary(
                    object_type,
                    quantity,
                    "EXPECTED_UNRESOLVED_PARENT",
                    "ParentPath não está presente entre os objetos exportados.",
                )
            )
    return tuple(result)


class IEC104DriverClassifier:
    """Explainable, filename-independent Master/Slave classifier."""

    MASTER_THRESHOLD = 0.80
    WARNING_THRESHOLD = 0.60
    AMBIGUITY_MARGIN = 0.30

    def classify(self, document: E3CSVDocument) -> IEC104ClassificationResult:
        objects = document.objects
        tags = [obj for obj in objects if obj.object_type == "IOTag"]
        blocks = [obj for obj in objects if obj.object_type == "IOBlock"]
        elements = [obj for obj in objects if obj.object_type == "IOBlockElement"]
        commands = [tag for tag in tags if _value(tag, "N3") in COMMAND_FAMILIES]
        readable = [tag for tag in tags if _value(tag, "AllowRead").casefold() == "true"]
        writable = [tag for tag in tags if _value(tag, "AllowWrite").casefold() == "true"]
        b_parameters = sum(
            any(_value(block, field) for field in ("B1", "B2", "B3", "B4")) for block in blocks
        )
        master_score = 0.0
        slave_score = 0.0
        evidences: list[IEC104ClassificationEvidence] = []
        if commands:
            weight = 30.0
            master_score += weight
            evidences.append(
                IEC104ClassificationEvidence(
                    "MASTER_COMMAND_IOTAG",
                    f"{len(commands)} IOTags pertencem à família de comandos.",
                    weight,
                    len(commands),
                )
            )
        if readable:
            weight = 15.0
            master_score += weight
            evidences.append(
                IEC104ClassificationEvidence(
                    "MASTER_READ_IOTAGS",
                    f"{len(readable)} IOTags possuem AllowRead=True.",
                    weight,
                    len(readable),
                )
            )
        if not blocks and (commands or readable):
            weight = 10.0
            master_score += weight
            evidences.append(
                IEC104ClassificationEvidence(
                    "MASTER_NO_IOBLOCK",
                    "Nenhum IOBlock foi encontrado.",
                    weight,
                    0,
                )
            )
        if blocks:
            weight = 40.0
            slave_score += weight
            evidences.append(
                IEC104ClassificationEvidence(
                    "SLAVE_IOBLOCK_PRESENT",
                    f"{len(blocks)} objetos IOBlock encontrados.",
                    weight,
                    len(blocks),
                )
            )
        if elements:
            weight = 20.0
            slave_score += weight
            evidences.append(
                IEC104ClassificationEvidence(
                    "SLAVE_IOBLOCK_ELEMENT",
                    f"{len(elements)} objetos IOBlockElement encontrados.",
                    weight,
                    len(elements),
                )
            )
        if b_parameters:
            weight = 20.0
            slave_score += weight
            evidences.append(
                IEC104ClassificationEvidence(
                    "SLAVE_B_PARAMETERS",
                    f"{b_parameters} IOBlocks possuem parâmetros B.",
                    weight,
                    b_parameters,
                )
            )
        if writable:
            weight = 10.0
            slave_score += weight
            evidences.append(
                IEC104ClassificationEvidence(
                    "SLAVE_WRITE_IOTAGS",
                    f"{len(writable)} IOTags possuem AllowWrite=True.",
                    weight,
                    len(writable),
                )
            )
        total = master_score + slave_score
        confidence = max(master_score, slave_score) / total if total else 0.0
        if not total:
            role = DriverRole.UNKNOWN
            warnings: tuple[str, ...] = ("insufficient_evidence",)
        elif abs(master_score - slave_score) / total < self.AMBIGUITY_MARGIN:
            role = DriverRole.AMBIGUOUS
            warnings = ("conflicting_evidence",)
        elif confidence < self.WARNING_THRESHOLD:
            role = DriverRole.AMBIGUOUS
            warnings = ("low_confidence",)
        else:
            role = DriverRole.MASTER if master_score > slave_score else DriverRole.SLAVE
            warnings = () if confidence >= self.MASTER_THRESHOLD else ("classification_warning",)
        return IEC104ClassificationResult(
            role=role,
            confidence=confidence,
            master_score=master_score,
            slave_score=slave_score,
            evidences=tuple(evidences),
            warnings=warnings,
        )


def classify_and_build(document: E3CSVDocument) -> IEC104CanonicalDocument:
    canonical = build_canonical_document(document)
    canonical.classification = IEC104DriverClassifier().classify(document)
    return canonical
