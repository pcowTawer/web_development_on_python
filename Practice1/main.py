import math
import os

def get_input_float() -> float:
    while True:
        try:
            return float(input())
        except ValueError as exc:
            print(f"Введенная строка не является числом. Попробуйте заново. \n Подробнее: {exc}")

def get_input_int() -> int:
    while True:
        try:
            return int(input())
        except ValueError as exc:
            print(f"Введенная строка не является числом. Попробуйте заново. \n Подробнее: {exc}")

def menu() -> int:
    while True:
        os.system("cls||clear")
        print("1. Вычислить значение\n2. Выход.")
        flag = get_input_int()
        if flag == 1: break
        if flag == 2: break
        print("Данного параметра не существует. Попробуйте снова")
        input()
    os.system("cls||clear")
    return flag

def get_user_input():
    while True:
        print("Введите значение точности:")
        exactness = get_input_float()
        if exactness <= 0:
            print("Невозможно вычислить значение с точностью меньшей либо равной 0!. Попробуйте снова")
            input()
            os.system("cls||clear")
            continue
        print("Введите значение x:")
        x = get_input_float()
        return exactness, x

def show_result(result: float):
    print(f"Результат {result}")

def write_result_in_file(exactness, x, result):
    f = open('results.txt', 'a+t')
    f.write(str(exactness) + " " + str(x) + " " + str(result) + "\n")
    f.close()

def calculation(exactness: float, x: float) -> float:
    factor = 1 - (x/math.pi) * (x/math.pi)
    iterator = 1
    last_result = 0
    result = factor * x
    while abs(last_result - result) > exactness:
        iterator = iterator + 1
        factor = 1 - (x / (iterator * math.pi)) * (x / (iterator * math.pi))
        last_result = result
        result = result * factor
    return result

def main():

    while True:
        flag = menu()
        if flag == 2: break
        exactness, x = get_user_input()
        result = calculation(exactness, x)
        show_result(result)
        write_result_in_file(exactness, x, result)
        input()


if __name__ == '__main__':
    main()