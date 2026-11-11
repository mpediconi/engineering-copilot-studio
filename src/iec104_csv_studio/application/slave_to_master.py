"""Slave/Distribuição to Master/Aquisição conversion workflow."""

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

from iec104_csv_studio.application.conversion_pipeline import (
    ensure_distinct_paths,
    ensure_expected_source,
    evaluate_target,
    read_source,
    source_gate_codes,
    write_verified,
)
from iec104_csv_studio.application.master_to_slave import (
    ConversionAction,
    ConversionActionKind,
    ConversionPlan,
    ConversionResult,
)
from iec104_csv_studio.domain.audit_models import DiagnosticSeverity, IEC104AuditReport
from iec104_csv_studio.domain.audit_rules import AuditRuleProfile, get_profile
from iec104_csv_studio.domain.auditor import IEC104Auditor
from iec104_csv_studio.domain.e3_models import E3CSVDocument, E3Object, E3Property, SourceMetadata
from iec104_csv_studio.domain.enums import DataFamily, DriverRole, IEC104Function
from iec104_csv_studio.domain.models import (
    IEC104Block,
    IEC104CanonicalDocument,
    IEC104Point,
)

MASTER_HEADERS = (
    "ObjectType",
    "Name",
    "AdviseType",
    "AlarmVerify",
    "AllowRead",
    "AllowWrite",
    "AsyncBatchFlushTimeMs",
    "AsyncBatchSize",
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
    "UseBitFields",
    "WriteFeedbackMode",
    "WriteNullAsEmpty",
    "WriteRetries",
    "WriteSyncMode",
)


class MasterCommandStrategy(StrEnum):
    EXECUTE = "EXECUTE"
    SELECT = "SELECT"
    SELECT_EXECUTE = "SELECT_EXECUTE"
    PROFILE_DEFAULT = "PROFILE_DEFAULT"
    REFERENCE_PRESERVING = "REFERENCE_PRESERVING"


def _source_root(document: E3CSVDocument) -> str:
    source = next((obj for obj in document.objects if obj.property_value("PathContainer")), None)
    return (source.property_value("PathContainer") or "") if source else ""


def _target_root(source_root: str) -> str:
    parent = source_root.rsplit(".", 1)[0] if "." in source_root else source_root
    return f"{parent}.[IEC104-MASTER]" if parent else "[IEC104-MASTER]"


