"""Launch the migrated original E3 comparator without touching E3 projects."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

from ..bootstrap import project_root


def comparator_directory() -> Path:
    return project_root() / "tools" / "e3_comparator_original"


def comparator_script() -> Path:
    script = comparator_directory() / "E3_Comparador_Visual.ps1"
    if not script.is_file():
        raise FileNotFoundError(
            "O comparador original migrado não foi encontrado em "
            f"{comparator_directory()}."
        )
    return script


def launch_original_comparator() -> subprocess.Popen[bytes]:
    """Open the original Windows Forms visualizer in its migrated folder."""
    if os.name != "nt":
        raise RuntimeError("O comparador original usa Windows Forms e requer Windows.")
    script = comparator_script()
    return subprocess.Popen(
        [
            "powershell.exe",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(script),
        ],
        cwd=str(comparator_directory()),
        close_fds=True,
    )
