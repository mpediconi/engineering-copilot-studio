"""Master/Aquisição to Slave/Distribuição conversion workflow."""

from collections import defaultdict
from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path
from typing import Any

from iec104_csv_studio.application.conversion_pipeline import (
    ensure_distinct_paths,
    ensure_expected_source,
    evaluate_target,
    read_source,
    source_gate_codes,
    write_verified,
)
from iec104_csv_studio.domain.audit_models import IEC104AuditReport
from iec104_csv_studio.domain.audit_rules import AuditRuleProfile, get_profile
from iec104_csv_studio.domain.auditor import IEC104Auditor
from iec104_csv_studio.domain.e3_models import E3CSVDocument, E3Object, E3Property, SourceMetadata
from iec104_csv_studio.domain.enums import DriverRole, IEC104Function
from iec104_csv_studio.domain.models import (
    IEC104Address,
    IEC104CanonicalDocument,
    IEC104Command,
    IEC104Point,
)

SLAVE_HEADERS = (
    "ObjectType",
    "Name",
    "AdviseType",
    "AlarmVerify",
    "AllowRead",
    "AllowWrite",
    "AsyncBatchFlushTimeMs",
    "AsyncBatchSize",
    "B1",
    "B2",
    "B3",
    "B4",
    "DeviceHigh",
    "DeviceLow",
    "DisableIOServerPool",
    "DocString",
    "DriverLocation",
    "DriverName",
    "EnableDeadband",
    "EnableDriverEvent",
    "EnableReadGrouping",
    "EnableScaling",
    "EU",
    "EUHigh",
    "EULow",
    "ExposeToOpc",
    "Index",
    "IsAlarmArea",
    "N1",
    "N2",
    "N3",
    "N4",
    "P1",
    "P2",
    "P3",
    "P4",
    "ParamDevice",
    "ParamItem",
    "PathContainer",
    "PathName",
    "PathVolume",
    "PercentDeadband",
    "ReadRetries",
    "Scan",
    "ShareMaximum",
    "ShareServer",
    "Size",
    "UseBitFields",
    "WriteFeedbackMode",
    "WriteNullAsEmpty",
    "WriteRetries",
    "WriteSyncMode",
)


class ConversionActionKind(StrEnum):
    PRESERVE = "PRESERVE"
    CREATE = "CREATE"
    TRANSFORM = "TRANSFORM"
    REMOVE = "REMOVE"
    SKIP = "SKIP"


@dataclass(frozen=True, slots=True)
class ConversionAction:
    kind: ConversionActionKind
    source_path: str
    source_object_type: str
    target_path: str = ""
    target_object_type: str = ""
    reason: str = ""
    address: IEC104Address | None = None


@dataclass(slots=True)
class ConversionPlan:
    source_role: str
    target_role: str
    profile: str
    actions: list[ConversionAction] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    blocking_errors: list[str] = field(default_factory=list)
    source_audit: IEC104AuditReport | None = None
    monitoring_points: int = 0
    commands: int = 0
    setpoints: int = 0
    source_e3_objects_total: int = 0
    source_iec104_objects: int = 0
    source_command_tags: int = 0
    source_setpoint_tags: int = 0
    source_unknown_tags: int = 0
    source_iofolders: int = 0
    source_objects_in_scope: int = 0
    source_objects_out_of_scope: int = 0
    source_iotags: int = 0
    source_monitoring_points: int = 0
    source_unknown_iotags: int = 0
    source_ioblocks: int = 0
    source_ioblock_elements: int = 0
    source_commands: int = 0
    source_setpoints: int = 0
    source_sha256: str = ""
    target_audit: IEC104AuditReport | None = None
    cross_validation: dict[str, int] = field(default_factory=dict)

    @property
    def blocked(self) -> bool:
        return bool(self.blocking_errors) or (
            self.target_audit is not None and self.target_audit.has_blocking_errors
        )

    @property
    def blocking_count(self) -> int:
        return len(self.blocking_errors) + (
            self.target_audit.summary.blocking_count if self.target_audit is not None else 0
        )

    @property
    def objects_preserved(self) -> int:
        return sum(action.kind is ConversionActionKind.PRESERVE for action in self.actions)

    @property
    def objects_created(self) -> int:
        return sum(action.kind is ConversionActionKind.CREATE for action in self.actions)

    @property
    def objects_transformed(self) -> int:
        return sum(action.kind is ConversionActionKind.TRANSFORM for action in self.actions)

    @property
    def objects_skipped(self) -> int:
        return sum(action.kind is ConversionActionKind.SKIP for action in self.actions)


