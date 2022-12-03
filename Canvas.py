
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QColor, QPainter, QPixmap
from PyQt5.QtCore import Qt, QSize

import random

SPRAY_PARTICLES = 100
SPRAY_DIAMETER = 10

class Canvas(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)

        self.painter, self.p = None, None
        self.penSize = 4

        self.pmRect = None
        self.last_x, self.last_y = None, None
        self.pen_color = QColor('#000000')
        self.currentTool = "pen"

    def set_pen_color(self, c):
        self.pen_color = QColor(c)

    def mouseMoveEvent(self, e):
        self.p.setColor(self.pen_color)
        self.painter.setPen(self.p)

        if self.currentTool == "pen":
            if self.last_x is None:
                self.last_x = e.x()
                self.last_y = e.y()
                return

            self.p.setWidth(self.penSize)
            # painter.translate(-self.pmRect.topLeft())
            self.painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
            # self.painter.end()
            self.update()

            self.last_x = e.x()
            self.last_y = e.y()

        elif self.currentTool == "spray":
            self.p.setWidth(self.penSize // 2)
            # p = painter.pen()
            # painter.translate(-self.pmRect.topLeft())
            for n in range(SPRAY_PARTICLES):
                xo = random.gauss(0, SPRAY_DIAMETER * self.penSize * 0.5)
                yo = random.gauss(0, SPRAY_DIAMETER * self.penSize * 0.5)
                self.painter.drawPoint(int(e.x() + xo), int(e.y() + yo))

            self.update()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def changePenSize(self, value):
        self.penSize = value

    def pickPen(self):
        self.currentTool = "pen"

    def pickSpray(self):
        self.currentTool = "spray"

    def setPixmap(self, a0: QPixmap):
        super().setPixmap(a0)
        rect = self.contentsRect()
        self.pmRect = self.pixmap().rect()
        if rect != self.pmRect:
            align = self.alignment()
            if align & Qt.AlignHCenter:
                self.pmRect.moveLeft((rect.width() - self.pmRect.width()) // 2)
            elif align & Qt.AlignRight:
                self.pmRect.moveRight(rect.right())
            if align & Qt.AlignVCenter:
                self.pmRect.moveTop((rect.height() - self.pmRect.height()) // 2)
            elif align &  Qt.AlignBottom:
                self.pmRect.moveBottom(rect.bottom())

        self.painter = QPainter(self.pixmap())
        self.p = self.painter.pen()
        self.p.setWidth(4)
        self.p.setColor(self.pen_color)
        self.painter.setPen(self.p)
        self.painter.translate(-self.pmRect.topLeft())
        self.update()

COLORS = [
# 17 undertones https://lospec.com/palette-list/17undertones
'#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
'#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
'#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
]


class QPaletteButton(QPushButton):
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QSize(24,24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)