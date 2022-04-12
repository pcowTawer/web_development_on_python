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


def input_note() -> Note:
    note = Note()
    note.set_name(input("Введите имя: "))
    note.set_surname(input("Введите фамилию: "))
    print("Введите номер телефона: ", end='')
    note.set_phone_number(get_input_int())
    print("Введите дату рождения: ")
    note.set_birth_date([get_input_int(), get_input_int(), get_input_int()])
    return note


def print_note(note: Note):
    print("Имя: ", note.get_name())
    print("Фамилия: ", note.get_surname())
    print("Номер телефона: ", )
    print("Дата рождения: ", end="")
    for x in note.get_birth_date():
        print(x, end=" ")


def main():
    list_of_notes = [Note(), Note(), Note(), Note(),
                     Note(), Note(), Note(), Note()]
    list_of_notes[0] = input_note()
    print_note(list_of_notes[0])
    input()


if __name__ == "__main__":
    main()
