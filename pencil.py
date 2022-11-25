
# import time

# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
# QPushButton, QTableWidget, QWidget, QRadioButton, QTableWidgetItem)
# from PyQt5.QtGui import QIcon, QPixmap

# def get_num(a1, k, n):
#     if n == 1:
#         return a1
#     else:
#         return get_num(a1, k, n - 1) * k


# app = QApplication([])
# app.setApplicationName("Lab03 (3rd year)")
# app.setWindowIcon(QIcon('C:\\Users\\asus\\Desktop\\Projects\\SUAI\\Labs\\3-ий курс\\C++\\Lab02 Python\\plex.jpg'))
# window = QWidget()
# window.setGeometry(100, 100, 1200, 600)

# label = QLabel(window)
# # pixmap = QPixmap('something.jpg').scaledToHeight(500)
# # label.setPixmap(pixmap)

# j = 500

# pixmap = QPixmap('something.jpg').scaledToHeight(j)
# label.setPixmap(pixmap)
# j += 1
# time.sleep(5)

# window.resize(pixmap.width(),pixmap.height())
# window.show()

# app.exec_()