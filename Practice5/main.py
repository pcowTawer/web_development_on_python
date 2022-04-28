import random
import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton)
from PyQt6.QtCore import Qt, QPoint, QRect, QSize
from PyQt6.QtGui import QPainter, QPolygon
from shapely.geometry import Polygon


def random_int_except(a, b, c, d):
    number = random.randint(a, b)
    while c <= number <= d:
        number = random.randint(a, b)
    return number


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(0, 0, 700, 700)
        self.setWindowTitle("Test")
        self.init_ui()

    def init_ui(self):
        self.Rect_point1x = random.randint(0, 20)
        self.Rect_point1y = random.randint(0, 20)
        self.Rect_point2x = random_int_except(0, 20, self.Rect_point1x, self.Rect_point1x)
        self.Rect_point2y = random_int_except(0, 20, self.Rect_point1y, self.Rect_point1y)

        if self.Rect_point1x > self.Rect_point2x:
            self.Rect_point1x, self.Rect_point2x = self.Rect_point2x, self.Rect_point1x
        if self.Rect_point1y > self.Rect_point2y:
            self.Rect_point1y, self.Rect_point2y = self.Rect_point2y, self.Rect_point1y

        self.coordinates_of_rectangle = [(self.Rect_point1x, self.Rect_point1y),
                                         (self.Rect_point1x, self.Rect_point2y),
                                         (self.Rect_point2x, self.Rect_point2y),
                                         (self.Rect_point2x, self.Rect_point1y)]

        self.rectangle = Polygon(self.coordinates_of_rectangle)

        while True:

            self.Triangle_point1x = random.randint(0, 20)
            self.Triangle_point1y = random.randint(0, 20)
            self.Triangle_point2x = random.randint(0, 20)
            self.Triangle_point2y = random.randint(0, 20)
            self.Triangle_point3x = random.randint(0, 20)
            self.Triangle_point3y = random.randint(0, 20)

            self.coordinates_of_triangle = [(self.Triangle_point1x, self.Triangle_point1y),
                                            (self.Triangle_point2x, self.Triangle_point2y),
                                            (self.Triangle_point3x, self.Triangle_point3y)]

            self.triangle = Polygon(self.coordinates_of_triangle)

            length1 = ((self.Triangle_point1x - self.Triangle_point2x)**2 +
                       (self.Triangle_point1y - self.Triangle_point2y)**2)**0.5
            length2 = ((self.Triangle_point2x - self.Triangle_point3x)**2 +
                       (self.Triangle_point2y - self.Triangle_point3y)**2)**0.5
            length3 = ((self.Triangle_point3x - self.Triangle_point1x)**2 +
                       (self.Triangle_point3y - self.Triangle_point1y)**2)**0.5
            if self.triangle.intersection(self.rectangle) and self.triangle.touches(self.rectangle):
                break
            if not self.triangle.intersection(self.rectangle) \
                    and length3 < length2 + length1 \
                    and length2 < length3 + length1 \
                    and length1 < length3 + length2:
                break

        self.label_txt1 = QLabel("Найдите площадь фигур(ы)")
        font = self.label_txt1.font()
        font.setPointSize(30)
        self.label_txt1.setFont(font)
        self.label_txt1.setMaximumHeight(50)
        self.label_txt1.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        self.label_img = QLabel()
        self.label_img.setFixedSize(QSize(200, 220))
        self.label_img.setScaledContents(True)
        self.label_img.setFrameRect(QRect(QPoint(100, 100), QSize(400, 400)))

        self.line_edit_widget = QLineEdit()
        self.line_edit_widget.setMaximumHeight(20)
        self.line_edit_widget.setMaxLength(10)
        self.line_edit_widget.setPlaceholderText("Enter your text")
        self.line_edit_widget.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.line_edit_widget.returnPressed.connect(self.check_the_answer)

        self.label_result = QLabel()
        self.label_result.setMaximumHeight(20)
        self.label_result.setAlignment(Qt.AlignmentFlag.AlignBottom)

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
        print(self.calculate_square())
        self.show()

    def paintEvent(self, event):
        self.img_scale = int((self.height() - self.label_txt1.height() - self.line_edit_widget.height() -
                              self.label_result.height() - self.button_next.height() - 50) / 20)
        x_offset = int(0.5 * self.width() - 10 * self.img_scale)
        y_offset = 70
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.GlobalColor.black)
        painter.setBrush(Qt.GlobalColor.black)
        for i in range(21):
            painter.drawLine(x_offset + 20 * self.img_scale,
                             y_offset + i * self.img_scale,
                             x_offset,
                             y_offset + i * self.img_scale)
            painter.drawLine(x_offset + i * self.img_scale,
                             y_offset + 20 * self.img_scale,
                             x_offset + i * self.img_scale,
                             y_offset)

        painter.drawRect(x_offset + self.Rect_point1x * self.img_scale,
                         y_offset + self.Rect_point1y * self.img_scale,
                         x_offset + self.Rect_point2x * self.img_scale -
                         (x_offset + self.Rect_point1x * self.img_scale),
                         y_offset + self.Rect_point2y * self.img_scale -
                         (y_offset + self.Rect_point1y * self.img_scale))

        points = [
            QPoint(x_offset + self.Triangle_point1x * self.img_scale,
                   y_offset + self.Triangle_point1y * self.img_scale),
            QPoint(x_offset + self.Triangle_point2x * self.img_scale,
                   y_offset + self.Triangle_point2y * self.img_scale),
            QPoint(x_offset + self.Triangle_point3x * self.img_scale,
                   y_offset + self.Triangle_point3y * self.img_scale)
        ]
        poly = QPolygon(points)
        painter.drawPolygon(poly)

    def check_the_answer(self):
        self.line_edit_widget.setDisabled(True)
        try:
            user_square = float(self.line_edit_widget.text())
        except ValueError:
            self.label_result.setText("Введено невозможное значение")
            self.layout.addWidget(self.label_result)
            self.layout.addWidget(self.button_next)
            return
        if user_square == self.calculate_square():
            self.label_result.setText("Верно!")
        else:
            self.label_result.setText("Неверно!")

        self.layout.addWidget(self.label_result)
        self.layout.addWidget(self.button_next)

    def calculate_square(self):
        result = abs(self.Rect_point1x - self.Rect_point2x) * abs(self.Rect_point2y - self.Rect_point1y) + \
               0.5*abs((self.Triangle_point2x - self.Triangle_point1x) *
                       (self.Triangle_point3y - self.Triangle_point1y) -
                       (self.Triangle_point3x - self.Triangle_point1x) *
                       (self.Triangle_point2y - self.Triangle_point1y))
        return result

    def load_new_try(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(QWidget())
        self.init_ui()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()


if __name__ == "__main__":
    main()
