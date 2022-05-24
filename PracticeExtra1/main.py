import random
import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget)
from PyQt6.QtCore import Qt, QPoint, QRect, QSize
from PyQt6.QtGui import QPainter


def is_touches(field, x, y):
    if x >= 10 or y >= 10 or x < 0 or y < 0:
        return None
    result = 0
    x1 = x - 1
    x2 = x + 1
    y1 = y - 1
    y2 = y + 1
    if y + 1 >= 10:
        y2 = y
    if y - 1 < 0:
        y1 = y
    if x + 1 >= 10:
        x2 = x
    if x - 1 < 0:
        x1 = x
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            result += field[i][j]
    return bool(result)


def is_filled(field):
    for i in range(0, 10):
        for j in range(0, 10):
            if not is_touches(field, i, j):
                return False
    return True


def generate_ship(field, ship_length):
    flag = True
    x: int
    y: int
    x1: int
    y1: int
    ship_length -= 1

    while True:
        variants = []
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        while (is_touches(field, x, y) is None) or is_touches(field, x, y):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        if (not is_touches(field, x + ship_length, y)) and (not (is_touches(field, x + ship_length, y) is None)):
            variants.append(0)
        if (not is_touches(field, x, y + ship_length)) and (not (is_touches(field, x, y + ship_length) is None)):
            variants.append(1)
        if (not is_touches(field, x - ship_length, y)) and (not (is_touches(field, x - ship_length, y) is None)):
            variants.append(2)
        if (not is_touches(field, x, y - ship_length)) and (not (is_touches(field, x, y - ship_length) is None)):
            variants.append(3)
        if variants.__len__() > 0:
            flag = random.choice(variants)
            if flag == 0:
                x1 = x + ship_length
                y1 = y
                break
            if flag == 1:
                x1 = x
                y1 = y + ship_length
                break
            if flag == 2:
                x1 = x - ship_length
                y1 = y
                break
            if flag == 3:
                x1 = x
                y1 = y - ship_length
                break

    if x1 < x:
        x, x1 = x1, x
    if y1 < y:
        y, y1 = y1, y
    for i in range(x, x1 + 1):
        for j in range(y, y1 + 1):
            field[i][j] = 1


def generate_field():
    field = [[0 for i in range(10)] for j in range(10)]
    generate_ship(field, 4)
    generate_ship(field, 3)
    generate_ship(field, 3)
    generate_ship(field, 2)
    generate_ship(field, 2)
    generate_ship(field, 2)
    generate_ship(field, 1)
    generate_ship(field, 1)
    generate_ship(field, 1)
    generate_ship(field, 1)
    return field


def print_field(field):
    for i in range(10):
        for j in range(10):
            if field[i][j]:
                print("\033[30m{}".format(field[i][j]), end='  ')
            else:
                print("\033[36m{}".format(field[i][j]), end='  ')
        print()


def print_fields(field1, field2):
    for i in range(63):
        print("\033[31m{}".format("_"), end='')
    print()
    for i in range(10):
        print("\033[31m{}".format("|"), end='')
        for j in range(10):
            if field1[i][j]:
                print("\033[30m{}".format(field1[i][j]), end='  ')
            else:
                print("\033[36m{}".format(field1[i][j]), end='  ')
        print("\033[31m{}".format("|"), end='')
        for j in range(10):
            if field2[i][j]:
                print("\033[30m{}".format(field2[i][j]), end='  ')
            else:
                print("\033[36m{}".format(field2[i][j]), end='  ')

        print("\033[31m{}".format("|"))
    for i in range(63):
        print("\033[31m{}".format("_"), end='')


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(0, 0, 700, 700)
        self.setWindowTitle("Test")
        self.field = generate_field()
        self.init_ui()

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

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label_txt1)
        self.layout.addWidget(self.label_img, alignment=(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter))

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        self.show()

    def paintEvent(self, event):
        self.img_scale = int((self.height() - self.label_txt1.height() - 50) / 10)
        self.img_scale += int((self.width() - 50) < self.img_scale * 10) * (
                    int((self.width() - 50) / 10) - self.img_scale)

        x_offset = int(0.5 * self.width() - 5 * self.img_scale)
        y_offset = 70
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.GlobalColor.black)
        painter.setBrush(Qt.GlobalColor.black)
        for i in range(11):
            painter.drawLine(x_offset + 10 * self.img_scale,
                             y_offset + i * self.img_scale,
                             x_offset,
                             y_offset + i * self.img_scale)
            painter.drawLine(x_offset + i * self.img_scale,
                             y_offset + 10 * self.img_scale,
                             x_offset + i * self.img_scale,
                             y_offset)
        for i in range(10):
            for j in range(10):
                if self.field[i][j] == 1:
                    painter.drawRect(x_offset + i * self.img_scale,
                                     y_offset + j * self.img_scale,
                                     self.img_scale, self.img_scale)


def main():
    field1 = generate_field()
    field2 = generate_field()
    print_fields(field1, field2)


if __name__ == "__main__":
    main()
