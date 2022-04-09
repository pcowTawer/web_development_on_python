import random
import os
def get_input_int() -> int:
    while True:
        try:
            return int(input())
        except ValueError as exc:
            print("Введенная строка не является числом")

def main():
    rub = 3
    wins = 0
    while True:
        os.system("cls || clear")
        print("Игра \"Орлянка\"\n")
        print("У вас на счету {rub} рублей".format(rub=rub))
        print("Выигрышей: {wins}\n".format(wins=wins))
        print("Введите:")
        print("0: орел")
        print("1: решка")
        print("любое другое число - выход из игры")

        buf = get_input_int()
        if (buf < 0 or buf > 1):
            os.system("cls || clear")
            print("Спасибо за игру!")
            input()
            return

        if(random.randrange(0,2,1) == buf):
            os.system("cls || clear")
            print("Вы выиграли рубль!")
            wins += 1
            rub += 1
            input()
        else:
            os.system("cls || clear")
            print("Вы проиграли рубль!")
            rub -= 1
            if (not rub):
                print("Рублей не осталось")
                print("Спасибо за игру!")
                input()
                return

            input()


if __name__ == '__main__':
    main()
