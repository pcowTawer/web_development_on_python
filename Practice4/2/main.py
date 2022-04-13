from functools import singledispatch
import io
import os
from operator import methodcaller


def get_input_int():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Введенная строка не является числом")


def check_date(date: list) -> bool:
    try:
        month = int(date[1])
    except ValueError:
        print("В списке переданном в check_date \n1 элемент не является числом!")
        input()
        return False

    if month > 12 or month < 1:
        print("Невозможный формат даты!")
        input()
        return False

    # Проверяем год
    try:
        year = int(date[2])
    except ValueError:
        print("В списке переданном в check_date \n2 элемент не является числом!")
        input()
        return False

    try:
        day = int(date[0])
    except ValueError:
        print("В списке переданном в check_date \n0 элемент не является числом!")
        input()
        return False

    if day > 31 or day < 1:
        print("Невозможный формат даты!")
        input()
        return False
    if month % 2 == 0 and month < 8:
        if day > 30:
            print("Невозможный формат даты!")
            input()
            return False
        if month == 2:
            if day > 29:
                print("Невозможный формат даты!")
                input()
                return False
            if day > 28 and year % 4 != 0:
                print("Невозможный формат даты!")
                input()
                return False
        if month % 2 == 1 and month > 8:
            if day > 30:
                print("Невозможный формат даты!")
                input()
                return False
    return True




class Note:
    def __init__(self):
        self._name = ""
        self._surname = ""
        self._phone_number = None
        self._birth_date = []

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_phone_number(self):
        return self._phone_number

    def get_birth_date(self):
        return self._birth_date

    def set_name(self, name):
        self._name = str(name)

    def set_surname(self, surname):
        self._surname = surname

    def set_phone_number(self, phone_number):
        try:
            self._phone_number = int(phone_number)
        except ValueError:
            print("Переданный аргумент в set_phone_number() не является числом")
            input()

    def set_birth_date(self, birth_date: list):
        # Проверяем месяц
        try:
            month = int(birth_date[1])
        except ValueError:
            print("В списке переданном в set_birth_date \n1 элемент не является числом!")
            input()
            return
        # Проверяем год
        try:
            year = int(birth_date[2])
        except ValueError:
            print("В списке переданном в set_birth_date \n2 элемент не является числом!")
            input()
            return
        try:
            day = int(birth_date[0])
        except ValueError:
            print("В списке переданном в set_birth_date \n0 элемент не является числом!")
            input()
            return

        if check_date([day, month, year]):
            self._birth_date = [day, month, year]

    def print_note(self):
        print("Имя: ", self._name)
        print("Фамилия: ", self._surname)
        print("Номер телефона: ", self._phone_number)
        print("Дата рождения: ", end="")
        for x in self._birth_date:
            print(x, end=" ")
        print()

    def __del__(self):
        pass


@singledispatch
def input_note(label) -> Note:
    os.system("cls || clean")
    note = Note()
    note.set_name(input("Введите имя: "))
    note.set_surname(input("Введите фамилию: "))
    print("Введите номер телефона: ", end='')
    note.set_phone_number(get_input_int())
    print("Введите дату рождения: ")
    note.set_birth_date([get_input_int(), get_input_int(), get_input_int()])
    return note


@input_note.register(str)
def _(label) -> Note:
    print(label)
    return input_note(None)


@input_note.register(io.TextIOBase)
def _(label) -> Note:
    os.system("cls || clean")
    note = Note()
    note.set_name(str.rstrip(label.readline()))
    note.set_surname(str.rstrip(label.readline()))
    note.set_phone_number(label.readline())
    note.set_birth_date([label.readline(), label.readline(), label.readline()])
    return note


def find_note(list_of_notes: list, surname: str):
    i: int = 0
    count: int = 0
    print("Ищю человека с фамилией", surname)
    try:
        for note in list_of_notes:
            if note.get_surname() == surname:
                note.print_note()
                count = count + 1
            i = i + 1
        if count == 0:
            print("Человек с такой фамилией не найден")
    except AttributeError:
        print("В списке переданном find_note", i,
              "элемент не является объектом класса Note")


def menu() -> int:
    os.system("cls || clean")
    while True:
        print("1. Создать заметку(максимум 8)")
        print("2. Вывести все заметки")
        print("3. Удалить заметку")
        print("4. Найти по фамилии")
        print("5. Выход")
        buf = get_input_int()
        if buf < 1 or buf > 5:
            print("Нет такой опции")
            input()
            os.system("cls || clear")
            continue
        os.system("cls || clear")
        return buf


def main():
    list_of_notes = []
    count_of_notes = 0
    while True:
        flag = menu()
        if flag == 1:
            if count_of_notes >= 8:
                print("Невозможно добавить новую запись!")
                input()
                continue
            count_of_notes += 1
            list_of_notes.append(input_note(None))
            list_of_notes.sort(key=methodcaller("get_phone_number"))
        if flag == 2:
            for note in list_of_notes:
                note.print_note()
            input()
        if flag == 3:
            i: int = 0
            for i in range(count_of_notes):
                print(i + 1, end=") ")
                list_of_notes[i].print_note()
            print("Введите номер note:")
            buf = get_input_int()
            if buf > count_of_notes or buf < 1:
                print("Нет такого параметра")
                input()
                continue
            count_of_notes -= 1
            list_of_notes.pop(buf - 1)
            list_of_notes.sort(key=methodcaller("get_phone_number"))

        if flag == 4:
            surname = input("Введите фамилию: ")
            exist: bool = False
            for note in list_of_notes:
                if note.get_surname() == surname:
                    exist = True
                    note.print_note()
            if not exist:
                print("Нет человека с такой фамилией!")
            input()
        if flag == 5:
            return


if __name__ == "__main__":
    main()
