class Note:
    def __init__(self, name, surname, phone_number, birth_date: list):
        self._name = name
        self._surname = surname
        self._phone_number = phone_number
        self._birth_date = birth_date

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_phone_number(self):
        return self._phone_number

    def get_birth_date(self):
        return self._birth_date


def main():
    pass


if __name__ == "__main__":
    main()