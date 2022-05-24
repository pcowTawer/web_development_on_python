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
        self.init_rect()
        self.init_triangle()
        self.init_ui()

    def init_rect(self):
        rect_point1x = random.randint(0, 20)
        rect_point1y = random.randint(0, 20)
        rect_point2x = random_int_except(0, 20, rect_point1x, rect_point1x)
        rect_point2y = random_int_except(0, 20, rect_point1y, rect_point1y)

        if rect_point1x > rect_point2x:
            rect_point1x, rect_point2x = rect_point2x, rect_point1x
        if rect_point1y > rect_point2y:
            rect_point1y, rect_point2y = rect_point2y, rect_point1y

        coordinates_of_rectangle = [(rect_point1x, rect_point1y),
                                    (rect_point1x, rect_point2y),
                                    (rect_point2x, rect_point2y),
                                    (rect_point2x, rect_point1y)]
        self.rectangle = Polygon(coordinates_of_rectangle)

    def init_triangle(self):
        while True:
            triangle_point1x = random.randint(0, 20)
            triangle_point1y = random.randint(0, 20)
            triangle_point2x = random.randint(0, 20)
            triangle_point2y = random.randint(0, 20)
            triangle_point3x = random.randint(0, 20)
            triangle_point3y = random.randint(0, 20)

            coordinates_of_triangle = [(triangle_point1x, triangle_point1y),
                                            (triangle_point2x, triangle_point2y),
                                            (triangle_point3x, triangle_point3y)]
            self.triangle = Polygon(coordinates_of_triangle)
            if not self.triangle.is_valid:
                continue
            if self.triangle.intersection(self.rectangle) and self.triangle.touches(self.rectangle):
                break
            if not self.triangle.intersection(self.rectangle):
                break

    def init_ui(self):
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
        self.img_scale += int((self.width() - 50) < self.img_scale * 20) * (
                    int((self.width() - 50) / 20) - self.img_scale)
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
        rc = list(self.rectangle.exterior.coords)
        painter.drawRect(
                         int(x_offset + rc[0][0] * self.img_scale),

                         int(y_offset + rc[0][1] * self.img_scale),

                         int(x_offset + rc[2][0] * self.img_scale -
                                (x_offset + rc[0][0] * self.img_scale)),

                         int(y_offset + rc[1][1] * self.img_scale -
                                (y_offset + rc[0][1] * self.img_scale))
        )

        trc = list(self.triangle.exterior.coords)

        points = [
            QPoint(int(x_offset + trc[0][0] * self.img_scale),
                   int(y_offset + trc[0][1] * self.img_scale)),
            QPoint(int(x_offset + trc[1][0] * self.img_scale),
                   int(y_offset + trc[1][1] * self.img_scale)),
            QPoint(int(x_offset + trc[2][0] * self.img_scale),
                   int(y_offset + trc[2][1] * self.img_scale))
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
        result = self.rectangle.area + self.triangle.area
        return result

    def load_new_try(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(QWidget())
        self.init_rect()
        self.init_triangle()
        self.init_ui()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()


if __name__ == "__main__":
    main()
