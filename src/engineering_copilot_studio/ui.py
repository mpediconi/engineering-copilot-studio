"""PySide6 desktop shell and task-oriented screens."""

from __future__ import annotations

import json
import shutil
from collections.abc import Callable
from functools import partial
from pathlib import Path

from PySide6.QtCore import QObject, QRunnable, Qt, QThreadPool, Signal
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFileDialog,
    QFormLayout,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QSplitter,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from . import converter
from .bootstrap import user_data_root
from .e3.audit import audit_project, compare_projects
from .e3.comparator_launcher import launch_original_comparator
from .gateway import GatewayPoint, export_mapping, preview, validate_points
from .skills import all_skills, import_skill, import_skill_collection

STYLE = """
QMainWindow, QWidget { background: #f5f7fa; color: #1c2a39; font: 10pt 'Segoe UI'; }
QListWidget#navigation { background: #15243a; color: #dce8f4; border: 0; font-size: 11pt; }
QListWidget#navigation::item { padding: 14px 18px; border-radius: 7px; margin: 3px 8px; }
QListWidget#navigation::item:selected { background: #2068a3; color: white; }
QFrame#card { background: white; border: 1px solid #dce4eb; border-radius: 10px; }
QPushButton { background: #e9f0f6; border: 1px solid #c4d4e1; border-radius: 6px; padding: 8px 13px; }
QPushButton:hover { background: #dcebf6; }
QPushButton#primary { background: #176ba5; color: white; border: 1px solid #176ba5; font-weight: 600; }
QPushButton#primary:hover { background: #135b8e; }
QLineEdit, QComboBox, QPlainTextEdit, QTableWidget { background: white; border: 1px solid #cdd9e3; border-radius: 5px; padding: 5px; }
QTabWidget::pane { border: 1px solid #dce4eb; background: white; }
QTabBar::tab { padding: 9px 15px; }
QTabBar::tab:selected { color: #176ba5; font-weight: 600; }
QLabel#heading { font-size: 20pt; font-weight: 700; }
QLabel#subtitle { color: #526679; }
"""


class WorkerSignals(QObject):
    result = Signal(object)
    error = Signal(str)
    finished = Signal()


class TaskWorker(QRunnable):
    def __init__(self, function: Callable[[], object]) -> None:
        super().__init__()
        self.function = function
        self.signals = WorkerSignals()

    def run(self) -> None:
        try:
            self.signals.result.emit(self.function())
        except Exception as exc:
            self.signals.error.emit(f"{type(exc).__name__}: {exc}")
        finally:
            self.signals.finished.emit()


def heading(title: str, subtitle: str) -> QWidget:
    container = QWidget()
    layout = QVBoxLayout(container)
    title_label = QLabel(title)
    title_label.setObjectName("heading")
    description = QLabel(subtitle)
    description.setObjectName("subtitle")
    description.setWordWrap(True)
    layout.addWidget(title_label)
    layout.addWidget(description)
    return container


def file_selector(parent: QWidget, title: str, filter_text: str) -> tuple[QWidget, QLineEdit]:
    row = QWidget()
    layout = QHBoxLayout(row)
    layout.setContentsMargins(0, 0, 0, 0)
    field = QLineEdit()
    field.setPlaceholderText(title)
    button = QPushButton("Escolher…")

    def choose() -> None:
        path, _ = QFileDialog.getOpenFileName(parent, title, field.text(), filter_text)
        if path:
            field.setText(path)

    button.clicked.connect(choose)
    layout.addWidget(field, 1)
    layout.addWidget(button)
    return row, field


def pretty(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, default=str)


def result_box() -> QPlainTextEdit:
    box = QPlainTextEdit()
    box.setReadOnly(True)
    box.setPlaceholderText("O resultado aparecerá aqui.")
    return box


