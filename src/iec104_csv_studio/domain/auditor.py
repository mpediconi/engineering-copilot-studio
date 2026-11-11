"""Deterministic IEC104 audit and Master/Slave cross-validation services."""

from collections import defaultdict
from collections.abc import Iterable

from .audit_models import (
    DiagnosticCategory,
    DiagnosticSeverity,
    IEC104AuditReport,
    IEC104CrossValidationReport,
    IEC104Diagnostic,
)
from .audit_rules import AuditRuleProfile, get_profile
from .classification import (
    address_key,
    asdu_semantics,
    build_canonical_document,
    numeric_value,
)
from .e3_models import E3CSVDocument, E3Object
from .enums import CommandPhase, DriverRole, IEC104Function
from .models import (
    IEC104Address,
    IEC104Block,
    IEC104CanonicalDocument,
    IEC104Command,
)

MAX_STATION = 65_535
MAX_IOA = 16_777_215
IEC104_OBJECT_TYPES = frozenset({"IOTag", "IOBlock", "IOBlockElement", "IOFolder"})
# Parser findings that make the parsed content unreliable for conversion.
BLOCKING_PARSER_CODES = frozenset({"INVALID_ROW", "OBJECT_TYPE_MISSING", "HEADER_DUPLICATE"})
_COMMAND_PHASES = frozenset({"SELECT", "EXECUTE", "CANCEL"})


def _sort_diagnostics(diagnostics: Iterable[IEC104Diagnostic]) -> tuple[IEC104Diagnostic, ...]:
    return tuple(
        sorted(
            diagnostics,
            key=lambda item: (
                item.severity.value,
                item.code,
                item.source_path,
                str(item.address) if item.address else "",
            ),
        )
    )


def _diagnostic(
    code: str,
    severity: DiagnosticSeverity,
    category: DiagnosticCategory,
    message: str,
    *,
    obj: E3Object | None = None,
    address: IEC104Address | None = None,
    profile: str = "",
    details: dict[str, object] | None = None,
    related_paths: tuple[str, ...] = (),
    expected: str | None = None,
    actual: str | None = None,
) -> IEC104Diagnostic:
    return IEC104Diagnostic(
        code=code,
        severity=severity,
        category=category,
        message=message,
        source_path=obj.path_name if obj else "",
        object_type=obj.object_type if obj else "",
        address=address,
        rule_profile=profile,
        details=details or {},
        suggested_action="Revisar a configuração e selecionar o perfil correto.",
        row_index=obj.original_row_index if obj else None,
        related_paths=related_paths,
        expected_value=expected,
        actual_value=actual,
    )


def _value(obj: E3Object, name: str) -> str:
    return obj.property_value(name) or ""


def _source_objects(document: E3CSVDocument) -> dict[str, list[E3Object]]:
    by_type: dict[str, list[E3Object]] = defaultdict(list)
    for obj in document.objects:
        by_type[obj.object_type].append(obj)
    return by_type


