import random


def main():
    # list = []
    # for a in input().split():
    #     list.append(int(a))
    # max_id = list.index(max(list))
    # min_id = list.index(min(list))
    # list[min_id], list[max_id] = list[max_id], list[min_id]
    # print(list)

    list = [[0] * 5 for i in range(5)]
    for i in range(5):
        for j in range(5):
            if (i == j):
                list[i][j] = 1
            if (i > j):
                list[i][j] = list[j][i]
            if (i < j):
                list[i][j] = 0
    for i in range(5):
        print(*list[i])

    for i in range(5):
        for j in range(5):
            if list[i][j] != list[j][i]:
                print("Нессиметрична")
                return
    print('Симметрична')
if __name__ == "__main__":
    main()
