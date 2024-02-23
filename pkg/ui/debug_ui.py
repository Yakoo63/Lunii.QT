import logging

from PySide6.QtCore import (QSize, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QAbstractButton, QDialogButtonBox,
                               QVBoxLayout, QHBoxLayout, QWidget, QComboBox, QLineEdit,
                               QPlainTextEdit, QFileDialog, QSpacerItem, QSizePolicy)

LUNII_LOGGER = "lunii-qt"


def filter_log(log, filter):
    if filter:
        log_lines = log.splitlines()
        left_lines = [line for line in log_lines if filter.lower() in line.lower()]
        left_log = "\n".join(left_lines)
        pass
    else:
        left_log = log
    return left_log

class QTextEditHandler(logging.Handler):
    def __init__(self, text_edit):
        super(QTextEditHandler, self).__init__()
        self.text_edit = text_edit
        self.text_edit.full_log = ""
        self.text_edit.filter = ""

    def emit(self, record):
        msg = self.format(record)

        # saving in internal buffer
        self.text_edit.full_log += msg + "\n"
        # filtering
        log = filter_log(self.text_edit.full_log, self.text_edit.filter)
        # showing
        self.text_edit.setPlainText(log)

        # moving vertical scrollbar to bottom
        v_sb = self.text_edit.verticalScrollBar()
        v_sb.setValue(v_sb.maximum())

        # moving horizontal scrollbar to left
        h_sb = self.text_edit.horizontalScrollBar()
        h_sb.setValue(h_sb.minimum())

class DebugDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.logger = logging.getLogger(LUNII_LOGGER)
        self.logger.setLevel(logging.DEBUG)

        # window config
        self.setWindowTitle("Debug Log")
        icon = QIcon()
        icon.addFile(u":/icon/res/debug_log.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.setMinimumSize(QSize(500, 0))
        self.resize(500, 300)

        # contents
        self.cb_level = QComboBox(self)
        self.le_filter = QLineEdit(self)
        self.le_filter.setClearButtonEnabled(True)
        self.le_filter.setPlaceholderText("(Log filter text)")
        self.le_filter.setToolTip("Try \"error\" or \"fail\".")

        horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        upper_layout = QHBoxLayout()
        upper_layout.addWidget(self.cb_level)
        upper_layout.addItem(horizontalSpacer)
        upper_layout.addWidget(self.le_filter)

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.te_Logger = QPlainTextEdit(self)
        self.te_Logger.setObjectName(u"textEdit")
        self.te_Logger.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.te_Logger.setReadOnly(True)
        self.te_Logger.setPlaceholderText("Application Log Empty ...")

        # adding contents to vertical layout
        self.verticalLayout.addLayout(upper_layout)
        self.verticalLayout.addWidget(self.te_Logger)

        # buttons at bottom
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close |
                                          QDialogButtonBox.Reset |
                                          QDialogButtonBox.Save)
        # callbacks on buttons
        self.buttonBox.clicked.connect(self.button_clicked)

        self.verticalLayout.addWidget(self.buttonBox)

        # next UI inits
        self.init_ui()

    def init_ui(self):
        self.modify_widgets()
        self.setup_connections()

    def modify_widgets(self):
        self.cb_level.setVisible(True)
        self.cb_level.addItem("NONE")
        self.cb_level.addItem("DEBUG")
        self.cb_level.addItem("INFO")
        self.cb_level.addItem("WARNING")
        self.cb_level.addItem("ERROR")

        self.cb_level.setCurrentIndex(2)
        self.logger.setLevel(logging.INFO)

        self.le_filter.setVisible(True)

    def setup_connections(self):
        # log level selector
        self.cb_level.currentIndexChanged.connect(self.cb_level_selected)

        # text filter
        self.le_filter.textChanged.connect(self.log_update)

        # connecting logger handler
        handler = QTextEditHandler(self.te_Logger)
        handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
        self.logger.addHandler(handler)

    def cb_level_selected(self):
        # getting current device
        dict_level = {"NONE": logging.NOTSET,
                      "DEBUG": logging.DEBUG,
                      "INFO": logging.INFO,
                      "WARNING": logging.WARNING,
                      "ERROR": logging.ERROR}

        level = self.cb_level.currentText()
        self.logger.setLevel(dict_level[level])

    def log_update(self):
        # getting filter text
        self.te_Logger.filter = self.le_filter.text()

        # filtering
        left_log = filter_log(self.te_Logger.full_log, self.te_Logger.filter)

        # showing log
        self.te_Logger.clear()
        self.te_Logger.setPlainText(left_log)

        # moving vertical scrollbar to bottom
        v_sb = self.te_Logger.verticalScrollBar()
        v_sb.setValue(v_sb.maximum())

    def button_clicked(self, button: QAbstractButton):
        button_role = self.sender().buttonRole(button)

        if button_role == QDialogButtonBox.RejectRole:
            self.hide()
        elif button_role == QDialogButtonBox.ResetRole:
            self.te_Logger.clear()
        elif button_role == QDialogButtonBox.AcceptRole:
            self.save_log()

    def save_log(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Log", "", "Text Files (*.txt);;All Files (*)")
        if filename:
            with open(filename, 'wb') as file:
                file.write(self.te_Logger.full_log.encode('utf-8'))