class IEC104Auditor:
    def audit(
        self,
        document: E3CSVDocument,
        profile: str | AuditRuleProfile = "PROJECT_PROFILE",
        role: DriverRole | None = None,
        canonical: IEC104CanonicalDocument | None = None,
    ) -> IEC104AuditReport:
        selected = get_profile(profile) if isinstance(profile, str) else profile
        if canonical is None or canonical.source_document is not document:
            canonical = build_canonical_document(document)
        diagnostics: list[IEC104Diagnostic] = []
        diagnostics.extend(self._audit_parser(document))
        diagnostics.extend(self._audit_objects(document))
        diagnostics.extend(self._audit_canonical(canonical))
        diagnostics.extend(self._audit_unclassified(document, canonical))
        diagnostics.extend(self._audit_properties(canonical, selected, role))
        diagnostics.extend(self._audit_blocks(document, canonical, selected))
        diagnostics.extend(self._audit_commands(canonical))
        ordered = _sort_diagnostics(diagnostics)
        statistics = {
            "points": len(canonical.points),
            "commands": len(canonical.commands),
            "blocks": len(canonical.blocks),
            "block_elements": sum(len(block.element_paths) for block in canonical.blocks),
        }
        return IEC104AuditReport(
            document_role=(role or DriverRole.UNKNOWN).value,
            profile=selected.name,
            diagnostics=ordered,
            statistics=statistics,
        )

    def _audit_parser(self, document: E3CSVDocument) -> list[IEC104Diagnostic]:
        """Escalate parser findings that make conversion output unreliable."""
        by_row = {obj.original_row_index: obj for obj in document.objects}
        diagnostics: list[IEC104Diagnostic] = []
        for item in document.diagnostics:
            if item.code not in BLOCKING_PARSER_CODES:
                continue
            diagnostics.append(
                _diagnostic(
                    f"CSV_{item.code}",
                    DiagnosticSeverity.BLOCKING,
                    DiagnosticCategory.STRUCTURE,
                    f"{item.message} Corrija o CSV antes de converter.",
                    obj=by_row.get(item.row) if item.row is not None else None,
                    actual=str(item.row) if item.row is not None else None,
                )
            )
        return diagnostics

    def _audit_unclassified(
        self, document: E3CSVDocument, canonical: IEC104CanonicalDocument
    ) -> list[IEC104Diagnostic]:
        """IOTags that declare an ASDU but could not be projected are never silent."""
        by_row = {obj.original_row_index: obj for obj in document.objects}
        diagnostics: list[IEC104Diagnostic] = []
        for reference in canonical.unclassified_objects:
            obj = by_row.get(reference.original_row_index)
            if obj is None or obj.object_type != "IOTag":
                continue
            raw_n3 = _value(obj, "N3")
            if raw_n3 in {"", "0"}:
                # Driver-internal tags (status, statistics) carry no IEC104 ASDU.
                continue
            function, _, _ = asdu_semantics(raw_n3)
            if function is IEC104Function.UNKNOWN:
                diagnostics.append(
                    _diagnostic(
                        "IEC104_UNKNOWN_ASDU",
                        DiagnosticSeverity.BLOCKING,
                        DiagnosticCategory.IEC104,
                        "N3 não corresponde a um ASDU suportado; o tag seria omitido.",
                        obj=obj,
                        actual=raw_n3,
                    )
                )
            else:
                diagnostics.append(
                    _diagnostic(
                        "IEC104_INVALID_IOA",
                        DiagnosticSeverity.BLOCKING,
                        DiagnosticCategory.IEC104,
                        "IOA (N4) ausente; o tag seria omitido.",
                        obj=obj,
                        actual=_value(obj, "N4"),
                    )
                )
        return diagnostics

    def _audit_objects(self, document: E3CSVDocument) -> list[IEC104Diagnostic]:
        diagnostics: list[IEC104Diagnostic] = []
        by_path: dict[str, list[E3Object]] = defaultdict(list)
        by_parent_name: dict[tuple[str | None, str], list[E3Object]] = defaultdict(list)
        for obj in document.objects:
            if obj.path_name:
                by_path[obj.path_name].append(obj)
            by_parent_name[(obj.parent_path, obj.name)].append(obj)
        for path, objects in by_path.items():
            if len(objects) > 1:
                diagnostics.append(
                    _diagnostic(
                        "OBJ_DUPLICATE_PATH",
                        _duplicate_severity(objects),
                        DiagnosticCategory.OBJECT,
                        f"PathName duplicado: {path}.",
                        obj=objects[0],
                        related_paths=tuple(item.path_name for item in objects),
                    )
                )
        for (parent, name), objects in by_parent_name.items():
            if name and len(objects) > 1:
                diagnostics.append(
                    _diagnostic(
                        "OBJ_DUPLICATE_NAME_PARENT",
                        _duplicate_severity(objects),
                        DiagnosticCategory.OBJECT,
                        f"ParentPath + Name duplicado: {parent}/{name}.",
                        obj=objects[0],
                        related_paths=tuple(item.path_name for item in objects),
                    )
                )
        return diagnostics

    def _audit_canonical(self, canonical: IEC104CanonicalDocument) -> list[IEC104Diagnostic]:
        diagnostics: list[IEC104Diagnostic] = []
        address_items: dict[tuple[str, str, str], list[tuple[str, str, str]]] = defaultdict(list)
        first_address: dict[tuple[str, str, str], IEC104Address] = {}
        all_items: list[tuple[IEC104Address, str, str, str]] = []
        for point in canonical.points:
            all_items.append((point.address, point.function.value, point.source_path, ""))
        for command in canonical.commands:
            all_items.append(
                (command.address, command.function.value, command.source_path, command.phase.value)
            )
        for block in canonical.blocks:
            path = block.source.path_name if block.source else ""
            all_items.append((block.address, block.function.value, path, ""))
        for address, function, path, phase in all_items:
            key = address_key(address)
            first_address.setdefault(key, address)
            address_items[key].append((function, path, phase))
        for key, items in address_items.items():
            address = first_address[key]
            phases = [item[2] for item in items]
            # Only distinct command phases (one SELECT, one EXECUTE, one CANCEL)
            # may share an address; any repetition is a real duplicate.
            distinct_phases = all(phase in _COMMAND_PHASES for phase in phases) and len(
                set(phases)
            ) == len(phases)
            if len(items) > 1 and not distinct_phases:
                diagnostics.append(
                    _diagnostic(
                        "ADDR_DUPLICATE",
                        DiagnosticSeverity.BLOCKING,
                        DiagnosticCategory.ADDRESS,
                        f"Endereço IEC104 duplicado: {address}.",
                        address=address,
                        related_paths=tuple(item[1] for item in items),
                    )
                )
        station_ioa: dict[tuple[str, str], set[str]] = defaultdict(set)
        for address, _, _, _ in all_items:
            station, asdu, ioa = address_key(address)
            station_ioa[(station, ioa)].add(asdu)
        for (station, ioa), asdus in station_ioa.items():
            if len(asdus) > 1:
                diagnostics.append(
                    _diagnostic(
                        "ADDR_IOA_OVERLAP",
                        DiagnosticSeverity.WARNING,
                        DiagnosticCategory.ADDRESS,
                        f"Station {station} / IOA {ioa} é utilizado pelos ASDUs {sorted(asdus)}.",
                        address=IEC104Address(station, ",".join(sorted(asdus)), ioa),
                    )
                )
        for point in canonical.points:
            diagnostics.extend(self._validate_address(point.address, point.source))
        for command in canonical.commands:
            diagnostics.extend(self._validate_address(command.address, command.source))
        for block in canonical.blocks:
            diagnostics.extend(self._validate_address(block.address, block.source))
        return diagnostics

    def _validate_address(
        self, address: IEC104Address, source: object | None
    ) -> list[IEC104Diagnostic]:
        diagnostics: list[IEC104Diagnostic] = []
        station = numeric_value(address.station)
        if station is None or station > MAX_STATION:
            diagnostics.append(
                _diagnostic(
                    "IEC104_INVALID_STATION",
                    DiagnosticSeverity.BLOCKING,
                    DiagnosticCategory.IEC104,
                    f"Station ausente, não numérica ou fora da faixa 0..{MAX_STATION}: "
                    f"{address.station!r}.",
                    address=address,
                    actual=address.station,
                )
            )
        ioa = numeric_value(address.ioa)
        if not address.ioa:
            diagnostics.append(
                _diagnostic(
                    "IEC104_INVALID_IOA",
                    DiagnosticSeverity.BLOCKING,
                    DiagnosticCategory.IEC104,
                    "IOA ausente.",
                    address=address,
                )
            )
        elif ioa is None or not 1 <= ioa <= MAX_IOA:
            diagnostics.append(
                _diagnostic(
                    "IEC104_INVALID_IOA",
                    DiagnosticSeverity.BLOCKING,
                    DiagnosticCategory.IEC104,
                    f"IOA inválido ou fora da faixa 1..{MAX_IOA}: {address.ioa!r}.",
                    address=address,
                    actual=address.ioa,
                )
            )
        function, _, _ = asdu_semantics(address.asdu)
        if function is IEC104Function.UNKNOWN:
            diagnostics.append(
                _diagnostic(
                    "IEC104_UNKNOWN_ASDU",
                    DiagnosticSeverity.WARNING,
                    DiagnosticCategory.IEC104,
                    f"ASDU ainda não possui semântica implementada: {address.asdu}.",
                    address=address,
                )
            )
        return diagnostics

    def _audit_properties(
        self,
        canonical: IEC104CanonicalDocument,
        profile: AuditRuleProfile,
        role: DriverRole | None,
    ) -> list[IEC104Diagnostic]:
        diagnostics: list[IEC104Diagnostic] = []
        by_row = {obj.original_row_index: obj for obj in canonical.source_document.objects}
        for point in canonical.points:
            if point.source is None:
                continue
            source = by_row.get(point.source.original_row_index)
            if source is None:
                continue
            diagnostics.extend(self._advise(source, profile))
            if role is DriverRole.MASTER:
                diagnostics.extend(
                    self._allow(
                        source,
                        profile.master_monitor_allow_read,
                        "AllowRead",
                        "MASTER_INVALID_ALLOW_READ",
                        profile,
                    )
                )
                diagnostics.extend(
                    self._allow(
                        source,
                        profile.master_monitor_allow_write,
                        "AllowWrite",
                        "MASTER_INVALID_ALLOW_WRITE",
                        profile,
                    )
                )
            elif role is DriverRole.SLAVE:
                diagnostics.extend(
                    self._allow(
                        source,
                        profile.slave_monitor_allow_read,
                        "AllowRead",
                        "SLAVE_INVALID_ALLOW_READ",
                        profile,
                    )
                )
                diagnostics.extend(
                    self._allow(
                        source,
                        profile.slave_monitor_allow_write,
                        "AllowWrite",
                        "SLAVE_INVALID_ALLOW_WRITE",
                        profile,
                    )
                )
        for command in canonical.commands:
            if command.source is None:
                continue
            source = by_row.get(command.source.original_row_index)
            if source is None:
                continue
            diagnostics.extend(self._advise(source, profile))
            if role is DriverRole.MASTER:
                diagnostics.extend(
                    self._allow(
                        source,
                        profile.master_command_allow_read,
                        "AllowRead",
                        "MASTER_INVALID_ALLOW_READ",
                        profile,
                    )
                )
                diagnostics.extend(
                    self._allow(
                        source,
                        profile.master_command_allow_write,
                        "AllowWrite",
                        "MASTER_INVALID_ALLOW_WRITE",
                        profile,
                    )
                )
        return diagnostics

    def _advise(self, obj: E3Object, profile: AuditRuleProfile) -> list[IEC104Diagnostic]:
        actual = _value(obj, "AdviseType")
        if actual != profile.expected_advise_type:
            return [
                _diagnostic(
                    "PROPERTY_INVALID_ADVISE_TYPE",
                    DiagnosticSeverity.WARNING,
                    DiagnosticCategory.PROPERTY,
                    "AdviseType divergente do perfil.",
                    obj=obj,
                    profile=profile.name,
                    expected=profile.expected_advise_type,
                    actual=actual,
                )
            ]
        return []

    def _allow(
        self, obj: E3Object, expected: str, field: str, code: str, profile: AuditRuleProfile
    ) -> list[IEC104Diagnostic]:
        actual = _value(obj, field)
        if actual != expected:
            return [
                _diagnostic(
                    code,
                    DiagnosticSeverity.WARNING,
                    DiagnosticCategory.PROPERTY,
                    f"{field} divergente do perfil.",
                    obj=obj,
                    profile=profile.name,
                    expected=expected,
                    actual=actual,
                )
            ]
        return []

    def _audit_blocks(
        self, document: E3CSVDocument, canonical: IEC104CanonicalDocument, profile: AuditRuleProfile
    ) -> list[IEC104Diagnostic]:
        diagnostics: list[IEC104Diagnostic] = []
        by_path = {obj.path_name: obj for obj in document.objects}
        expected_size = numeric_value(profile.block_size) or len(profile.element_order)
        for block in canonical.blocks:
            source = by_path.get(block.source.path_name if block.source else "")
            if source is None:
                continue
            if block.raw_b2 != profile.block_b2:
                diagnostics.append(
                    _diagnostic(
                        "PROFILE_RULE_MISMATCH",
                        DiagnosticSeverity.WARNING,
                        DiagnosticCategory.PROFILE,
                        "B2 divergente do perfil selecionado.",
                        obj=source,
                        profile=profile.name,
                        expected=profile.block_b2,
                        actual=block.raw_b2,
                    )
                )
            if block.raw_size != profile.block_size:
                diagnostics.append(
                    _diagnostic(
                        "BLOCK_INVALID_SIZE",
                        DiagnosticSeverity.ERROR,
                        DiagnosticCategory.COMMAND,
                        "Size do IOBlock divergente do perfil.",
                        obj=source,
                        profile=profile.name,
                        expected=profile.block_size,
                        actual=block.raw_size,
                    )
                )
            if (
                numeric_value(block.raw_b1) is None
                or numeric_value(block.raw_b3) is None
                or numeric_value(block.raw_b4) is None
            ):
                diagnostics.append(
                    _diagnostic(
                        "BLOCK_INVALID_ADDRESS",
                        DiagnosticSeverity.BLOCKING,
                        DiagnosticCategory.IEC104,
                        "IOBlock possui endereço incompleto ou não numérico.",
                        obj=source,
                    )
                )
            if block.function is IEC104Function.UNKNOWN:
                diagnostics.append(
                    _diagnostic(
                        "IEC104_UNKNOWN_ASDU",
                        DiagnosticSeverity.BLOCKING,
                        DiagnosticCategory.IEC104,
                        "B3 não possui semântica conhecida; conversão bloqueada.",
                        obj=source,
                        profile=profile.name,
                        actual=block.raw_b3,
                    )
                )
            elements = []
            seen_paths: set[str] = set()
            for path in block.element_paths:
                if path in by_path and path not in seen_paths:
                    elements.append(by_path[path])
                    seen_paths.add(path)
            labels = [element.name.rsplit(".", 1)[-1] for element in elements]
            if len(elements) < expected_size:
                diagnostics.append(
                    _diagnostic(
                        "BLOCK_ELEMENT_MISSING",
                        DiagnosticSeverity.BLOCKING,
                        DiagnosticCategory.COMMAND,
                        "IOBlock possui menos elementos que o esperado.",
                        obj=source,
                        profile=profile.name,
                        actual=str(len(elements)),
                    )
                )
            if len(elements) > expected_size:
                diagnostics.append(
                    _diagnostic(
                        "BLOCK_ELEMENT_EXCESS",
                        DiagnosticSeverity.BLOCKING,
                        DiagnosticCategory.COMMAND,
                        "IOBlock possui mais elementos que o esperado.",
                        obj=source,
                        profile=profile.name,
                        expected=str(expected_size),
                        actual=str(len(elements)),
                    )
                )
            if len(labels) != len(set(labels)):
                diagnostics.append(
                    _diagnostic(
                        "BLOCK_ELEMENT_DUPLICATE",
                        DiagnosticSeverity.BLOCKING,
                        DiagnosticCategory.COMMAND,
                        "IOBlock possui elementos duplicados.",
                        obj=source,
                        profile=profile.name,
                    )
                )
            indices = [_value(element, "Index") for element in elements]
            invalid_indices = []
            for index in indices:
                numeric_index = numeric_value(index)
                if numeric_index is None or numeric_index >= expected_size:
                    invalid_indices.append(index)
            if invalid_indices:
                diagnostics.append(
                    _diagnostic(
                        "BLOCK_ELEMENT_INVALID_INDEX",
                        DiagnosticSeverity.BLOCKING,
                        DiagnosticCategory.COMMAND,
                        "IOBlock possui índice de elemento inválido.",
                        obj=source,
                        actual=", ".join(invalid_indices),
                    )
                )
            if len(indices) != len(set(indices)):
                diagnostics.append(
                    _diagnostic(
                        "BLOCK_ELEMENT_DUPLICATE_INDEX",
                        DiagnosticSeverity.BLOCKING,
                        DiagnosticCategory.COMMAND,
                        "IOBlock possui índices duplicados.",
                        obj=source,
                        profile=profile.name,
                    )
                )
            if len(labels) == len(profile.element_order) and tuple(labels) != profile.element_order:
                diagnostics.append(
                    _diagnostic(
                        "BLOCK_ELEMENT_ORDER_MISMATCH",
                        DiagnosticSeverity.WARNING,
                        DiagnosticCategory.PROFILE,
                        "Ordem dos IOBlockElements divergente do perfil.",
                        obj=source,
                        profile=profile.name,
                        expected="/".join(profile.element_order),
                        actual="/".join(labels),
                    )
                )
        return diagnostics

    def _audit_commands(self, canonical: IEC104CanonicalDocument) -> list[IEC104Diagnostic]:
        diagnostics: list[IEC104Diagnostic] = []
        for command in canonical.commands:
            if command.phase is CommandPhase.UNKNOWN:
                diagnostics.append(
                    _diagnostic(
                        "COMMAND_PHASE_UNKNOWN",
                        DiagnosticSeverity.WARNING,
                        DiagnosticCategory.COMMAND,
                        f"N2 não mapeado para fase de comando: {command.raw_n2}.",
                        address=command.address,
                    )
                )
        return diagnostics