class IECPage(QWidget):
    def __init__(self, host: MainWindow) -> None:
        super().__init__()
        self.host = host
        self.plan_sha = ""
        self.plan_context: tuple[str, str, str, str] | None = None
        self.profile_data: list[dict] = []
        outer = QVBoxLayout(self)
        outer.addWidget(heading("IEC 104", "Analise CSVs E3, converta entre Master e Slave e gere listas de pontos."))
        self.tabs = QTabWidget()
        outer.addWidget(self.tabs, 1)
        self._analysis_tab()
        self._conversion_tab()
        self._lists_tab()
        self._profiles_tab()
        self._reference_tab()
        self.refresh_profiles()

    def _profile_box(self) -> QComboBox:
        box = QComboBox()
        box.addItems(["PROJECT_PROFILE", "ELIPSE_DOCUMENTED"])
        return box

    def _analysis_tab(self) -> None:
        page = QWidget()
        layout = QVBoxLayout(page)
        self.analysis_data: dict | None = None
        form = QFormLayout()
        row, self.analysis_file = file_selector(page, "CSV principal", "CSV (*.csv *.CSV)")
        form.addRow("CSV principal", row)
        row, self.compare_file = file_selector(page, "CSV para comparação", "CSV (*.csv *.CSV)")
        form.addRow("Comparar com", row)
        self.analysis_profile = self._profile_box()
        form.addRow("Perfil", self.analysis_profile)
        layout.addLayout(form)
        actions = QHBoxLayout()
        analyze_button = QPushButton("Analisar e auditar")
        analyze_button.setObjectName("primary")
        compare_button = QPushButton("Comparar dois CSVs")
        save_button = QPushButton("Salvar relatório JSON")
        analyze_button.clicked.connect(self.analyze)
        compare_button.clicked.connect(self.compare)
        save_button.clicked.connect(self.save_analysis)
        actions.addWidget(analyze_button)
        actions.addWidget(compare_button)
        actions.addWidget(save_button)
        actions.addStretch()
        layout.addLayout(actions)
        self.analysis_summary = QLabel("Selecione um CSV para iniciar.")
        self.analysis_summary.setWordWrap(True)
        layout.addWidget(self.analysis_summary)
        self.analysis_table = QTableWidget(0, 4)
        self.analysis_table.setHorizontalHeaderLabels(("Nível", "Código", "Mensagem", "Linha"))
        self.analysis_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.analysis_table.setColumnWidth(0, 85)
        self.analysis_table.setColumnWidth(1, 220)
        self.analysis_table.setColumnWidth(3, 65)
        self.analysis_result = result_box()
        self.analysis_views = QTabWidget()
        self.analysis_views.addTab(self.analysis_table, "Diagnósticos")
        self.analysis_views.addTab(self.analysis_result, "JSON completo")
        layout.addWidget(self.analysis_views, 1)
        self.tabs.addTab(page, "Análise")

    def analyze(self) -> None:
        path = self.analysis_file.text().strip()
        if not Path(path).is_file():
            self.host.show_error("Selecione um CSV existente.")
            return
        self.host.run_task(
            "Analisando CSV",
            partial(converter.analysis, path, self.analysis_profile.currentText()),
            self.render_analysis,
        )

    def render_analysis(self, result: dict) -> None:
        self.analysis_data = result
        counts = result["resumo"]
        self.analysis_summary.setText(
            f"{result['papel']} · {result['monitoracao']} pontos de monitoração · "
            f"{result['comandos']} comandos · {result['setpoints']} setpoints · "
            f"{counts['avisos']} avisos · {counts['erros']} erros · {counts['bloqueios']} bloqueios. "
            "A tabela mostra até 1.000 diagnósticos; o JSON contém todos."
        )
        diagnostics = result["diagnosticos"]
        self.analysis_table.setRowCount(min(len(diagnostics), 1000))
        for row, item in enumerate(diagnostics[:1000]):
            for column, key in enumerate(("severidade", "codigo", "mensagem", "linha")):
                self.analysis_table.setItem(row, column, QTableWidgetItem(str(item.get(key) or "")))
        self.analysis_result.setPlainText(pretty(result))
        self.analysis_views.setCurrentWidget(self.analysis_table)

    def compare(self) -> None:
        left, right = self.analysis_file.text().strip(), self.compare_file.text().strip()
        if not Path(left).is_file() or not Path(right).is_file():
            self.host.show_error("Selecione os dois CSVs para comparar.")
            return
        self.host.run_task(
            "Comparando CSVs",
            partial(converter.compare, left, right, self.analysis_profile.currentText()),
            self.render_comparison,
        )

    def render_comparison(self, result: dict) -> None:
        self.analysis_data = {"comparacao": result}
        self.analysis_summary.setText("Comparação canônica concluída. Veja as estatísticas no JSON.")
        self.analysis_result.setPlainText(pretty(self.analysis_data))
        self.analysis_views.setCurrentWidget(self.analysis_result)

    def save_analysis(self) -> None:
        if self.analysis_data is None:
            self.host.show_error("Execute uma análise ou comparação antes de salvar.")
            return
        path, _ = QFileDialog.getSaveFileName(self, "Salvar relatório IEC 104", "", "JSON (*.json)")
        if not path:
            return
        if Path(path).exists() and QMessageBox.question(
            self, "Sobrescrever relatório?", "O arquivo já existe. Sobrescrever?"
        ) != QMessageBox.StandardButton.Yes:
            return
        Path(path).write_text(pretty(self.analysis_data) + "\n", encoding="utf-8")
        self.host.notice("Relatório IEC 104 exportado.")

    def _conversion_tab(self) -> None:
        page = QWidget()
        layout = QVBoxLayout(page)
        form = QFormLayout()
        row, self.conversion_file = file_selector(page, "CSV de origem", "CSV (*.csv *.CSV)")
        form.addRow("CSV de origem", row)
        self.direction = QComboBox()
        self.direction.addItem("Master → Slave", "MASTER_TO_SLAVE")
        self.direction.addItem("Slave → Master", "SLAVE_TO_MASTER")
        form.addRow("Direção", self.direction)
        self.conversion_profile = self._profile_box()
        form.addRow("Perfil", self.conversion_profile)
        self.strategy = QComboBox()
        for item in ("PROFILE_DEFAULT", "EXECUTE", "SELECT", "SELECT_EXECUTE", "REFERENCE_PRESERVING"):
            self.strategy.addItem(item.replace("_", " ").title(), item)
        self.strategy.setEnabled(False)
        self.direction.currentIndexChanged.connect(
            lambda: self.strategy.setEnabled(self.direction.currentData() == "SLAVE_TO_MASTER")
        )
        form.addRow("Comando no Master", self.strategy)
        layout.addLayout(form)
        actions = QHBoxLayout()
        plan_button = QPushButton("1. Gerar plano")
        plan_button.setObjectName("primary")
        self.export_button = QPushButton("2. Exportar CSV")
        self.export_button.setEnabled(False)
        plan_button.clicked.connect(self.plan)
        self.export_button.clicked.connect(self.export)
        actions.addWidget(plan_button)
        actions.addWidget(self.export_button)
        actions.addStretch()
        layout.addLayout(actions)
        self.conversion_result = result_box()
        layout.addWidget(self.conversion_result, 1)
        for widget in (self.conversion_file, self.direction, self.conversion_profile, self.strategy):
            if isinstance(widget, QLineEdit):
                widget.textChanged.connect(self.invalidate_plan)
            else:
                widget.currentIndexChanged.connect(self.invalidate_plan)
        self.tabs.addTab(page, "Conversão")

    def _conversion_context(self) -> tuple[str, str, str, str]:
        return (
            self.conversion_file.text().strip(),
            self.direction.currentData(),
            self.conversion_profile.currentText(),
            self.strategy.currentData(),
        )

    def invalidate_plan(self, *_: object) -> None:
        self.plan_sha = ""
        self.plan_context = None
        self.export_button.setEnabled(False)

    def plan(self) -> None:
        context = self._conversion_context()
        if not Path(context[0]).is_file():
            self.host.show_error("Selecione um CSV de origem existente.")
            return
        self.invalidate_plan()

        def done(result: dict) -> None:
            self.conversion_result.setPlainText(pretty(result))
            if not result["bloqueado"]:
                self.plan_sha = result["sha256_origem"]
                self.plan_context = context
                self.export_button.setEnabled(True)

        self.host.run_task("Planejando conversão", partial(converter.plan_conversion, *context), done)

    def export(self) -> None:
        if self.plan_context != self._conversion_context() or not self.plan_sha:
            self.host.show_error("Gere um plano atualizado antes de exportar.")
            return
        target, _ = QFileDialog.getSaveFileName(self, "Salvar CSV convertido", "", "CSV (*.csv)")
        if not target:
            return
        if Path(target).exists() and QMessageBox.question(
            self, "Sobrescrever destino?", "O CSV de destino já existe. Sobrescrever?"
        ) != QMessageBox.StandardButton.Yes:
            return
        source, direction, profile, strategy = self.plan_context
        self.host.run_task(
            "Exportando conversão",
            partial(converter.convert, source, target, direction, profile, strategy, self.plan_sha),
            lambda result: self.conversion_result.setPlainText(pretty(result)),
        )

    def _lists_tab(self) -> None:
        page = QWidget()
        layout = QVBoxLayout(page)
        form = QFormLayout()
        row, self.list_file = file_selector(page, "CSV de origem", "CSV (*.csv *.CSV)")
        form.addRow("CSV de origem", row)
        self.list_kind = QComboBox()
        self.list_kind.addItem("Aquisição (Master)", "ACQUISITION")
        self.list_kind.addItem("Distribuição (Slave)", "DISTRIBUTION")
        form.addRow("Tipo de lista", self.list_kind)
        self.list_profile = self._profile_box()
        form.addRow("Perfil", self.list_profile)
        layout.addLayout(form)
        button = QPushButton("Gerar planilha XLSX")
        button.setObjectName("primary")
        button.clicked.connect(self.make_list)
        layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.list_result = result_box()
        layout.addWidget(self.list_result, 1)
        self.tabs.addTab(page, "Listas de pontos")

    def make_list(self) -> None:
        source = self.list_file.text().strip()
        if not Path(source).is_file():
            self.host.show_error("Selecione um CSV de origem existente.")
            return
        target, _ = QFileDialog.getSaveFileName(self, "Salvar lista de pontos", "", "Excel (*.xlsx)")
        if not target:
            return
        if Path(target).exists() and QMessageBox.question(
            self, "Sobrescrever destino?", "A planilha já existe. Sobrescrever?"
        ) != QMessageBox.StandardButton.Yes:
            return
        self.host.run_task(
            "Gerando lista",
            partial(converter.point_list, source, target, self.list_kind.currentData(), self.list_profile.currentText()),
            lambda result: self.list_result.setPlainText(pretty(result)),
        )

    def _profiles_tab(self) -> None:
        page = QWidget()
        layout = QVBoxLayout(page)
        label = QLabel("Escolha um perfil. Para criar outro, copie um existente e altere o nome no JSON.")
        label.setWordWrap(True)
        layout.addWidget(label)
        self.profile_list = QListWidget()
        self.profile_list.currentRowChanged.connect(self.load_selected_profile)
        self.profile_editor = QPlainTextEdit()
        splitter = QSplitter()
        splitter.addWidget(self.profile_list)
        splitter.addWidget(self.profile_editor)
        splitter.setStretchFactor(1, 3)
        layout.addWidget(splitter, 1)
        actions = QHBoxLayout()
        for title, action in (
            ("Copiar perfil", self.copy_profile),
            ("Salvar perfil", self.save_profile),
            ("Excluir perfil", self.remove_profile),
        ):
            button = QPushButton(title)
            button.clicked.connect(action)
            actions.addWidget(button)
        actions.addStretch()
        layout.addLayout(actions)
        self.tabs.addTab(page, "Perfis")

    def refresh_profiles(self) -> None:
        try:
            self.profile_data = converter.profiles()
        except Exception as exc:
            self.host.show_error(str(exc))
            self.profile_data = []
        self.profile_list.clear()
        self.profile_list.addItems([str(item["id"]) for item in self.profile_data])
        names = [str(item["id"]) for item in self.profile_data]
        for box in (self.analysis_profile, self.conversion_profile, self.list_profile):
            current = box.currentText()
            box.clear()
            box.addItems(names)
            box.setCurrentText(current if current in names else "PROJECT_PROFILE")

    def load_selected_profile(self, row: int) -> None:
        if 0 <= row < len(self.profile_data):
            self.profile_editor.setPlainText(pretty(self.profile_data[row]))

    def copy_profile(self) -> None:
        row = self.profile_list.currentRow()
        if row < 0:
            self.host.show_error("Selecione um perfil para copiar.")
            return
        value = dict(self.profile_data[row])
        value["id"] = "NOVO_PERFIL"
        self.profile_editor.setPlainText(pretty(value))

    def save_profile(self) -> None:
        try:
            payload = json.loads(self.profile_editor.toPlainText())
            converter.save_profile(payload)
        except Exception as exc:
            self.host.show_error(str(exc))
            return
        self.refresh_profiles()
        self.host.notice("Perfil salvo.")

    def remove_profile(self) -> None:
        row = self.profile_list.currentRow()
        if row < 0:
            return
        name = str(self.profile_data[row]["id"])
        if QMessageBox.question(
            self, "Excluir perfil?", f"Excluir o perfil {name}?"
        ) != QMessageBox.StandardButton.Yes:
            return
        try:
            converter.delete_profile(name)
            self.refresh_profiles()
        except Exception as exc:
            self.host.show_error(str(exc))

    def _reference_tab(self) -> None:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("Golden Files: exemplos editáveis para análise e comparação."))
        self.golden_list = QListWidget()
        layout.addWidget(self.golden_list, 1)
        actions = QHBoxLayout()
        import_button = QPushButton("Adicionar CSV")
        import_button.clicked.connect(self.import_golden)
        edit_button = QPushButton("Editar CSV")
        edit_button.clicked.connect(self.edit_golden)
        remove_button = QPushButton("Remover CSV")
        remove_button.clicked.connect(self.remove_golden)
        self.golden_role = QComboBox()
        self.golden_role.addItems(["MASTER", "SLAVE"])
        assign_button = QPushButton("Atribuir ao papel")
        assign_button.clicked.connect(self.assign_golden)
        actions.addWidget(import_button)
        actions.addWidget(edit_button)
        actions.addWidget(remove_button)
        actions.addWidget(self.golden_role)
        actions.addWidget(assign_button)
        actions.addStretch()
        layout.addLayout(actions)
        form = QFormLayout()
        self.import_columns = QLineEdit()
        self.export_columns = QLineEdit()
        form.addRow("Colunas importadas", self.import_columns)
        form.addRow("Colunas exportadas", self.export_columns)
        layout.addLayout(form)
        save_button = QPushButton("Salvar colunas padrão")
        save_button.clicked.connect(self.save_columns)
        layout.addWidget(save_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.reference_result = result_box()
        layout.addWidget(self.reference_result, 1)
        types_button = QPushButton("Descobrir ObjectTypes do CSV selecionado")
        types_button.clicked.connect(self.show_object_types)
        layout.addWidget(types_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.tabs.addTab(page, "Dados de referência")
        self.refresh_reference()

    def refresh_reference(self) -> None:
        store = converter.data_setup()
        from iec104_csv_studio.infrastructure.application_paths import golden_files_directory
        files = sorted(p.name for p in golden_files_directory().glob("*") if p.suffix.lower() == ".csv")
        self.golden_list.clear()
        self.golden_list.addItems(files)
        self.import_columns.setText(", ".join(store.import_columns))
        self.export_columns.setText(", ".join(store.export_columns))
        self.reference_result.setPlainText(pretty({"atribuicoes": store.assignments, "CSVs": files}))

    def import_golden(self) -> None:
        path, _ = QFileDialog.getOpenFileName(self, "Adicionar Golden File", "", "CSV (*.csv *.CSV)")
        if not path:
            return
        from iec104_csv_studio.infrastructure.application_paths import golden_files_directory
        target = golden_files_directory() / Path(path).name
        if target.exists():
            self.host.show_error("Já existe um Golden File com esse nome.")
            return
        shutil.copy2(path, target)
        self.refresh_reference()

    def _selected_golden_path(self) -> Path | None:
        item = self.golden_list.currentItem()
        if item is None:
            self.host.show_error("Selecione um Golden File.")
            return None
        from iec104_csv_studio.infrastructure.application_paths import golden_files_directory

        return golden_files_directory() / item.text()

    def edit_golden(self) -> None:
        path = self._selected_golden_path()
        if path is None:
            return
        dialog = QDialog(self)
        dialog.setWindowTitle(f"Editar {path.name}")
        dialog.resize(1000, 680)
        layout = QVBoxLayout(dialog)
        layout.addWidget(QLabel("Edite a cópia local. Salvar substitui somente este Golden File."))
        editor = QPlainTextEdit()
        try:
            editor.setPlainText(path.read_text(encoding="utf-8-sig"))
        except (OSError, UnicodeError) as exc:
            self.host.show_error(str(exc))
            return
        layout.addWidget(editor, 1)
        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel
        )
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        temporary = path.with_name(path.name + ".tmp")
        try:
            temporary.write_text(editor.toPlainText(), encoding="utf-8", newline="")
            from iec104_csv_studio.infrastructure.e3_csv_reader import read_e3_csv

            read_e3_csv(temporary)
            temporary.replace(path)
            self.refresh_reference()
            self.host.notice("Golden File salvo.")
        except Exception as exc:
            temporary.unlink(missing_ok=True)
            self.host.show_error(str(exc))

    def remove_golden(self) -> None:
        path = self._selected_golden_path()
        if path is None:
            return
        if QMessageBox.question(
            self, "Remover Golden File?", f"Remover a cópia local {path.name}?"
        ) != QMessageBox.StandardButton.Yes:
            return
        try:
            converter.data_setup().forget_golden(path.name)
            path.unlink()
            self.refresh_reference()
            self.host.notice("Golden File removido.")
        except Exception as exc:
            self.host.show_error(str(exc))

    def show_object_types(self) -> None:
        path = self._selected_golden_path()
        if path is None:
            return
        self.host.run_task(
            "Descobrindo ObjectTypes",
            partial(converter.analysis, str(path), "PROJECT_PROFILE"),
            lambda result: self.reference_result.setPlainText(pretty(result["tipos_objeto"])),
        )

    def assign_golden(self) -> None:
        item = self.golden_list.currentItem()
        if item is None:
            self.host.show_error("Selecione um Golden File.")
            return
        try:
            converter.data_setup().assign_golden(self.golden_role.currentText(), item.text())
            self.refresh_reference()
        except Exception as exc:
            self.host.show_error(str(exc))

    def save_columns(self) -> None:
        try:
            converter.data_setup().save_columns(
                self.import_columns.text(), self.export_columns.text()
            )
            self.refresh_reference()
            self.host.notice("Colunas padrão salvas.")
        except Exception as exc:
            self.host.show_error(str(exc))


class GatewayPage(QWidget):
    HEADERS = ("Nome", "Caminho JSON", "ASDU", "CA", "IOA", "Direção", "Escala", "Unidade", "Qualidade", "Timestamp")

    def __init__(self, host: MainWindow) -> None:
        super().__init__()
        self.host = host
        outer = QVBoxLayout(self)
        outer.addWidget(heading(
            "Gateway API → IEC 104",
            "Modele pontos a partir de JSON e valide CA, IOA, ASDU, qualidade e timestamp sem acessar a rede.",
        ))
        form = QFormLayout()
        self.source_name = QLineEdit()
        self.source_name.setPlaceholderText("Ex.: API de inversores")
        self.endpoint = QLineEdit()
        self.endpoint.setPlaceholderText("URL de referência; nenhuma chamada será feita")
        form.addRow("Fonte", self.source_name)
        form.addRow("Endpoint", self.endpoint)
        outer.addLayout(form)
        self.sample = QPlainTextEdit()
        self.sample.setPlaceholderText('Cole uma amostra JSON, por exemplo: {"plant": {"power": 12.5}}')
        self.sample.setMaximumHeight(115)
        outer.addWidget(self.sample)
        sample_actions = QHBoxLayout()
        load_sample = QPushButton("Abrir amostra JSON")
        load_sample.clicked.connect(self.open_sample)
        sample_actions.addWidget(load_sample)
        sample_actions.addStretch()
        outer.addLayout(sample_actions)
        self.table = QTableWidget(0, len(self.HEADERS))
        self.table.setHorizontalHeaderLabels(self.HEADERS)
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        outer.addWidget(self.table, 1)
        actions = QHBoxLayout()
        for title, action in (
            ("Adicionar ponto", self.add_point),
            ("Remover linha", self.remove_point),
            ("Validar e prévia", self.validate),
            ("Exportar mapeamento", self.export),
        ):
            button = QPushButton(title)
            if title == "Validar e prévia":
                button.setObjectName("primary")
            button.clicked.connect(action)
            actions.addWidget(button)
        actions.addStretch()
        outer.addLayout(actions)
        self.result = result_box()
        self.result.setMaximumHeight(190)
        outer.addWidget(self.result)
        self.add_point()

    def add_point(self) -> None:
        row = self.table.rowCount()
        self.table.insertRow(row)
        defaults = (f"PONTO_{row+1}", "", "13", "1", str(row + 1), "MONITORING", "1", "", "", "")
        for column, value in enumerate(defaults):
            if column == 5:
                direction = QComboBox()
                direction.addItems(["MONITORING", "COMMAND"])
                self.table.setCellWidget(row, column, direction)
            else:
                self.table.setItem(row, column, QTableWidgetItem(value))

    def remove_point(self) -> None:
        row = self.table.currentRow()
        if row >= 0:
            self.table.removeRow(row)

    def open_sample(self) -> None:
        path, _ = QFileDialog.getOpenFileName(self, "Abrir amostra JSON", "", "JSON (*.json)")
        if path:
            self.sample.setPlainText(Path(path).read_text(encoding="utf-8"))

    def points(self) -> list[GatewayPoint]:
        points = []
        for row in range(self.table.rowCount()):
            values = [
                self.table.cellWidget(row, column).currentText().strip()
                if isinstance(self.table.cellWidget(row, column), QComboBox)
                else (
                    self.table.item(row, column).text().strip()
                    if self.table.item(row, column) else ""
                )
                for column in range(len(self.HEADERS))
            ]
            points.append(GatewayPoint(
                name=values[0],
                json_path=values[1],
                asdu=int(values[2]),
                common_address=int(values[3]),
                ioa=int(values[4]),
                direction=values[5].upper(),
                scale=float(values[6]),
                unit=values[7],
                quality_path=values[8],
                timestamp_path=values[9],
            ))
        return points

    def _sample_payload(self) -> object | None:
        content = self.sample.toPlainText().strip()
        return json.loads(content) if content else None

    def validate(self) -> None:
        try:
            points = self.points()
            sample = self._sample_payload()
            findings = validate_points(points, sample)
            result = {"pontos": len(points), "achados": findings}
            if sample is not None:
                result["previa"] = preview(points, sample)
            self.result.setPlainText(pretty(result))
        except Exception as exc:
            self.host.show_error(str(exc))

    def export(self) -> None:
        try:
            points = self.points()
            sample = self._sample_payload()
            findings = validate_points(points, sample)
            if any(item["nivel"] == "ERRO" for item in findings):
                self.result.setPlainText(pretty({"achados": findings}))
                self.host.show_error("Corrija os erros de mapeamento antes de exportar.")
                return
        except Exception as exc:
            self.host.show_error(str(exc))
            return
        path, _ = QFileDialog.getSaveFileName(self, "Salvar mapeamento", "", "JSON (*.json)")
        if not path:
            return
        if Path(path).exists() and QMessageBox.question(
            self, "Sobrescrever arquivo?", "O mapeamento já existe. Sobrescrever?"
        ) != QMessageBox.StandardButton.Yes:
            return
        try:
            output = export_mapping(
                path, points,
                {"name": self.source_name.text().strip(), "endpoint_reference": self.endpoint.text().strip()},
            )
            self.result.setPlainText(pretty({"arquivo": str(output), "achados": findings}))
            self.host.notice("Mapeamento exportado.")
        except Exception as exc:
            self.host.show_error(str(exc))


class E3Page(QWidget):
    def __init__(self, host: MainWindow) -> None:
        super().__init__()
        self.host = host
        self.report: dict | None = None
        outer = QVBoxLayout(self)
        outer.addWidget(heading(
            "Projetos Elipse E3",
            "Inventário estático de objetos e propriedades em arquivos .prj e .lib, com hash e cobertura.",
        ))
        row, self.file = file_selector(self, "Projeto .prj ou biblioteca .lib", "Elipse E3 (*.prj *.lib)")
        outer.addWidget(row)
        row, self.compare_file = file_selector(self, "Versão E3 para comparar", "Elipse E3 (*.prj *.lib)")
        outer.addWidget(row)
        actions = QHBoxLayout()
        analyze = QPushButton("Inspecionar projeto")
        analyze.setObjectName("primary")
        analyze.clicked.connect(self.analyze)
        compare_button = QPushButton("Comparar versões")
        compare_button.clicked.connect(self.compare)
        original_button = QPushButton("Abrir gerador de log comparativo")
        original_button.clicked.connect(self.launch_comparator)
        self.save_button = QPushButton("Exportar relatório JSON")
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_report)
        actions.addWidget(analyze)
        actions.addWidget(compare_button)
        actions.addWidget(original_button)
        actions.addWidget(self.save_button)
        actions.addStretch()
        outer.addLayout(actions)
        self.summary = QLabel("Selecione um arquivo para iniciar.")
        self.summary.setWordWrap(True)
        outer.addWidget(self.summary)
        self.tabs = QTabWidget()
        self.objects = QTableWidget(0, 3)
        self.objects.setHorizontalHeaderLabels(("Caminho", "Classe", "Nome"))
        self.objects.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.objects.setColumnWidth(1, 160)
        self.objects.setColumnWidth(2, 160)
        self.links = QTableWidget(0, 3)
        self.links.setHorizontalHeaderLabels(("Objeto", "Propriedade", "Valor original"))
        self.links.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.links.setColumnWidth(1, 150)
        self.links.setColumnWidth(2, 250)
        self.findings = result_box()
        self.comparison = result_box()
        self.tabs.addTab(self.objects, "Objetos")
        self.tabs.addTab(self.links, "Propriedades")
        self.tabs.addTab(self.findings, "Achados e limites")
        self.tabs.addTab(self.comparison, "Comparação")
        outer.addWidget(self.tabs, 1)

    @staticmethod
    def _fill_table(table: QTableWidget, rows: list[dict], keys: tuple[str, ...]) -> None:
        limit = min(len(rows), 1000)
        table.setRowCount(limit)
        for row_index, row in enumerate(rows[:limit]):
            for column, key in enumerate(keys):
                table.setItem(row_index, column, QTableWidgetItem(str(row.get(key, ""))))

    def analyze(self) -> None:
        path = self.file.text().strip()
        if not Path(path).is_file():
            self.host.show_error("Selecione um arquivo .prj ou .lib existente.")
            return
        self.report = None
        self.save_button.setEnabled(False)
        self.host.run_task("Inspecionando E3", partial(audit_project, path), self.render_report)

    def render_report(self, report: dict) -> None:
        self.report = report
        self.save_button.setEnabled(True)
        coverage = report["cobertura"]
        self.summary.setText(
            f"{report['arquivo']} · SHA-256 {report['sha256'][:16]}… · "
            f"{coverage['objetos']} objetos · {coverage['nos_decodificados']}/"
            f"{coverage['nos_com_dados']} nós decodificados. "
            "A tabela mostra até 1.000 linhas; a exportação contém todas."
        )
        self._fill_table(self.objects, report["objetos"], ("caminho", "classe", "nome"))
        self._fill_table(self.links, report["vinculos"], ("objeto", "propriedade", "valor"))
        self.findings.setPlainText(pretty({
            "achados": report["achados"],
            "limites": report["limites"],
            "cobertura": coverage,
        }))

    def save_report(self) -> None:
        if self.report is None:
            return
        path, _ = QFileDialog.getSaveFileName(self, "Salvar relatório E3", "", "JSON (*.json)")
        if not path:
            return
        if Path(path).exists() and QMessageBox.question(
            self, "Sobrescrever relatório?", "O arquivo já existe. Sobrescrever?"
        ) != QMessageBox.StandardButton.Yes:
            return
        Path(path).write_text(pretty(self.report) + "\n", encoding="utf-8")
        self.host.notice("Relatório E3 exportado.")

    def launch_comparator(self) -> None:
        try:
            launch_original_comparator()
            self.host.notice("Gerador de log comparativo original iniciado.")
        except Exception as exc:
            self.host.show_error(str(exc))

    def compare(self) -> None:
        before, after = self.file.text().strip(), self.compare_file.text().strip()
        if not Path(before).is_file() or not Path(after).is_file():
            self.host.show_error("Selecione dois projetos E3 para comparar.")
            return
        self.host.run_task(
            "Comparando projetos E3",
            partial(compare_projects, before, after),
            self.render_comparison,
        )

    def render_comparison(self, result: dict) -> None:
        self.report = result
        self.save_button.setEnabled(True)
        self.summary.setText(
            f"Comparação {result['antes']['arquivo']} → {result['depois']['arquivo']} · "
            f"{result['resumo']['adicionados']} adicionados · "
            f"{result['resumo']['removidos']} removidos · "
            f"{result['resumo']['propriedades_selecionadas_alteradas']} propriedades alteradas."
        )
        self.comparison.setPlainText(pretty(result))
        self.tabs.setCurrentWidget(self.comparison)


