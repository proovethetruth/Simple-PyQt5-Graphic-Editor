
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showMaximized()
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\Resourses/my_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #262626;")
        self.centralwidget.setGeometry(0, 41, 2500, 2500)
        self.centralwidget.adjustSize()
        
        self.ToolMenu = QtWidgets.QFrame(self.centralwidget)
        self.ToolMenu.adjustSize()
        self.ToolMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ToolMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ToolMenu.setObjectName("ToolMenu")

        self.toolButton = QtWidgets.QToolButton(self.ToolMenu)
        self.toolButton.setGeometry(QtCore.QRect(0, 0, 40, 40))
        self.toolButton.setWhatsThis("")
        self.toolButton.setAccessibleName("")
        self.toolButton.setAccessibleDescription("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\Resourses/pencil_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(40, 40))
        self.toolButton.setObjectName("toolButton")

        self.mainImage = QtWidgets.QLabel(self.centralwidget)
        self.mainImage.setGeometry(0, 41, self.centralwidget.width(), self.centralwidget.height())
        self.mainImage.setObjectName("mainImage")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")

        MainWindow.setMenuBar(self.menubar)

        self.actionCreate = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\Resourses/create_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(9)
        self.actionCreate.setFont(font)
        self.actionCreate.setObjectName("actionCreate")
        self.actionCreate.triggered.connect(self.createImage)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\Resourses/open_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.actionOpen.setFont(font)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.openImage)

        self.actionSave = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\Resourses/save_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        self.actionSave.setFont(font)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.saveImage)

        self.menuFile.addAction(self.actionCreate)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graphic Editor [Lab03]"))
        self.toolButton.setStatusTip(_translate("MainWindow", "\"Pencil\""))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionCreate.setText(_translate("MainWindow", "Create"))
        self.actionCreate.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def createImage(self):
        pixmap = QPixmap(10, 10).scaledToHeight(self.mainImage.height())
        pixmap.fill(Qt.white)
        self.mainImage.setPixmap(pixmap)

    def openImage(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        if imagePath:
            pixmap = QPixmap(imagePath).scaled(self.centralwidget.height(), self.centralwidget.width(), QtCore.Qt.KeepAspectRatio)
            self.mainImage.setPixmap(pixmap)
            self.mainImage.adjustSize()

            self.mainImage.painter = QPainter()
            self.mainImage.painter.drawPixmap(self.mainImage.rect(), self.mainImage.pixmap())
            pen = QPen(Qt.red, 3)
            self.mainImage.painter.setPen(pen)
            self.mainImage.painter.drawLine(10, 10, self.mainImage.rect().width() -10 , 10)

    def saveImage(self):
        fileName, _ = QFileDialog.getSaveFileName(self.mainImage, 'Save File', '', '*.jpg')
        if fileName:
            self.mainImage.pixmap().save(fileName)
    
    def mouseMoveEvent(self, event):
        if self.last:
            self.painter.drawLine(self.last, event.pos())

            self.last = event.pos()
            self.mainImage.setPixmap(self.mainImage.pixmap())
            self.mainImage.update()

    def mousePressEvent(self, event):
        self.last = event.pos()

    def mouseReleaseEvent(self, event):
        self.last = None

    def updateSize(self, width, height):
        pm = QPixmap(width, height)
        pm.fill(Qt.white)
        old = self.mainImage.pixmap()
        self.mainImage.setPixmap(pm)
        self.pen = QPen(Qt.black)
        self.painter = QPainter(pm)
        self.painter.drawPixmap(0,0,old)
        self.mainImage.setPixmap(pm)

    def resizeEvent(self, event):
        if event.oldSize().width() > 0:
            self.updateSize(event.size().width(), event.size().height())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()