def _duplicate_severity(objects: list[E3Object]) -> DiagnosticSeverity:
    """Duplicated IEC104 objects make conversion ambiguous, so they block it."""
    if any(obj.object_type in IEC104_OBJECT_TYPES for obj in objects):
        return DiagnosticSeverity.BLOCKING
    return DiagnosticSeverity.ERROR


def audit_target_structure(document: E3CSVDocument) -> tuple[IEC104Diagnostic, ...]:
    """Validate the hierarchy a conversion is about to write."""
    diagnostics: list[IEC104Diagnostic] = []
    by_name: dict[str, list[E3Object]] = defaultdict(list)
    for obj in document.objects:
        by_name[obj.name.casefold()].append(obj)
    for objects in by_name.values():
        if len(objects) > 1:
            diagnostics.append(
                _diagnostic(
                    "TARGET_DUPLICATE_NAME",
                    DiagnosticSeverity.BLOCKING,
                    DiagnosticCategory.STRUCTURE,
                    f"O destino teria objetos com o mesmo Name: {objects[0].name}.",
                    obj=objects[0],
                    related_paths=tuple(item.path_name for item in objects),
                )
            )
    for obj in document.objects:
        parent, separator, _ = obj.name.rpartition(".")
        if separator and parent.casefold() not in by_name:
            diagnostics.append(
                _diagnostic(
                    "TARGET_PARENT_MISSING",
                    DiagnosticSeverity.WARNING,
                    DiagnosticCategory.STRUCTURE,
                    f"O objeto pai {parent} não existe no destino.",
                    obj=obj,
                    expected=parent,
                )
            )
    return _sort_diagnostics(diagnostics)


