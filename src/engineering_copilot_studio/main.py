"""Application entry point."""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from .bootstrap import bootstrap_data


def main() -> int:
    bootstrap_data()
    from .ui import STYLE, MainWindow

    app = QApplication(sys.argv)
    app.setApplicationName("Engineering Copilot Studio")
    app.setStyleSheet(STYLE)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
