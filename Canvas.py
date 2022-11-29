
from PyQt5.QtWidgets import QLabel, QPushButton, QSizePolicy
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import QSize

import random, time

SPRAY_PARTICLES = 100
SPRAY_DIAMETER = 10

class Canvas(QLabel):
    def __init__(self):
        super().__init__()
        self.last_x, self.last_y = None, None
        self.pen_color = QColor('#000000')
        self.currentTool = "pen"

    def set_pen_color(self, c):
        self.pen_color = QColor(c)

    def mouseMoveEvent(self, e):
        if self.currentTool == "pen":
            if self.last_x is None:
                self.last_x = e.x()
                self.last_y = e.y()
                return

            painter = QPainter(self.pixmap())
            p = painter.pen()
            p.setWidth(4)
            p.setColor(self.pen_color)
            painter.setPen(p)
            painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
            painter.end()
            self.update()

            self.last_x = e.x()
            self.last_y = e.y()

        elif self.currentTool == "spray":
            painter = QPainter(self.pixmap())
            p = painter.pen()
            p.setWidth(1)
            p.setColor(self.pen_color)
            painter.setPen(p)
            for n in range(SPRAY_PARTICLES):
                xo = random.gauss(0, SPRAY_DIAMETER)
                yo = random.gauss(0, SPRAY_DIAMETER)
                painter.drawPoint(int(e.x() + xo), int(e.y() + yo))

            self.update()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def pickPen(self):
        self.currentTool = "pen"

    def pickSpray(self):
        self.currentTool = "spray"

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