"""Create editable per-user data without writing into the source tree."""

from __future__ import annotations

import os
import shutil
from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def user_data_root() -> Path:
    base = Path(os.environ.get("LOCALAPPDATA") or Path.home() / ".local" / "share")
    return base / "Engineering Copilot Studio"


def bootstrap_data() -> Path:
    root = user_data_root()
    root.mkdir(parents=True, exist_ok=True)
    for folder, variable in (
        ("config", "IEC104_CSV_STUDIO_CONFIG_DIR"),
        ("golden_files", "IEC104_CSV_STUDIO_GOLDEN_FILES_DIR"),
    ):
        target = root / folder
        if not target.exists():
            source = project_root() / folder
            if not source.is_dir():
                source = Path(__file__).resolve().parent / "seeds" / folder
            shutil.copytree(source, target)
        os.environ[variable] = str(target)
    (root / "skills").mkdir(exist_ok=True)
    return root