class IEC104CrossValidator:
    def compare(
        self, master: IEC104CanonicalDocument, slave: IEC104CanonicalDocument
    ) -> IEC104CrossValidationReport:
        diagnostics: list[IEC104Diagnostic] = []
        master_monitor = {point.address: point for point in master.points}
        slave_monitor = {point.address: point for point in slave.points}
        master_items: tuple[IEC104Command | IEC104Block, ...] = (
            *master.commands,
            *master.blocks,
        )
        slave_items: tuple[IEC104Command | IEC104Block, ...] = (
            *slave.commands,
            *slave.blocks,
        )
        master_commands = {item.address: item for item in master_items}
        slave_blocks = {item.address: item for item in slave_items}
        for address in sorted(set(master_monitor) | set(slave_monitor), key=str):
            if address not in master_monitor:
                diagnostics.append(
                    _diagnostic(
                        "CROSS_ONLY_SLAVE",
                        DiagnosticSeverity.INFO,
                        DiagnosticCategory.CROSS_VALIDATION,
                        "Ponto presente somente no Slave.",
                        address=address,
                    )
                )
            elif address not in slave_monitor:
                diagnostics.append(
                    _diagnostic(
                        "CROSS_ONLY_MASTER",
                        DiagnosticSeverity.INFO,
                        DiagnosticCategory.CROSS_VALIDATION,
                        "Ponto presente somente no Master.",
                        address=address,
                    )
                )
        for address in sorted(set(master_commands) | set(slave_blocks), key=str):
            if address not in master_commands:
                diagnostics.append(
                    _diagnostic(
                        "CROSS_ONLY_SLAVE",
                        DiagnosticSeverity.INFO,
                        DiagnosticCategory.CROSS_VALIDATION,
                        "Comando presente somente no Slave.",
                        address=address,
                    )
                )
            elif address not in slave_blocks:
                diagnostics.append(
                    _diagnostic(
                        "CROSS_ONLY_MASTER",
                        DiagnosticSeverity.INFO,
                        DiagnosticCategory.CROSS_VALIDATION,
                        "Comando presente somente no Master.",
                        address=address,
                    )
                )
            else:
                command = master_commands[address]
                block = slave_blocks[address]
                if command.function is not block.function:
                    diagnostics.append(
                        _diagnostic(
                            "CROSS_FUNCTION_MISMATCH",
                            DiagnosticSeverity.WARNING,
                            DiagnosticCategory.CROSS_VALIDATION,
                            "Função Master/Slave divergente.",
                            address=address,
                        )
                    )
        master_by_station_ioa = {
            (item.address.station, item.address.ioa): item for item in master_monitor.values()
        }
        slave_by_station_ioa = {
            (item.address.station, item.address.ioa): item for item in slave_monitor.values()
        }
        for key in set(master_by_station_ioa) & set(slave_by_station_ioa):
            master_item = master_by_station_ioa[key]
            slave_item = slave_by_station_ioa[key]
            if master_item.address.asdu != slave_item.address.asdu:
                diagnostics.append(
                    _diagnostic(
                        "CROSS_ASDU_MISMATCH",
                        DiagnosticSeverity.WARNING,
                        DiagnosticCategory.CROSS_VALIDATION,
                        "ASDU divergente para Station + IOA.",
                        address=master_item.address,
                    )
                )
        ordered = _sort_diagnostics(diagnostics)
        statistics = {
            "monitoring_matches": sum(address in slave_monitor for address in master_monitor),
            "command_matches": sum(address in slave_blocks for address in master_commands),
            "only_master": sum(item.code == "CROSS_ONLY_MASTER" for item in ordered),
            "only_slave": sum(item.code == "CROSS_ONLY_SLAVE" for item in ordered),
            "asdu_mismatches": sum(item.code == "CROSS_ASDU_MISMATCH" for item in ordered),
            "function_mismatches": sum(item.code == "CROSS_FUNCTION_MISMATCH" for item in ordered),
        }
        statistics.update(
            {
                "command_matches_command": sum(
                    address in slave_blocks
                    and item.function is IEC104Function.COMMAND
                    and slave_blocks[address].function is IEC104Function.COMMAND
                    for address, item in master_commands.items()
                ),
                "command_matches_setpoint": sum(
                    address in slave_blocks
                    and item.function is IEC104Function.SETPOINT
                    and slave_blocks[address].function is IEC104Function.SETPOINT
                    for address, item in master_commands.items()
                ),
            }
        )
        return IEC104CrossValidationReport(ordered, statistics)
