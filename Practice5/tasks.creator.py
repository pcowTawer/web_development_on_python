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
        self.title = "PyQt5 Drawing Tutorial"
        self.setMinimumSize(205, 205)
        self.Kpoint1x = random.randint(0, 20) * 10
        self.Kpoint1y = random.randint(0, 20) * 10
        self.Kpoint2x = random.randint(0, 20) * 10
        self.Kpoint2y = random.randint(0, 20) * 10

        self.Tpoint1x = random.randint(0, 20) * 10
        self.Tpoint1y = random.randint(0, 20) * 10
        self.Tpoint2x = random.randint(0, 20) * 10
        self.Tpoint2y = random.randint(0, 20) * 10
        self.Tpoint3x = random.randint(0, 20) * 10
        self.Tpoint3y = random.randint(0, 20) * 10
        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.black)
        painter.setBrush(Qt.black)
        for i in range(21):
            painter.drawLine(200, i * 10, 0, i * 10)
            painter.drawLine(i * 10, 200, i * 10, 0)

        painter.drawRect(self.Kpoint1x, self.Kpoint1y, self.Kpoint2x - self.Kpoint1x, self.Kpoint2y - self.Kpoint1y)

        points = [
            QPoint(self.Tpoint1x, self.Tpoint1y),
            QPoint(self.Tpoint2x, self.Tpoint2y),
            QPoint(self.Tpoint3x, self.Tpoint3y)
        ]
        poly = QPolygon(points)
        painter.drawPolygon(poly)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

