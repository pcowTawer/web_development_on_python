from functools import singledispatch
import io
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


@singledispatch
def input_note(label) -> Note:
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


def main():
    list_of_notes = [Note(), Note(), Note(), Note(),
                     Note(), Note(), Note(), Note()]
    # list_of_notes[0] = input_note(None)
    # print_note(list_of_notes[0])
    # input()
    # os.system("cls || clear")
    #
    # list_of_notes[1] = input_note("text")
    # print_note(list_of_notes[1])
    # input()
    # os.system("cls || clear")
    #
    # with open("text.txt", "r") as f:
    #     list_of_notes[2] = input_note(f)
    # print_note(list_of_notes[2])
    # input()
    # os.system("cls || clear")
    with open("text.txt", "r") as f:
        for i in range(list_of_notes.__len__()):
            list_of_notes[i] = input_note(f)
        list_of_notes.sort(key=methodcaller("get_phone_number"))
        for note in list_of_notes:
            note.print_note()


if __name__ == "__main__":
    main()