@dataclass(frozen=True, slots=True)
class ConversionResult:
    source_role: str
    target_role: str
    profile: str
    source_count: int
    target_count: int
    monitoring_converted: int
    commands_converted: int
    setpoints_converted: int
    io_blocks_created: int
    io_block_elements_created: int
    warning_count: int
    error_count: int
    blocking_count: int
    source_audit: IEC104AuditReport
    conversion_plan: ConversionPlan
    target_audit: IEC104AuditReport | None
    output_path: Path | None
    target_document: E3CSVDocument
    cross_validation: dict[str, int]
    iotags_created: int = 0
    ioblocks_removed: int = 0
    ioblock_elements_removed: int = 0
    lossy_diagnostics: tuple[str, ...] = ()


class MasterToSlavePlanner:
    """Create a complete, inspectable plan without writing a file."""

    def plan(
        self,
        document: E3CSVDocument,
        canonical: IEC104CanonicalDocument,
        source_audit: IEC104AuditReport,
        profile: AuditRuleProfile,
    ) -> ConversionPlan:
        plan = ConversionPlan(
            source_role=DriverRole.MASTER.value,
            target_role=DriverRole.SLAVE.value,
            profile=profile.name,
            source_audit=source_audit,
            monitoring_points=len(canonical.points),
            commands=sum(item.function is IEC104Function.COMMAND for item in canonical.commands),
            setpoints=sum(item.function is IEC104Function.SETPOINT for item in canonical.commands),
            source_e3_objects_total=len(document.objects),
            source_iec104_objects=canonical.iec104_object_count
            + len(canonical.unclassified_objects),
            source_command_tags=sum(
                item.function is IEC104Function.COMMAND for item in canonical.commands
            ),
            source_setpoint_tags=sum(
                item.function is IEC104Function.SETPOINT for item in canonical.commands
            ),
            source_unknown_tags=len(canonical.unclassified_objects),
            source_iofolders=sum(obj.object_type == "IOFolder" for obj in document.objects),
        )
        unknown_paths = {item.path_name for item in canonical.unclassified_objects}
        for obj in document.objects:
            if obj.object_type == "IODriver":
                plan.actions.append(
                    ConversionAction(
                        ConversionActionKind.SKIP,
                        obj.path_name,
                        obj.object_type,
                        reason=(
                            "Driver root excluded; destination imports under a preconfigured "
                            "Slave driver."
                        ),
                    )
                )
            elif obj.object_type == "IOFolder":
                plan.actions.append(
                    ConversionAction(
                        ConversionActionKind.PRESERVE,
                        obj.path_name,
                        obj.object_type,
                        target_object_type="IOFolder",
                        reason="Preserve hierarchy folder.",
                    )
                )
            elif obj.object_type in {
                "IEvents",
                "IEvent",
                "IAlarmUserFieldsCollection",
                "IAlarmUserField",
                "AgSimple",
            }:
                plan.actions.append(
                    ConversionAction(
                        ConversionActionKind.SKIP,
                        obj.path_name,
                        obj.object_type,
                        reason="Out of communication-scope conversion.",
                    )
                )
            elif obj.object_type == "IOTag":
                if obj.path_name in unknown_paths:
                    plan.actions.append(
                        ConversionAction(
                            ConversionActionKind.SKIP,
                            obj.path_name,
                            obj.object_type,
                            reason="UNCLASSIFIED_SOURCE_OBJECT",
                        )
                    )
                    plan.warnings.append("UNCLASSIFIED_SOURCE_OBJECT")
                else:
                    plan.actions.append(
                        ConversionAction(
                            ConversionActionKind.TRANSFORM,
                            obj.path_name,
                            obj.object_type,
                            target_object_type="IOTag",
                            reason=(
                                "Normalize Slave properties from canonical monitoring " "semantics."
                            ),
                        )
                    )
            else:
                plan.actions.append(
                    ConversionAction(
                        ConversionActionKind.SKIP,
                        obj.path_name,
                        obj.object_type,
                        reason="Unsupported source object type.",
                    )
                )
        groups: dict[IEC104Address, list[Any]] = defaultdict(list)
        for command in canonical.commands:
            groups[command.address].append(command)
        for address, commands in sorted(groups.items(), key=lambda item: str(item[0])):
            source = commands[0].source.path_name if commands[0].source else ""
            plan.actions.append(
                ConversionAction(
                    ConversionActionKind.CREATE,
                    source,
                    "IOTag",
                    target_object_type="IOBlock",
                    reason="Aggregate logical command phases by Station + ASDU + IOA.",
                    address=address,
                )
            )
            phase_names = {command.phase.value for command in commands}
            if phase_names != {"SELECT", "EXECUTE"}:
                plan.warnings.append(
                    f"COMMAND_PHASE_INCOMPLETE:{address.station}/{address.asdu}/{address.ioa}"
                )
        source_gate_codes(plan, source_audit)
        plan.source_objects_in_scope = plan.objects_preserved + plan.objects_transformed
        plan.source_objects_out_of_scope = (
            plan.source_e3_objects_total - plan.source_objects_in_scope
        )
        return plan


