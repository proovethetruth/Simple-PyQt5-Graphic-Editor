from Canvas import *
from InputDialog import *

import sys

from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QToolButton, 
QMenuBar, QMenu, QAction, QFileDialog, QHBoxLayout, QVBoxLayout, QSpinBox, QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt, QSize, QMetaObject, QCoreApplication

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        font = QFont()
        font.setFamily("Gill Sans MT")
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addPixmap(QPixmap(".\\Resourses/my_icon.jpg"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)

        self.mainImage = Canvas()
        self.mainImage.setObjectName("mainImage")

        self.menuWidget = QWidget()
        shadow = QGraphicsDropShadowEffect()
        shadow.setOffset(0, 5)
        shadow.setBlurRadius(20)
        self.menuWidget.setGraphicsEffect(shadow)
        self.menuWidget.setStyleSheet("background-color: #555555")
        self.menuWidget.setMaximumSize(5000, 100)
        self.menuWidget.setContentsMargins(10, 0, 0, 0)

        self.toolMenu = QHBoxLayout(self.menuWidget)
        self.toolMenu.setContentsMargins(0, 0, 0, 0)

        self.pencilTool = QToolButton()
        self.pencilTool.setStyleSheet("background-color: #888888")
        pencilIcon = QIcon()
        pencilIcon.addPixmap(QPixmap(".\\Resourses/pencil_icon.png"), QIcon.Normal, QIcon.Off)
        self.pencilTool.setIcon(pencilIcon)
        self.pencilTool.setIconSize(QSize(60, 60))
        self.pencilTool.setObjectName("pencilTool")
        self.pencilTool.clicked.connect(lambda: self.mainImage.pickPen())

        self.sprayTool = QToolButton()
        self.sprayTool.setStyleSheet("background-color: #888888")
        sprayIcon = QIcon()
        sprayIcon.addPixmap(QPixmap(".\\Resourses/spray_icon.png"), QIcon.Normal, QIcon.Off)
        self.sprayTool.setIcon(sprayIcon)
        self.sprayTool.setIconSize(QSize(60, 60))
        self.sprayTool.setObjectName("sprayTool")
        self.sprayTool.clicked.connect(lambda: self.mainImage.pickSpray())

        self.sizeLabel = QLabel("   Pen size: ")
        self.sizeLabel.setFont(QFont("Gill Sans MT", 14))
        self.sizeLabel.setStyleSheet("color: white")

        self.penSizeButton = QSpinBox()
        self.penSizeButton.setStyleSheet("padding: 5; color: white; background-color: #333333; font-size: 15px;")
        self.penSizeButton.setValue(4)
        self.penSizeButton.setMinimum(1)
        self.penSizeButton.setMaximum(50)
        self.penSizeButton.valueChanged.connect(lambda: self.mainImage.changePenSize(self.penSizeButton.value()))

        self.toolMenu.addWidget(self.pencilTool)
        self.toolMenu.addWidget(self.sprayTool)
        self.toolMenu.addWidget(self.sizeLabel)
        self.toolMenu.addWidget(self.penSizeButton)

        self.toolMenu.addStretch()

        self.palette = QHBoxLayout()
        self.palette.addStretch()
        self.add_palette_buttons(self.palette)
        self.palette.addStretch()

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")

        self.menuFile = QMenu(self.menubar)
        font = QFont()
        font.setFamily("Gill Sans MT")
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")

        MainWindow.setMenuBar(self.menubar)

        self.actionCreate = QAction(MainWindow)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(".\\Resourses/create_icon.png"), QIcon.Normal, QIcon.Off)
        self.actionCreate.setIcon(icon2)
        font = QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(9)
        self.actionCreate.setFont(font)
        self.actionCreate.setObjectName("actionCreate")
        self.actionCreate.triggered.connect(self.createImage)

        self.actionOpen = QAction(MainWindow)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(".\\Resourses/open_icon.png"), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon3)
        font = QFont()
        font.setFamily("Gill Sans MT")
        self.actionOpen.setFont(font)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.openImage)

        self.actionSave = QAction(MainWindow)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(".\\Resourses/save_icon.png"), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon4)
        font = QFont()
        font.setFamily("Gill Sans MT")
        self.actionSave.setFont(font)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.saveImage)

        self.menuFile.addAction(self.actionCreate)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 25)
        self.mainLayout.setSpacing(10)

        self.mainLayout.addWidget(self.menuWidget)
        
        self.mainLayout.addWidget(self.mainImage)

        self.palette.setSpacing(0)
        self.mainLayout.addLayout(self.palette)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setLayout(self.mainLayout)
        self.centralwidget.setStyleSheet("background-color: #262626;")

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.resize(800,600)
        MainWindow.showMaximized()
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graphic Editor [Lab03]"))
        self.pencilTool.setStatusTip(_translate("MainWindow", "\"Pencil\""))
        self.pencilTool.setText(_translate("MainWindow", "..."))
        # self.sprayTool.setStatusTip(_translate("MainWindow", "\"Spray\""))
        # self.sprayTool.setText(_translate("MainWindow", "..."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionCreate.setText(_translate("MainWindow", "Create"))
        self.actionCreate.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def createImage(self):
        dialog = InputDialog()
        if dialog.exec():
            pixmap = QPixmap(int(dialog.getInputs()[0]), int(dialog.getInputs()[1])).scaled(self.mainImage.width(), self.mainImage.height(), Qt.KeepAspectRatio)
            pixmap.fill(Qt.white)
            self.mainImage.setPixmap(pixmap)
            self.mainImage.adjustSize()

    def openImage(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        if imagePath:
            pixmap = QPixmap(imagePath).scaled(self.mainImage.width(), self.mainImage.height(), Qt.KeepAspectRatio)
            self.mainImage.setPixmap(pixmap)
            self.mainImage.adjustSize()

    def saveImage(self):
        fileName, _ = QFileDialog.getSaveFileName(self.mainImage, 'Save File', '', '*.jpg')
        if fileName:
            self.mainImage.pixmap().save(fileName)

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.mainImage.set_pen_color(c))
            layout.addWidget(b)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()