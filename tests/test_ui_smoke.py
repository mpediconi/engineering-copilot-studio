from __future__ import annotations

import os

from PySide6.QtWidgets import QApplication

from engineering_copilot_studio.bootstrap import bootstrap_data
from engineering_copilot_studio.ui import MainWindow


def test_navigation_and_built_in_skills() -> None:
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    bootstrap_data()
    app = QApplication.instance() or QApplication([])
    window = MainWindow()
    try:
        assert window.stack.count() == 5
        assert window.iec_page.tabs.count() == 5
        gateway = window.stack.widget(2)
        gateway.table.item(0, 1).setText("plant.power")
        assert gateway.points()[0].direction == "MONITORING"
        assert gateway.points()[0].json_path == "plant.power"
        window.navigation.setCurrentRow(4)
        assert window.stack.currentIndex() == 4
        assert window.stack.currentWidget().list.count() >= 10
    finally:
        window.close()
        app.processEvents()
