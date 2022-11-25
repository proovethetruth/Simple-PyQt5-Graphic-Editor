
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog, QLineEdit, QDialogButtonBox, QFormLayout


class InputDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Create Image")
        self.setWindowFlags(Qt.WindowTitleHint)

        icon2 = QIcon()
        icon2.addPixmap(QPixmap(".\\Resourses/create_icon.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon2)

        self.first = QLineEdit(self)
        self.second = QLineEdit(self)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        layout = QFormLayout(self)
        layout.addRow("Width", self.first)
        layout.addRow("Height", self.second)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.validation)
        buttonBox.rejected.connect(self.reject)

    def validation(self):
        if (len(self.first.text()) and len(self.second.text())) != 0:
            self.accept()

    def getInputs(self):
        width = int(self.first.text())
        height = int(self.second.text())
        return (width, height)
