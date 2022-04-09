from string import ascii_letters
import random
import os

def get_input_int():
    while True:
        try:
            return int(input())
        except ValueError as exc:
            print("Введенная строка не является числом")

def menu() -> int:
    while True:
        print("1. Создать треугольник")
        print("2. Создать пентагон")
        print("3. Вывести все фигуры")
        print("4. Удалить треугольник")
        print("5. Удалить пентагон")
        print("6. Проверить пересечение")
        print("7. Передвинуть фигуру")
        print("8. Выход")
        buf = get_input_int()
        if (buf < 1 or buf > 8):
            print("Нет такой опции")
            input()
            os.system("cls || clear")
            continue
        os.system("cls || clear")
        return buf

def segment_intersection(x1, y1, x2, y2, x3, y3, x4, y4) -> bool:
    return (((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)) *
            ((x4 - x1) * (y2 - y1) - (y4 - y1) * (x2 - x1)) <= 0) and \
           (((x1 - x3) * (y4 - y3) - (y1 - y3) * (x4 - x3)) *
            ((x2 - x3) * (y4 - y3) - (y2 - y3) * (x4 - x3)) <= 0)

class Polygon:
    _id : str
    _coord : list
    def move(self, x, y):
        pass
    def get_id(self):
        return self._id
    def get_coord(self):
        return self._coord
    def is_intersect(self, obj1, obj2) -> bool:
        for i in range(obj1._coord.__len__() - 1, 0, -2):
            for j in range(obj2._coord.__len__() - 1, 0, -2):
                if (segment_intersection(obj1._coord[i - 1], obj1._coord[i],
                                         obj1._coord[i - 3], obj1._coord[i - 2],
                                         obj2._coord[j - 1], obj2._coord[j],
                                         obj2._coord[j - 3], obj2._coord[j - 2])):
                    return bool(1)
        return bool(0)

class Triangle(Polygon):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self._coord = [x1, y1, x2, y2, x3, y3]
        self._id = ''.join(random.choice(ascii_letters) for i in range(12))
    def move(self, x, y):
        for i in range(0,6,2):
            self._coord[i] += x
            self._coord[i + 1] += y
    def __del__(self):
        pass

class Pentagon(Polygon):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
        self._coord = [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5]
        self._id = ''.join(random.choice(ascii_letters) for i in range(12))
    def move(self, x, y):
        for i in range(0, 9, 2):
            self._coord[i] += x
            self._coord[i + 1] += y
    def __del__(self):
        pass

class Factory:
    def create_triangle(self, x1, y1, x2, y2, x3, y3) -> Triangle:
        return Triangle(x1, y1, x2, y2, x3, y3)
    def create_pentagon(self, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5) -> Pentagon:
        return Pentagon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5)
    def delete_triangle(self, triangle : Triangle):
        triangle.__del__()
    def delete_pentagon(self, pentagon : Pentagon):
        pentagon.__del__()

