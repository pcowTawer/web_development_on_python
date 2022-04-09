def main():
    # a
    list1 = [list1 for list1 in range(0, 100, 10)]
    list2 = [list2 for list2 in range(0, 100, 10)]
    a = list1[1]
    b = list2[2]
    print(list1)
    print(list2, end="\n\n")

    # b
    second_elem = list1.pop(2)
    print(second_elem, end="\n\n")

    # c
    list2[list2.__len__() - 1] = 200
    print(list2, end="\n\n")

    # d
    list3 = list1 + list2
    print(list3, end="\n\n")

    # e
    list4 = list3[list1.__len__() - 2: list1.__len__() + 2]
    print(list4, end="\n\n")

    # f
    list4.append(list3[list1.__len__() + 2])
    list4.append(list3[list1.__len__() + 3])
    print(list4, end="\n\n")

    # g
    for i in list3:
        if i == min(list3) or i == max(list3):
            print(i, end=" ")





if __name__ == "__main__":
    main()