class MasterToSlaveTransformer:
    """Materialize a planned target E3 document from canonical semantics."""

    def transform(
        self,
        document: E3CSVDocument,
        canonical: IEC104CanonicalDocument,
        plan: ConversionPlan,
        profile: AuditRuleProfile,
    ) -> E3CSVDocument:
        source_root = self._source_root(document)
        target_root = self._target_root(source_root)
        source_by_path: dict[str, E3Object] = {}
        for obj in document.objects:
            source_by_path.setdefault(obj.path_name, obj)
        semantics_by_path: dict[str, IEC104Point | IEC104Command] = {}
        semantic_items: list[IEC104Point | IEC104Command] = [
            *canonical.points,
            *canonical.commands,
        ]
        for item in semantic_items:
            if item.source is not None:
                semantics_by_path.setdefault(item.source.path_name, item)
        objects: list[E3Object] = []
        for obj in document.objects:
            if obj.object_type == "IOFolder":
                objects.append(self._copy_object(obj, "IOFolder", target_root, source_root))
            elif obj.object_type == "IOTag":
                semantic = semantics_by_path.get(obj.path_name)
                if (
                    semantic is not None
                    and getattr(semantic, "function", None) is IEC104Function.MONITORING
                ):
                    objects.append(self._monitoring(obj, semantic, target_root, source_root))
        groups: dict[IEC104Address, list[Any]] = defaultdict(list)
        for command in canonical.commands:
            groups[command.address].append(command)
        for _address, commands in sorted(groups.items(), key=lambda item: str(item[0])):
            source = source_by_path.get(commands[0].source.path_name if commands[0].source else "")
            if source is None:
                continue
            block = self._block(source, commands[0], target_root, source_root, profile)
            objects.append(block)
            for index, label in enumerate(profile.element_order):
                objects.append(self._element(block, label, index, target_root))
        return E3CSVDocument(
            headers=list(SLAVE_HEADERS),
            objects=objects,
            source=SourceMetadata(
                document.source.encoding,
                document.source.delimiter,
                document.source.newline,
                document.source.has_bom,
            ),
            diagnostics=[],
        )

    @staticmethod
    def _source_root(document: E3CSVDocument) -> str:
        tag = next(
            (
                obj
                for obj in document.objects
                if obj.object_type == "IOTag" and obj.property_value("PathContainer")
            ),
            None,
        )
        return (tag.property_value("PathContainer") or "") if tag else ""

    @staticmethod
    def _target_root(source_root: str) -> str:
        parent = source_root.rsplit(".", 1)[0] if "." in source_root else source_root
        return f"{parent}.[IEC104-SLAVE]" if parent else "[IEC104-SLAVE]"

    def _path(self, name: str, target_root: str) -> str:
        return f"{target_root}.{name}" if name else target_root

    def _copy_object(
        self, source: E3Object, object_type: str, target_root: str, source_root: str
    ) -> E3Object:
        name = source.name.removeprefix(source_root + ".")
        path = self._path(name, target_root)
        return self._object(
            object_type, name, path, source, {"PathContainer": target_root, "PathName": path}
        )

    def _monitoring(
        self, source: E3Object, semantic: Any, target_root: str, source_root: str
    ) -> E3Object:
        name = source.name.removeprefix(source_root + ".")
        path = self._path(name, target_root)
        n2 = "6" if semantic.address.asdu == "2" else semantic.raw_n2
        overrides = {
            "PathContainer": target_root,
            "PathName": path,
            "AllowRead": "False",
            "AllowWrite": "True",
            "AdviseType": "0",
            "N1": semantic.address.station,
            "N2": n2,
            "N3": semantic.address.asdu,
            "N4": semantic.address.ioa,
        }
        return self._object("IOTag", name, path, source, overrides)

    def _block(
        self,
        source: E3Object,
        command: Any,
        target_root: str,
        source_root: str,
        profile: AuditRuleProfile,
    ) -> E3Object:
        name = source.name.removeprefix(source_root + ".")
        path = self._path(name, target_root)
        overrides = {
            "PathContainer": target_root,
            "PathName": path,
            "ObjectType": "IOBlock",
            "AllowRead": "False",
            "AllowWrite": "True",
            "AdviseType": "0",
            "B1": command.address.station,
            "B2": profile.block_b2,
            "B3": command.address.asdu,
            "B4": command.address.ioa,
            "Size": profile.block_size,
        }
        return self._object("IOBlock", name, path, source, overrides)

    def _element(self, block: E3Object, label: str, index: int, target_root: str) -> E3Object:
        name = f"{block.name}.{label}"
        path = f"{block.path_name}.{label}"
        return self._object(
            "IOBlockElement",
            name,
            path,
            block,
            {
                "ObjectType": "IOBlockElement",
                "Index": str(index),
                "PathName": path,
                "PathContainer": target_root,
            },
        )

    @staticmethod
    def _object(
        object_type: str, name: str, path: str, source: E3Object, overrides: dict[str, str]
    ) -> E3Object:
        values = {header: (source.property_value(header) or "") for header in SLAVE_HEADERS}
        values.update(overrides)
        values["ObjectType"] = object_type
        values["Name"] = name
        values["PathName"] = path
        properties = [E3Property(header, values[header]) for header in SLAVE_HEADERS]
        parent_path = name.rsplit(".", 1)[0] if "." in name else None
        return E3Object(
            object_type,
            path,
            name,
            parent_path,
            properties,
            source.original_row_index,
            [values[header] for header in SLAVE_HEADERS],
        )