def main():

    list_of_triangles = []
    list_of_pentagones = []
    list_of_polygones = []
    factory = Factory()
    while True:
        os.system("cls || clear")
        flag = menu()
        if (flag == 1):
            os.system("cls || clear")
            print("Введите координаты вершин треуголника")
            print("Порядок x1, y1, x2, y2, x3, y3")
            x1 = get_input_int()
            y1 = get_input_int()
            x2 = get_input_int()
            y2 = get_input_int()
            x3 = get_input_int()
            y3 = get_input_int()
            list_of_triangles.append(factory.create_triangle(x1, y1, x2, y2, x3, y3))
            print('Создан треугольник с индексом {a}'.format(a=list_of_triangles[list_of_triangles.__len__() - 1].get_id()))
            print("Координаты: {coord}".format(coord=list_of_triangles[list_of_triangles.__len__() - 1].get_coord()))
            input()
            os.system("cls || clear")
        if (flag == 2):
            os.system("cls || clear")
            print("Введите координаты вершин пентагона")
            print("Порядок x1, y1, x2, y2, x3, y3, x4, y4, x5, y5")
            x1 = get_input_int()
            y1 = get_input_int()
            x2 = get_input_int()
            y2 = get_input_int()
            x3 = get_input_int()
            y3 = get_input_int()
            x4 = get_input_int()
            y4 = get_input_int()
            x5 = get_input_int()
            y5 = get_input_int()
            list_of_pentagones.append(factory.create_pentagon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5))
            print('Создан пентагон с индексом {a}'.format(
                a=list_of_pentagones[list_of_pentagones.__len__() - 1].get_id()))
            print("Координаты: {coord}".format(
                coord=list_of_pentagones[list_of_pentagones.__len__() - 1].get_coord()))
            input()
            os.system("cls || clear")
        if (flag == 3):
            os.system("cls || clear")
            print("Пентагоны:")
            for i in list_of_pentagones:
                print(i.get_id())
                print(i.get_coord())
            print("Треугольники:")
            for i in list_of_triangles:
                print(i.get_id())
                print(i.get_coord())
            input()
            os.system("cls || clear")
        if (flag == 4):
            os.system("cls || clear")
            if(list_of_triangles.__len__() == 0):
                print("Треугольников нет!")
                input()
                continue
            while True:
                print("Треугольники:")
                index = 1
                for i in list_of_triangles:
                    print(index, end=") ")
                    print(i.get_id())
                    print(i.get_coord())
                    index += 1
                print("Введите номер треугольника который вы хотите удалить")
                index = get_input_int()
                if (index < 1 or index > list_of_triangles.__len__()):
                    print("Нет такой опции")
                    input()
                    os.system("cls || clear")
                    continue
                factory.delete_triangle(list_of_triangles[index - 1])
                list_of_triangles.pop(index - 1)
                break
        if (flag == 5):
            os.system("cls || clear")
            if (list_of_pentagones.__len__() == 0):
                print("Пентагонов нет!")
                input()
                continue
            while True:
                print("Пентагоны:")
                index = 1
                for i in list_of_pentagones:
                    print(index, end=") ")
                    print(i.get_id())
                    print(i.get_coord())
                    index += 1
                print("Введите номер пентагона который вы хотите удалить")
                buf = get_input_int()
                if (buf < 1 or buf > list_of_pentagones.__len__()):
                    print("Нет такой опции")
                    input()
                    os.system("cls || clear")
                    continue
                index = buf - 1
                factory.delete_pentagon(list_of_pentagones[index])
                list_of_pentagones.pop(index)
                break
        if (flag == 6):
            os.system("cls || clear")
            if (list_of_pentagones.__len__() + list_of_triangles.__len__() < 1):
                print("Нужно ввести как минимум 1 фигуру!")
                input()
                continue

            while True:
                print("Пентагоны:")
                index = 1
                for i in list_of_pentagones:
                    print(index, end=") ")
                    print(i.get_id())
                    print(i.get_coord())
                    index += 1
                print("Треугольники:")
                for i in list_of_triangles:
                    print(index, end=") ")
                    print(i.get_id())
                    print(i.get_coord())
                    index += 1
                list_of_polygones.clear()
                list_of_polygones = list_of_pentagones + list_of_triangles
                print("Введите номера 2х фигур")
                buf1 = get_input_int()
                if (buf1 < 1 or buf1 > list_of_pentagones.__len__() + list_of_triangles.__len__()):
                    print("Нет такой опции")
                    input()
                    os.system("cls || clear")
                    continue
                buf2 = get_input_int()
                if (buf2 < 1 or buf2 > list_of_pentagones.__len__() + list_of_triangles.__len__()):
                    print("Нет такой опции")
                    input()
                    os.system("cls || clear")
                    continue
                if (list_of_polygones[buf1 - 1].is_intersect(list_of_polygones[buf1 - 1], list_of_polygones[buf2 - 1])):
                    print("Фигуры пересекаются")
                else:
                    print("Фигуры не пересекаются")
                input()
                break
        if (flag == 7):
            os.system("cls || clear")
            if (list_of_polygones.__len__() + list_of_pentagones.__len__() == 0):
                print("Нет фигур!")
                input()
                continue
            while True:
                os.system("cls || clear")
                print("Пентагоны:")
                index = 1
                for i in list_of_pentagones:
                    print(index, end=") ")
                    print(i.get_id())
                    print(i.get_coord())
                    index += 1
                print("Треугольники:")
                for i in list_of_triangles:
                    print(index, end=") ")
                    print(i.get_id())
                    print(i.get_coord())
                    index += 1

                print("Введите номер фигуры, которую вы хотите передвинуть")
                buf = get_input_int()
                if (buf < 1 or buf > list_of_pentagones.__len__() + list_of_triangles.__len__()):
                    print("Нет такой опции!")
                    input()
                    continue
                print("Введите на сколько вы хотите передвинуть фигуру по x и y")
                print("Порядок x y")
                x = get_input_int()
                y = get_input_int()
                if buf > list_of_pentagones.__len__():
                    buf = buf - list_of_pentagones.__len__()
                    list_of_triangles[buf - 1].move(x, y)
                    print("Фигура {id} была передвинута на {x} по x и {y} по y".format(
                        id=list_of_triangles[buf - 1].get_id(),
                        x=x,
                        y=y))
                else:
                    list_of_pentagones[buf - 1].move(x, y)
                    print("Фигура {id} была передвинута на {x} по x и {y} по y".format(
                        id=list_of_pentagones[buf - 1].get_id(),
                        x=x,
                        y=y))
                input()
                break
        if (flag == 8): return

if __name__ == '__main__':
    main()
