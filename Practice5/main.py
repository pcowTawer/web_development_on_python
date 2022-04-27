import random
import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton)
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPixmap, QPen, QBrush, QPainter, QPolygon

variants = [
    "C:\\Users\\PCOW\\Pictures\\Logo.png",
    "C:\\Users\\PCOW\\Pictures\\Подпись.png"
]


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(0, 0, 500, 400)
        self.setWindowTitle("Test")
        self.initUI(random.choice(variants))

    def initUI(self, image_path="C:\\Users\\PCOW\\Pictures\\Logo.png"):

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

        self.label_txt1 = QLabel("Введите площадь фигуры")
        font = self.label_txt1.font()
        font.setPointSize(30)
        self.label_txt1.setFont(font)
        self.label_txt1.setMaximumHeight(80)
        self.label_txt1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.label_img = QLabel()
        self.label_img.setFixedSize(300, 300)
        self.label_img.setScaledContents(True)
        self.label_img.setPixmap(QPixmap(image_path))

        self.line_edit_widget = QLineEdit()
        self.line_edit_widget.setMaxLength(10)
        self.line_edit_widget.setPlaceholderText("Enter your text")
        self.line_edit_widget.returnPressed.connect(self.check_the_answer)

        self.button_next = QPushButton("Следующее")
        self.button_next.setMaximumSize(100, 50)
        self.button_next.setCheckable(True)
        self.button_next.clicked.connect(self.load_new_try)


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_txt1)
        self.layout.addWidget(self.label_img, alignment=(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter))
        self.layout.addWidget(self.line_edit_widget)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.GlobalColor.black)
        painter.setBrush(Qt.GlobalColor.black)
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

    def check_the_answer(self):
        self.line_edit_widget.setDisabled(True)
        try:
            user_s = float(self.line_edit_widget.text())
        except ValueError:
            self.layout.addWidget(QLabel("Введено невозможное значение"))
            self.layout.addWidget(self.button_next)
            return

        if user_s == 50.1:
            self.layout.addWidget(QLabel("Верно"))
        else:
            self.layout.addWidget(QLabel("Неверно"))
        self.layout.addWidget(self.button_next)

    def load_new_try(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(QWidget())
        self.initUI(random.choice(variants))


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()