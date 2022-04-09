import os

def get_input_int():
    while True:
        try:
            return int(input())
        except ValueError as exc:
            print("Введенная строка не является числом")

def menu() -> int:
    while True:
        print("1. Считать объект с файла")
        print('2. Ввести объект через клавиатуру')
        print("3. Вывести слово")
        print("4. Вывести страницы")
        print("5. Удалить элемент")
        print("6. Выйти")
        buf = get_input_int()
        if (buf < 1 or buf > 6):
            print("Нет такой опции")
            input()
            os.system("cls || clear")
            continue
        os.system("cls || clear")
        return buf

class subject_index:
    def __init__(self, word: str = '', pages = []):
        self.word = word
        self.pages = pages

    def get_word(self):
        return self.word
    def get_pages(self):
        return self.pages

    def delete(self):
        self.word = ''
        self.pages = []
        print("Элемент удален!")
        input()
        os.system("cls || clear")

    def set_word(self):
        print("Введите слово:")
        self.word = input()

    def set_pages(self):
        count_of_pages: int
        while (True):
            print("Введите кол-во страниц(максимум 10)")
            buf = get_input_int()
            if (buf > 10 or buf < 0):
                print("Невозможное кол-во страниц")
                input()
                os.system("cls || clear")
                continue
            count_of_pages = buf
            break
        os.system("cls || clear")
        i = 0
        print("Введите номера страниц")
        while (i < count_of_pages):
            buf = get_input_int()
            self.pages.append(buf)
            i = i + 1
        os.system("cls || clear")

    def set_from_file(self, name):
        with open(name, "r") as f:
            line = f.readline()
            self.word = line.replace('\n', '')
            line = f.readline()
            try:
                buf = int(line)
            except ValueError as exc:
                print("Не получилось считать кол-во старниц")
                input()
                os.system("cls || clear")
                return

            if (buf > 10 or buf < 0):
                print("Введено невозможное кол-во страниц")
                input()
                os.system("cls || clear")
                return

            for line in f:
                try:
                    buf = int(line)
                except ValueError as exc:
                    print("Не получилось ввести все номера страниц")
                    input()
                    os.system("cls || clear")
                    return
                self.pages.append(buf)
            print("Объект считан корректно!")
            input()
            os.system("cls || clear")


    def print_word(self):
        print(self.get_word())
        input()
        os.system("cls || clear")

    def print_pages(self):
        print(self.get_pages())
        input()
        os.system("cls || clear")


def main():
    subject_index_1 = subject_index()
    while True:
        flag = menu()
        if (flag == 1): subject_index_1.set_from_file("data.txt")
        if (flag == 2):
            subject_index_1.set_word()
            subject_index_1.set_pages()
        if (flag == 3):
            subject_index_1.print_word()
        if (flag == 4):
            subject_index_1.print_pages()
        if (flag == 5):
            subject_index_1.delete()
        if (flag == 6): return 0

if __name__ == "__main__":
    main()