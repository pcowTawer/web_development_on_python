import os


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

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def birth_date(self):
        return self._birth_date

    @name.setter
    def name(self, name):
        self._name = str(name)

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @phone_number.setter
    def phone_number(self, phone_number):
        try:
            self._phone_number = int(phone_number)
        except ValueError:
            print("Переданный аргумент в set_phone_number() не является числом")
            input()

    @birth_date.setter
    def birth_date(self, birth_date: list):
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

    def __del__(self):
        pass


def print_note(note: Note):
    print("Имя: ", note.name, end=", ")
    print("фамилия: ", note.surname, end=", ")
    print("номер телефона: ", note.phone_number, end=", ")
    print("дата рождения: ", end="")
    print(*note.birth_date, end=";\n")


def input_note_from_file(file):
    os.system("cls || clean")
    note = Note()
    note.name = str.rstrip(file.readline())
    note.surname = str.rstrip(file.readline())
    note.phone_number = file.readline()
    note.birth_date = [file.readline(), file.readline(), file.readline()]
    return note


def input_note(format_of_input="", to_be_printed=""):
    print(to_be_printed, end="")

    if format_of_input == "file":
        with open(input("Введите название файла:")) as f:
            return input_note_from_file(f)
    note = Note()
    note.surname = input("Введите имя: ")
    note.surname = input("Введите фамилию: ")
    print("Введите номер телефона: ", end='')
    note.phone_number = get_input_int()
    print("Введите дату рождения: ")
    note.birth_date = [get_input_int(), get_input_int(), get_input_int()]
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


class Menu:
    def __init__(self):
        self._count_of_options = 1

    def menu1(self):
        self._count_of_options = 5
        os.system("cls || clean")
        print("1. Создать заметку(максимум 8)")
        print("2. Вывести все заметки")
        print("3. Удалить заметку")
        print("4. Найти по фамилии")
        print("5. Выход")

    @property
    def count_of_options(self):
        return self._count_of_options

    def input_option(self) -> int:
        buf = get_input_int()
        if buf < 1 or buf > self._count_of_options:
            print("Нет такой опции")
            input()
            os.system("cls || clear")
        os.system("cls || clear")
        return buf


def main():
    list_of_notes = []
    count_of_notes = 0
    menu = Menu()
    while True:
        menu.menu1()
        flag = menu.input_option()
        if flag == 1:
            if count_of_notes >= 8:
                print("Невозможно добавить новую запись!")
                input()
                continue
            count_of_notes += 1
            list_of_notes.append(input_note())
            list_of_notes.sort(key=lambda notes: notes.phone_number)
        if flag == 2:
            for i in range(count_of_notes):
                print(i + 1, end=") ")
                print_note(list_of_notes[i])
            input()
        if flag == 3:
            for i in range(count_of_notes):
                print(i + 1, end=") ")
                print_note(list_of_notes[i])
            print("Введите номер note:")
            buf = get_input_int()
            if buf > count_of_notes or buf < 1:
                print("Нет такого параметра")
                input()
                continue
            count_of_notes -= 1
            list_of_notes.pop(buf - 1)
            list_of_notes.sort(key=lambda notes: notes.phone_number)
        if flag == 4:
            surname = input("Введите фамилию: ")
            exist: bool = False
            for note in list_of_notes:
                if note.surname == surname:
                    exist = True
                    print_note(note)
            if not exist:
                print("Нет человека с такой фамилией!")
            input()
        if flag == 5:
            return


if __name__ == "__main__":
    main()
