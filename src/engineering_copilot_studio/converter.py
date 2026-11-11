"""Typed façade over the existing IEC104 CSV Studio domain and use cases."""

from __future__ import annotations

from pathlib import Path

from iec104_csv_studio.application.analyze_csv import analyze_csv, compare_analyses
from iec104_csv_studio.application.generate_point_lists import (
    generate_acquisition_point_list,
    generate_distribution_point_list,
)
from iec104_csv_studio.application.master_to_slave import (
    ConvertMasterToSlave,
    PlanMasterToSlaveConversion,
)
from iec104_csv_studio.application.slave_to_master import (
    ConvertSlaveToMaster,
    MasterCommandStrategy,
    PlanSlaveToMasterConversion,
)
from iec104_csv_studio.infrastructure.data_setup_store import DataSetupStore
from iec104_csv_studio.infrastructure.profile_store import ProfileStore, profile_to_mapping


def analysis(path: str, profile: str) -> dict:
    result = analyze_csv(path, profile)
    report = result.audit
    summary = report.summary
    types: dict[str, int] = {}
    for obj in result.document.objects:
        types[obj.object_type] = types.get(obj.object_type, 0) + 1
    return {
        "arquivo": str(result.path),
        "papel": result.role.value,
        "confianca": round(result.confidence, 3),
        "monitoracao": result.monitoring_count,
        "comandos": result.command_count,
        "setpoints": result.setpoint_count,
        "resumo": {
            "informacoes": summary.info_count,
            "avisos": summary.warning_count,
            "erros": summary.error_count,
            "bloqueios": summary.blocking_count,
        },
        "asdu": list(result.asdu_breakdown),
        "tipos_objeto": types,
        "diagnosticos": [
            {
                "severidade": d.severity.value,
                "codigo": d.code,
                "mensagem": d.message,
                "caminho": d.source_path,
                "linha": d.row_index,
                "acao": d.suggested_action,
            }
            for d in report.diagnostics
        ],
    }


def compare(left: str, right: str, profile: str) -> dict[str, int]:
    return compare_analyses(analyze_csv(left, profile), analyze_csv(right, profile))


def plan_conversion(path: str, direction: str, profile: str, strategy: str) -> dict:
    if direction == "MASTER_TO_SLAVE":
        plan = PlanMasterToSlaveConversion().execute(path, profile)
    else:
        plan = PlanSlaveToMasterConversion().execute(
            path, profile, MasterCommandStrategy(strategy)
        )
    return {
        "bloqueado": plan.blocked,
        "erros_bloqueantes": list(plan.blocking_errors),
        "erros": list(plan.errors),
        "avisos": list(plan.warnings),
        "sha256_origem": plan.source_sha256,
        "objetos_destino": len(plan.target_document.objects) if hasattr(plan, "target_document") else None,
    }


def convert(
    source: str, target: str, direction: str, profile: str, strategy: str, sha256: str
) -> dict:
    if Path(source).resolve() == Path(target).resolve():
        raise ValueError("O destino deve ser diferente da origem.")
    if direction == "MASTER_TO_SLAVE":
        result = ConvertMasterToSlave().execute(
            source, target, profile, expected_sha256=sha256
        )
    else:
        result = ConvertSlaveToMaster().execute(
            source,
            target,
            profile,
            MasterCommandStrategy(strategy),
            expected_sha256=sha256,
        )
    return {
        "saida": str(result.output_path) if result.output_path else "",
        "origem": result.source_role,
        "destino": result.target_role,
        "objetos_origem": result.source_count,
        "objetos_destino": result.target_count,
        "avisos": result.warning_count,
        "erros": result.error_count,
        "bloqueios": result.blocking_count,
    }


def point_list(source: str, target: str, kind: str, profile: str) -> dict:
    action = (
        generate_acquisition_point_list
        if kind == "ACQUISITION"
        else generate_distribution_point_list
    )
    result = action(source, target, profile)
    return {
        "saida": str(result.output_path),
        "papel": result.role,
        "papel_incompativel": result.role_mismatch,
        "pontos": result.point_counts,
        "diagnosticos": result.diagnostic_counts,
    }


def profiles() -> list[dict]:
    store = ProfileStore()
    return [profile_to_mapping(item) for item in store.load()]


def save_profile(payload: dict) -> dict:
    return profile_to_mapping(ProfileStore().save(payload))


def delete_profile(name: str) -> None:
    ProfileStore().remove(name)


def data_setup() -> DataSetupStore:
    return DataSetupStore()
