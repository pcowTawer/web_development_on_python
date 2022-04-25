class ListNode:
    def __init__(self, other):
        self.object = other
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def add_in_top(self, other):
        if self.head is None:
            self.head = ListNode(other)
            return
        buf = ListNode(other)
        buf.next = self.head
        self.head = buf

    def add_in_end(self, other):
        if self.head is None:
            self.head = ListNode(other)
            return
        buf = self.head
        while buf.next is not None:
            buf = buf.next
        buf.next = ListNode(other)

    def __str__(self):
        word = ""
        buf = self.head

        while buf is not None:
            word = word + str(buf.object) + " "
            buf = buf.next
        return word


class Deque:
    def __init__(self):
        self.list_of_pre = List()
        self.local_list = List()

    def add_in_top(self, other):
        self.local_list.add_in_top(other)
        self.list_of_pre.add_in_top(None)
        if self.local_list.head.next is not None:
            self.list_of_pre.head.next = self.local_list.head

    def add_in_end(self, other):
        self.local_list.add_in_end(other)

    def __str__(self):
        word = ""
        buf = self.local_list.head

        while buf is not None:
            word = word + str(buf.object) + " "
            buf = buf.next
        return word


def main():
    # my_list = List()
    # my_list.add_in_top(5)
    # my_list.add_in_top(4)
    # my_list.add_in_top(3)
    # my_list.add_in_top(2)
    # my_list.add_in_top(1)
    # my_list.add_in_top(6)
    # print(my_list)
    deque = Deque()
    deque.add_in_top(5)
    deque.add_in_top(4)
    deque.add_in_top(3)
    deque.add_in_top(2)
    deque.add_in_end(10)
    print(deque)


if __name__ == "__main__":
    main()
