"""Offline REST/JSON to IEC104 mapping model. No network or control I/O."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

MONITORING_ASDUS = {1, 3, 9, 11, 13, 15, 30, 31, 34, 35, 36, 37}
COMMAND_ASDUS = {45, 46, 47, 48, 49, 50, 51, 58, 59, 60, 61, 62, 63, 64}


@dataclass(frozen=True)
class GatewayPoint:
    name: str
    json_path: str
    asdu: int
    common_address: int
    ioa: int
    direction: str = "MONITORING"
    scale: float = 1.0
    unit: str = ""
    quality_path: str = ""
    timestamp_path: str = ""


def read_path(payload: Any, path: str) -> Any:
    """Resolve a plain dotted path with optional numeric array indices."""
    value = payload
    for part in path.split("."):
        if not part:
            raise ValueError("O caminho JSON contém um segmento vazio.")
        if isinstance(value, list) and part.isdecimal():
            index = int(part)
            if index >= len(value):
                raise KeyError(path)
            value = value[index]
        elif isinstance(value, dict) and part in value:
            value = value[part]
        else:
            raise KeyError(path)
    return value


def validate_points(points: list[GatewayPoint], sample: Any | None = None) -> list[dict]:
    findings: list[dict] = []
    addresses: dict[tuple[int, int], str] = {}
    names: set[str] = set()
    for index, point in enumerate(points, 1):
        prefix = f"Linha {index}"
        if not point.name.strip() or not point.json_path.strip():
            findings.append({"nivel": "ERRO", "mensagem": f"{prefix}: nome e caminho JSON são obrigatórios."})
        if point.name.casefold() in names:
            findings.append({"nivel": "ERRO", "mensagem": f"{prefix}: nome duplicado: {point.name}."})
        names.add(point.name.casefold())
        address = (point.common_address, point.ioa)
        if address in addresses:
            findings.append({
                "nivel": "ERRO",
                "mensagem": f"{prefix}: CA/IOA duplicado com {addresses[address]}."
            })
        addresses[address] = point.name
        if not 1 <= point.common_address <= 65534 or not 1 <= point.ioa <= 16777215:
            findings.append({"nivel": "ERRO", "mensagem": f"{prefix}: CA ou IOA fora da faixa."})
        if point.direction == "MONITORING" and point.asdu not in MONITORING_ASDUS:
            findings.append({"nivel": "ERRO", "mensagem": f"{prefix}: ASDU incompatível com monitoração."})
        elif point.direction == "COMMAND" and point.asdu not in COMMAND_ASDUS:
            findings.append({"nivel": "ERRO", "mensagem": f"{prefix}: ASDU incompatível com comando."})
        elif point.direction not in {"MONITORING", "COMMAND"}:
            findings.append({"nivel": "ERRO", "mensagem": f"{prefix}: direção desconhecida."})
        if sample is not None:
            for label, path in (
                ("valor", point.json_path),
                ("qualidade", point.quality_path),
                ("timestamp", point.timestamp_path),
            ):
                if not path:
                    continue
                try:
                    read_path(sample, path)
                except (KeyError, ValueError):
                    findings.append({
                        "nivel": "REVISÃO",
                        "mensagem": f"{prefix}: caminho de {label} não encontrado: {path}."
                    })
    return findings


def preview(points: list[GatewayPoint], sample: Any) -> list[dict]:
    rows = []
    for point in points:
        try:
            raw = read_path(sample, point.json_path)
            value = raw * point.scale if isinstance(raw, (int, float)) else raw
        except (KeyError, ValueError, TypeError):
            value = None
        rows.append({
            "nome": point.name,
            "CA": point.common_address,
            "IOA": point.ioa,
            "ASDU": point.asdu,
            "valor": value,
            "unidade": point.unit,
            "qualidade": read_optional(sample, point.quality_path),
            "timestamp": read_optional(sample, point.timestamp_path),
        })
    return rows


def read_optional(sample: Any, path: str) -> Any:
    if not path:
        return None
    try:
        return read_path(sample, path)
    except (KeyError, ValueError):
        return None


def export_mapping(path: str | Path, points: list[GatewayPoint], source: dict) -> Path:
    findings = validate_points(points)
    if any(item["nivel"] == "ERRO" for item in findings):
        raise ValueError("O mapeamento contém erros. Corrija as linhas antes de exportar.")
    target = Path(path)
    if target.suffix.lower() != ".json":
        target = target.with_suffix(".json")
    payload = {
        "schema_version": 1,
        "mode": "offline_model",
        "source": source,
        "points": [asdict(point) for point in points],
    }
    temporary = target.with_name(target.name + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(target)
    return target
