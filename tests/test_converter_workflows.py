from __future__ import annotations

import hashlib
from pathlib import Path

from engineering_copilot_studio import converter
from engineering_copilot_studio.bootstrap import bootstrap_data, project_root


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_both_conversion_directions_and_point_lists(tmp_path: Path) -> None:
    bootstrap_data()
    master = project_root() / "golden_files" / "MasterIEC104 modelo.CSV"
    slave = project_root() / "golden_files" / "SlaveIEC104 modelo.CSV"
    original_hashes = digest(master), digest(slave)

    master_audit = converter.analysis(str(master), "PROJECT_PROFILE")
    slave_audit = converter.analysis(str(slave), "PROJECT_PROFILE")
    assert master_audit["papel"] == "MASTER"
    assert slave_audit["papel"] == "SLAVE"
    assert master_audit["monitoracao"] > 0
    assert slave_audit["monitoracao"] > 0

    for source, direction, kind, output_name in (
        (master, "MASTER_TO_SLAVE", "ACQUISITION", "slave.csv"),
        (slave, "SLAVE_TO_MASTER", "DISTRIBUTION", "master.csv"),
    ):
        plan = converter.plan_conversion(
            str(source), direction, "PROJECT_PROFILE", "PROFILE_DEFAULT"
        )
        assert not plan["bloqueado"]
        converted = converter.convert(
            str(source),
            str(tmp_path / output_name),
            direction,
            "PROJECT_PROFILE",
            "PROFILE_DEFAULT",
            plan["sha256_origem"],
        )
        assert converted["saida"]
        assert (tmp_path / output_name).is_file()
        points = converter.point_list(
            str(source), str(tmp_path / f"{kind}.xlsx"), kind, "PROJECT_PROFILE"
        )
        assert Path(points["saida"]).is_file()
        assert not points["papel_incompativel"]

    assert (digest(master), digest(slave)) == original_hashes
