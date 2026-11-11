from __future__ import annotations

from pathlib import Path

import pytest

from engineering_copilot_studio import skills
from engineering_copilot_studio.e3.audit import audit_project, sha256_file
from engineering_copilot_studio.e3.comparator_launcher import (
    comparator_directory,
    comparator_script,
)


def test_user_skill_import_is_declarative(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(skills, "user_data_root", lambda: tmp_path / "user")
    source = tmp_path / "source" / "my-skill"
    source.mkdir(parents=True)
    (source / "SKILL.md").write_text(
        "---\nname: my-skill\ndescription: Exemplo\ngroup: Engenharia\n---\n"
        "# Exemplo\nVerifique a origem.\n",
        encoding="utf-8",
    )
    imported = skills.import_skill(source)
    assert imported.title == "my-skill"
    assert imported.action is None
    assert "Verifique a origem" in skills.load_user_skills()[0].instructions
    with pytest.raises(FileExistsError):
        skills.import_skill(source)


def test_e3_rejects_unsupported_file_without_modifying_it(tmp_path: Path) -> None:
    source = tmp_path / "sample.txt"
    source.write_text("not an E3 project", encoding="utf-8")
    before = sha256_file(source)
    with pytest.raises(ValueError):
        audit_project(str(source))
    assert sha256_file(source) == before


def test_migrated_original_comparator_is_complete() -> None:
    directory = comparator_directory()
    assert (directory / "comparar.py").is_file()
    assert (directory / "e3reader.py").is_file()
    assert (directory / "e3base.py").is_file()
    assert (directory / "patterns" / "modelo.json").is_file()
    assert comparator_script().name == "E3_Comparador_Visual.ps1"
