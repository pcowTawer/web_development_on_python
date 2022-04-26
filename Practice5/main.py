from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPolygon
from PyQt5.QtCore import QPoint
import random


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)
        self.title = "PyQt5 Drawing Tutorial"
        self.top = 150
        self.left = 150
        self.width = 500
        self.height = 500
        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.black)
        painter.setBrush(Qt.white)
        for i in range(21):
            painter.drawLine(200, i * 10, 0, i * 10)
            painter.drawLine(i * 10, 200, i * 10, 0)

        point1x = random.randint(0, 20) * 10
        point1y = random.randint(0, 20) * 10
        point2x = random.randint(0, 20) * 10
        point2y = random.randint(0, 20) * 10

        painter.setPen(QPen(Qt.black, 1, Qt.DotLine))
        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        painter.drawRect(point1x, point1y, point2x - point1x, point2y - point1y)

        point1x = random.randint(0, 20) * 10
        point1y = random.randint(0, 20) * 10
        point2x = random.randint(0, 20) * 10
        point2y = random.randint(0, 20) * 10
        point3x = random.randint(0, 20) * 10
        point3y = random.randint(0, 20) * 10

        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        points = [
            QPoint(point1x, point1y),
            QPoint(point2x, point2y),
            QPoint(point3x, point3y)
        ]
        poly = QPolygon(points)
        painter.drawPolygon(poly)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
