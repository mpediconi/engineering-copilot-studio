from __future__ import annotations

import json
from pathlib import Path

import pytest

from engineering_copilot_studio.gateway import (
    GatewayPoint,
    export_mapping,
    preview,
    validate_points,
)


def test_mapping_validation_and_offline_preview(tmp_path: Path) -> None:
    sample = {"plant": {"measurements": [{"power": 12.5, "quality": "GOOD"}]}}
    point = GatewayPoint(
        "Potência",
        "plant.measurements.0.power",
        13,
        1,
        100,
        scale=1000,
        unit="W",
        quality_path="plant.measurements.0.quality",
    )
    assert validate_points([point], sample) == []
    assert preview([point], sample)[0]["valor"] == 12500
    output = export_mapping(tmp_path / "mapping.json", [point], {"name": "API teste"})
    data = json.loads(output.read_text(encoding="utf-8"))
    assert data["mode"] == "offline_model"
    assert data["points"][0]["ioa"] == 100


def test_duplicate_address_and_wrong_asdu_block_export(tmp_path: Path) -> None:
    points = [
        GatewayPoint("A", "a", 13, 1, 7),
        GatewayPoint("B", "b", 45, 1, 7, direction="MONITORING"),
    ]
    findings = validate_points(points)
    assert sum(item["nivel"] == "ERRO" for item in findings) >= 2
    with pytest.raises(ValueError):
        export_mapping(tmp_path / "invalid.json", points, {})