@dataclass(slots=True)
class PreparedMasterToSlave:
    document: E3CSVDocument
    canonical: IEC104CanonicalDocument
    role: DriverRole
    plan: ConversionPlan
    target_document: E3CSVDocument
    target_canonical: IEC104CanonicalDocument


def prepare_master_to_slave(
    source: str | Path,
    profile: str = "PROJECT_PROFILE",
    import_columns: tuple[str, ...] | None = None,
) -> PreparedMasterToSlave:
    """Full dry-run: source audit, plan, materialized target, target audit and invariants."""
    document, canonical, role = read_source(source, import_columns)
    selected = get_profile(profile)
    source_audit = IEC104Auditor().audit(document, profile, role, canonical)
    plan = MasterToSlavePlanner().plan(document, canonical, source_audit, selected)
    plan.source_sha256 = document.source.sha256
    if role is not DriverRole.MASTER:
        plan.blocking_errors.append(f"SOURCE_ROLE_NOT_MASTER:{role.value}")
    target_document = MasterToSlaveTransformer().transform(document, canonical, plan, selected)
    evaluation = evaluate_target(plan, canonical, target_document, profile, DriverRole.SLAVE)
    return PreparedMasterToSlave(
        document, canonical, role, plan, target_document, evaluation.canonical
    )


class PlanMasterToSlaveConversion:
    def execute(
        self,
        source: str | Path,
        profile: str = "PROJECT_PROFILE",
        import_columns: tuple[str, ...] | None = None,
    ) -> ConversionPlan:
        return prepare_master_to_slave(source, profile, import_columns).plan


class ConvertMasterToSlave:
    def execute(
        self,
        source: str | Path,
        target: str | Path,
        profile: str = "PROJECT_PROFILE",
        export_columns: tuple[str, ...] | None = None,
        import_columns: tuple[str, ...] | None = None,
        expected_sha256: str | None = None,
    ) -> ConversionResult:
        ensure_distinct_paths(source, target)
        prepared = prepare_master_to_slave(source, profile, import_columns)
        plan = prepared.plan
        ensure_expected_source(plan, expected_sha256)
        target_audit = plan.target_audit
        assert target_audit is not None
        target_path = (
            None
            if plan.blocked
            else write_verified(prepared.target_document, target, export_columns)
        )
        canonical = prepared.canonical
        target_canonical = prepared.target_canonical
        summary = target_audit.summary
        return ConversionResult(
            source_role=prepared.role.value,
            target_role=DriverRole.SLAVE.value,
            profile=profile,
            source_count=len(prepared.document.objects),
            target_count=len(prepared.target_document.objects),
            monitoring_converted=len(canonical.points),
            commands_converted=sum(
                item.function is IEC104Function.COMMAND for item in canonical.commands
            ),
            setpoints_converted=sum(
                item.function is IEC104Function.SETPOINT for item in canonical.commands
            ),
            io_blocks_created=len(target_canonical.blocks),
            io_block_elements_created=sum(
                len(item.element_paths) for item in target_canonical.blocks
            ),
            warning_count=summary.warning_count,
            error_count=summary.error_count,
            blocking_count=plan.blocking_count,
            source_audit=plan.source_audit or target_audit,
            conversion_plan=plan,
            target_audit=target_audit,
            output_path=target_path,
            target_document=prepared.target_document,
            cross_validation=plan.cross_validation,
        )