class SlaveToMasterPlanner:
    """Create a dry-run plan for the reverse conversion."""

    def plan(
        self,
        document: E3CSVDocument,
        canonical: IEC104CanonicalDocument,
        source_audit: IEC104AuditReport,
        profile: AuditRuleProfile,
        strategy: MasterCommandStrategy = MasterCommandStrategy.PROFILE_DEFAULT,
    ) -> ConversionPlan:
        plan = ConversionPlan(
            source_role=DriverRole.SLAVE.value,
            target_role=DriverRole.MASTER.value,
            profile=profile.name,
            source_audit=source_audit,
            source_e3_objects_total=len(document.objects),
            source_iec104_objects=canonical.iec104_object_count
            + len(canonical.unclassified_objects),
            source_iotags=sum(obj.object_type == "IOTag" for obj in document.objects),
            source_monitoring_points=len(canonical.points),
            source_unknown_iotags=len(canonical.unclassified_objects),
            source_iofolders=sum(obj.object_type == "IOFolder" for obj in document.objects),
            source_ioblocks=len(canonical.blocks),
            source_ioblock_elements=sum(len(block.element_paths) for block in canonical.blocks),
            source_commands=sum(
                block.function is IEC104Function.COMMAND for block in canonical.blocks
            ),
            source_setpoints=sum(
                block.function is IEC104Function.SETPOINT for block in canonical.blocks
            ),
            monitoring_points=len(canonical.points),
            commands=sum(block.function is IEC104Function.COMMAND for block in canonical.blocks),
            setpoints=sum(block.function is IEC104Function.SETPOINT for block in canonical.blocks),
        )
        unknown_paths = {item.path_name for item in canonical.unclassified_objects}
        blocking_paths = {
            diagnostic.source_path
            for diagnostic in source_audit.diagnostics
            if diagnostic.severity is DiagnosticSeverity.BLOCKING
        }
        for obj in document.objects:
            if obj.object_type == "IODriver":
                self._skip(
                    plan, obj, "Driver root excluded; import under a preconfigured Master driver."
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
                reason = (
                    "EXTERNAL_REFERENCE_NOT_APPLICABLE"
                    if obj.object_type == "AgSimple"
                    else "Out of communication-scope conversion."
                )
                self._skip(plan, obj, reason)
            elif obj.object_type == "IOTag":
                if obj.path_name in unknown_paths:
                    self._skip(plan, obj, "UNCLASSIFIED_SOURCE_OBJECT")
                    plan.warnings.append("UNCLASSIFIED_SOURCE_OBJECT")
                else:
                    plan.actions.append(
                        ConversionAction(
                            ConversionActionKind.TRANSFORM,
                            obj.path_name,
                            obj.object_type,
                            target_object_type="IOTag",
                            reason=(
                                "Normalize Master monitoring properties from canonical "
                                "semantics."
                            ),
                        )
                    )
            elif obj.object_type == "IOBlock":
                if obj.path_name in blocking_paths:
                    # The diagnostic itself is added to blocking_errors below.
                    self._skip(plan, obj, "BLOCKING_SOURCE_DIAGNOSTIC")
                else:
                    plan.actions.append(
                        ConversionAction(
                            ConversionActionKind.TRANSFORM,
                            obj.path_name,
                            obj.object_type,
                            target_object_type="IOTag",
                            reason="Transform logical IOBlock to one Master IOTag.",
                        )
                    )
            elif obj.object_type == "IOBlockElement":
                plan.actions.append(
                    ConversionAction(
                        ConversionActionKind.REMOVE,
                        obj.path_name,
                        obj.object_type,
                        reason="SLAVE_COMMAND_STRUCTURE_NOT_USED_BY_MASTER",
                    )
                )
            else:
                self._skip(plan, obj, "Unsupported source object type.")
        for block in canonical.blocks:
            if block.function is IEC104Function.UNKNOWN:
                plan.warnings.append(f"UNSUPPORTED_TRANSFORMATION_RULE:{block.address.asdu}")
            plan.warnings.append(
                f"COMMAND_PHASE_RECONSTRUCTED_FROM_PROFILE:{block.address.station}/{block.address.asdu}/{block.address.ioa}"
            )
        for asdu in sorted(
            {
                point.address.asdu
                for point in canonical.points
                if profile.master_n2_for_asdu(point.address.asdu) is None
            }
        ):
            plan.warnings.append(f"UNSUPPORTED_TRANSFORMATION_RULE:{asdu}")
        source_gate_codes(plan, source_audit)
        plan.source_objects_in_scope = plan.objects_preserved + plan.objects_transformed
        plan.source_objects_out_of_scope = (
            plan.source_e3_objects_total - plan.source_objects_in_scope
        )
        return plan

    @staticmethod
    def _skip(plan: ConversionPlan, obj: E3Object, reason: str) -> None:
        plan.actions.append(
            ConversionAction(
                ConversionActionKind.SKIP, obj.path_name, obj.object_type, reason=reason
            )
        )


class SlaveToMasterTransformer:
    """Materialize Master E3 objects from canonical Slave semantics."""

    def transform(
        self,
        document: E3CSVDocument,
        canonical: IEC104CanonicalDocument,
        plan: ConversionPlan,
        profile: AuditRuleProfile,
        strategy: MasterCommandStrategy = MasterCommandStrategy.PROFILE_DEFAULT,
    ) -> E3CSVDocument:
        source_root = _source_root(document)
        target_root = _target_root(source_root)
        source_by_path: dict[str, E3Object] = {}
        for obj in document.objects:
            source_by_path.setdefault(obj.path_name, obj)
        points_by_path: dict[str, IEC104Point] = {}
        for point in canonical.points:
            if point.source is not None:
                points_by_path.setdefault(point.source.path_name, point)
        skipped = {
            action.source_path
            for action in plan.actions
            if action.kind is ConversionActionKind.SKIP
        }
        objects: list[E3Object] = []
        unknown = {item.path_name for item in canonical.unclassified_objects}
        for obj in document.objects:
            if obj.object_type == "IOFolder":
                objects.append(self._copy_object(obj, target_root, source_root))
            elif obj.object_type == "IOTag" and obj.path_name not in unknown:
                semantic = points_by_path.get(obj.path_name)
                if semantic is not None:
                    objects.append(
                        self._monitoring(obj, semantic, target_root, source_root, profile)
                    )
        for block in canonical.blocks:
            block_path = block.source.path_name if block.source else ""
            if block_path in skipped:
                continue
            source = source_by_path.get(block_path)
            if source is None:
                continue
            phases = self._phases(block, profile, strategy)
            if any(suffix.startswith(".") for suffix, _ in phases):
                # ".Select"/".Execute" tags live under a folder named after the block.
                objects.append(self._copy_object(source, target_root, source_root))
            for suffix, phase in phases:
                objects.append(
                    self._command(source, block, target_root, source_root, phase, suffix)
                )
        return E3CSVDocument(
            headers=list(MASTER_HEADERS),
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
    def _phases(
        block: IEC104Block,
        profile: AuditRuleProfile,
        strategy: MasterCommandStrategy,
    ) -> tuple[tuple[str, str], ...]:
        if strategy is MasterCommandStrategy.SELECT_EXECUTE:
            return ((".Select", "SELECT"), (".Execute", "EXECUTE"))
        if strategy is MasterCommandStrategy.SELECT:
            return (("", "SELECT"),)
        if strategy is MasterCommandStrategy.EXECUTE:
            return (("", "EXECUTE"),)
        if block.function is IEC104Function.SETPOINT:
            return (("", profile.master_setpoint_phase),)
        if block.data_family is DataFamily.BITSTRING:
            return (("", profile.master_bitstring_phase),)
        return (("", profile.master_command_phase),)

    def _monitoring(
        self,
        source: E3Object,
        point: IEC104Point,
        target_root: str,
        source_root: str,
        profile: AuditRuleProfile,
    ) -> E3Object:
        name = source.name.removeprefix(source_root + ".")
        path = f"{target_root}.{name}"
        # Without a profile rule keep the source priority instead of writing an empty N2.
        n2 = profile.master_n2_for_asdu(point.address.asdu) or point.raw_n2
        return self._object(
            "IOTag",
            name,
            path,
            source,
            {
                "PathContainer": target_root,
                "PathName": path,
                "AllowRead": "True",
                "AllowWrite": "False",
                "AdviseType": "0",
                "N1": point.address.station,
                "N2": n2,
                "N3": point.address.asdu,
                "N4": point.address.ioa,
            },
        )

    def _command(
        self,
        source: E3Object,
        block: IEC104Block,
        target_root: str,
        source_root: str,
        phase: str,
        suffix: str,
    ) -> E3Object:
        name = source.name.removeprefix(source_root + ".") + suffix
        path = f"{target_root}.{name}"
        n2 = {"SELECT": "10", "EXECUTE": "11", "CANCEL": "12"}.get(phase, "")
        return self._object(
            "IOTag",
            name,
            path,
            source,
            {
                "PathContainer": target_root,
                "PathName": path,
                "ObjectType": "IOTag",
                "AllowRead": "False",
                "AllowWrite": "False",
                "AdviseType": "0",
                "N1": block.address.station,
                "N2": n2,
                "N3": block.address.asdu,
                "N4": block.address.ioa,
            },
        )

    def _copy_object(self, source: E3Object, target_root: str, source_root: str) -> E3Object:
        name = source.name.removeprefix(source_root + ".")
        path = f"{target_root}.{name}"
        overrides = {"PathContainer": target_root, "PathName": path}
        if source.object_type != "IOFolder":
            # Folder synthesized from an IOBlock: drop communication properties.
            overrides.update(
                {
                    field: ""
                    for field in ("AllowRead", "AllowWrite", "AdviseType", "N1", "N2", "N3", "N4")
                }
            )
        return self._object("IOFolder", name, path, source, overrides)

    @staticmethod
    def _object(
        object_type: str,
        name: str,
        path: str,
        source: E3Object,
        overrides: dict[str, str],
    ) -> E3Object:
        values = {header: (source.property_value(header) or "") for header in MASTER_HEADERS}
        values.update(overrides)
        values["ObjectType"] = object_type
        values["Name"] = name
        values["PathName"] = path
        properties = [E3Property(header, values[header]) for header in MASTER_HEADERS]
        parent_path = name.rsplit(".", 1)[0] if "." in name else None
        return E3Object(
            object_type,
            path,
            name,
            parent_path,
            properties,
            source.original_row_index,
            [values[header] for header in MASTER_HEADERS],
        )


@dataclass(slots=True)
class PreparedSlaveToMaster:
    document: E3CSVDocument
    canonical: IEC104CanonicalDocument
    role: DriverRole
    plan: ConversionPlan
    target_document: E3CSVDocument


def prepare_slave_to_master(
    source: str | Path,
    profile: str = "PROJECT_PROFILE",
    strategy: MasterCommandStrategy = MasterCommandStrategy.PROFILE_DEFAULT,
    import_columns: tuple[str, ...] | None = None,
) -> PreparedSlaveToMaster:
    """Full dry-run: source audit, plan, materialized target, target audit and invariants."""
    document, canonical, role = read_source(source, import_columns)
    selected = get_profile(profile)
    source_audit = IEC104Auditor().audit(document, profile, role, canonical)
    plan = SlaveToMasterPlanner().plan(document, canonical, source_audit, selected, strategy)
    plan.source_sha256 = document.source.sha256
    if role is not DriverRole.SLAVE:
        plan.blocking_errors.append(f"SOURCE_ROLE_NOT_SLAVE:{role.value}")
    target_document = SlaveToMasterTransformer().transform(
        document, canonical, plan, selected, strategy
    )
    evaluate_target(plan, canonical, target_document, profile, DriverRole.MASTER)
    return PreparedSlaveToMaster(document, canonical, role, plan, target_document)


class PlanSlaveToMasterConversion:
    def execute(
        self,
        source: str | Path,
        profile: str = "PROJECT_PROFILE",
        strategy: MasterCommandStrategy = MasterCommandStrategy.PROFILE_DEFAULT,
        import_columns: tuple[str, ...] | None = None,
    ) -> ConversionPlan:
        return prepare_slave_to_master(source, profile, strategy, import_columns).plan


class ConvertSlaveToMaster:
    def execute(
        self,
        source: str | Path,
        target: str | Path,
        profile: str = "PROJECT_PROFILE",
        strategy: MasterCommandStrategy = MasterCommandStrategy.PROFILE_DEFAULT,
        export_columns: tuple[str, ...] | None = None,
        import_columns: tuple[str, ...] | None = None,
        expected_sha256: str | None = None,
    ) -> ConversionResult:
        ensure_distinct_paths(source, target)
        prepared = prepare_slave_to_master(source, profile, strategy, import_columns)
        plan = prepared.plan
        ensure_expected_source(plan, expected_sha256)
        target_audit = plan.target_audit
        assert target_audit is not None
        output_path = (
            None
            if plan.blocked
            else write_verified(prepared.target_document, target, export_columns)
        )
        canonical = prepared.canonical
        target_document = prepared.target_document
        summary = target_audit.summary
        return ConversionResult(
            source_role=prepared.role.value,
            target_role=DriverRole.MASTER.value,
            profile=profile,
            source_count=len(prepared.document.objects),
            target_count=len(target_document.objects),
            monitoring_converted=len(canonical.points),
            commands_converted=sum(
                block.function is IEC104Function.COMMAND for block in canonical.blocks
            ),
            setpoints_converted=sum(
                block.function is IEC104Function.SETPOINT for block in canonical.blocks
            ),
            io_blocks_created=0,
            io_block_elements_created=0,
            warning_count=summary.warning_count,
            error_count=summary.error_count,
            blocking_count=plan.blocking_count,
            source_audit=plan.source_audit or target_audit,
            conversion_plan=plan,
            target_audit=target_audit,
            output_path=output_path,
            target_document=target_document,
            cross_validation=plan.cross_validation,
            iotags_created=sum(obj.object_type == "IOTag" for obj in target_document.objects),
            ioblocks_removed=len(canonical.blocks),
            ioblock_elements_removed=sum(len(block.element_paths) for block in canonical.blocks),
            lossy_diagnostics=tuple(
                item for item in plan.warnings if item.startswith("COMMAND_PHASE_RECONSTRUCTED")
            ),
        )