class SkillsPage(QWidget):
    def __init__(self, host: MainWindow) -> None:
        super().__init__()
        self.host = host
        self.items = []
        outer = QVBoxLayout(self)
        outer.addWidget(heading(
            "Biblioteca de skills",
            "Fluxos integrados e conhecimento adicional em SKILL.md. Arquivos importados não executam código.",
        ))
        self.search = QLineEdit()
        self.search.setPlaceholderText("Buscar skill por nome, grupo ou descrição")
        self.search.textChanged.connect(self.refresh)
        outer.addWidget(self.search)
        splitter = QSplitter()
        self.list = QListWidget()
        self.list.currentRowChanged.connect(self.select)
        self.detail = result_box()
        splitter.addWidget(self.list)
        splitter.addWidget(self.detail)
        splitter.setStretchFactor(1, 3)
        splitter.setSizes([350, 700])
        outer.addWidget(splitter, 1)
        actions = QHBoxLayout()
        add = QPushButton("Adicionar SKILL.md")
        add.setObjectName("primary")
        add.clicked.connect(self.add_skill)
        add_folder = QPushButton("Importar pasta de skills")
        add_folder.clicked.connect(self.add_collection)
        refresh = QPushButton("Atualizar catálogo")
        refresh.clicked.connect(self.refresh)
        actions.addWidget(add)
        actions.addWidget(add_folder)
        actions.addWidget(refresh)
        actions.addStretch()
        outer.addLayout(actions)
        self.refresh()

    def refresh(self, *_: object) -> None:
        term = self.search.text().casefold()
        self.items = [
            item for item in all_skills()
            if term in f"{item.title} {item.group} {item.description}".casefold()
        ]
        self.list.clear()
        self.list.addItems([f"{item.group} · {item.title}" for item in self.items])
        if self.items:
            self.list.setCurrentRow(0)
        else:
            self.detail.clear()

    def select(self, row: int) -> None:
        if 0 <= row < len(self.items):
            item = self.items[row]
            self.detail.setPlainText(
                f"{item.title}\n\n{item.description}\n\n"
                f"Grupo: {item.group}\nOrigem: {item.source}\n"
                f"Ferramenta: {item.action or 'instruções de engenharia'}\n\n"
                f"{item.instructions}"
            )

    def add_skill(self) -> None:
        path, _ = QFileDialog.getOpenFileName(self, "Importar skill", "", "SKILL.md (SKILL.md)")
        if not path:
            return
        try:
            skill = import_skill(path)
            self.refresh()
            self.host.notice(f"Skill {skill.title} adicionada.")
        except Exception as exc:
            self.host.show_error(str(exc))

    def add_collection(self) -> None:
        path = QFileDialog.getExistingDirectory(self, "Pasta de skills")
        if not path:
            return
        imported, skipped = import_skill_collection(path)
        self.refresh()
        self.detail.setPlainText(pretty({
            "importadas": [item.title for item in imported],
            "ignoradas": skipped,
        }))
        self.host.notice(f"{len(imported)} skills importadas.")


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Engineering Copilot Studio")
        self.resize(1320, 860)
        self.pool = QThreadPool.globalInstance()
        self.busy = False
        self.workers: list[TaskWorker] = []
        shell = QWidget()
        self.setCentralWidget(shell)
        row = QHBoxLayout(shell)
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(0)
        self.navigation = QListWidget()
        self.navigation.setObjectName("navigation")
        self.navigation.setFixedWidth(230)
        self.navigation.addItems(["Início", "IEC 104", "Gateway API", "Projetos E3", "Skills"])
        self.navigation.currentRowChanged.connect(self.navigate)
        row.addWidget(self.navigation)
        self.stack = QStackedWidget()
        row.addWidget(self.stack, 1)
        self.stack.addWidget(self._home())
        self.iec_page = IECPage(self)
        self.stack.addWidget(self.iec_page)
        self.stack.addWidget(GatewayPage(self))
        self.stack.addWidget(E3Page(self))
        self.stack.addWidget(SkillsPage(self))
        self.navigation.setCurrentRow(0)
        self.statusBar().showMessage(f"Dados locais: {user_data_root()}")

    def _home(self) -> QWidget:
        page = QWidget()
        outer = QVBoxLayout(page)
        outer.setContentsMargins(26, 26, 26, 26)
        outer.addWidget(heading(
            "Engineering Copilot Studio",
            "Um espaço de trabalho para engenharia IEC 104, integração de APIs e auditoria Elipse E3.",
        ))
        for title, description, index in (
            ("IEC 104", "Analise, compare, converta e gere listas de pontos a partir de CSVs E3.", 1),
            ("Gateway API", "Desenhe e valide mapeamentos REST/JSON para endereços IEC 104.", 2),
            ("Projetos E3", "Leia .prj/.lib com hash, inventário e limites de cobertura.", 3),
            ("Skills", "Explore os fluxos integrados e adicione conhecimento em SKILL.md.", 4),
        ):
            card = QFrame()
            card.setObjectName("card")
            content = QHBoxLayout(card)
            text = QLabel(f"<b>{title}</b><br>{description}")
            text.setWordWrap(True)
            button = QPushButton("Abrir")
            button.clicked.connect(partial(self.navigation.setCurrentRow, index))
            content.addWidget(text, 1)
            content.addWidget(button)
            outer.addWidget(card)
        outer.addStretch()
        return page

    def navigate(self, index: int) -> None:
        if index >= 0:
            self.stack.setCurrentIndex(index)

    def show_error(self, message: str) -> None:
        QMessageBox.warning(self, "Atenção", message)
        self.statusBar().showMessage(message, 8000)

    def notice(self, message: str) -> None:
        self.statusBar().showMessage(message, 8000)

    def run_task(self, label: str, function: Callable[[], object], done: Callable[[object], None]) -> None:
        if self.busy:
            self.show_error("Aguarde a tarefa atual terminar.")
            return
        self.busy = True
        self.statusBar().showMessage(label + "…")
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        worker = TaskWorker(function)
        self.workers.append(worker)
        worker.signals.result.connect(done)
        worker.signals.error.connect(self.show_error)

        def finish() -> None:
            self.busy = False
            QApplication.restoreOverrideCursor()
            self.statusBar().showMessage("Pronto.", 5000)
            if worker in self.workers:
                self.workers.remove(worker)

        worker.signals.finished.connect(finish)
        self.pool.start(worker)
