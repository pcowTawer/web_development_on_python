class ListNode:
    def __init__(self, other):
        self.object = other
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def add_in_head(self, other):
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

    def remove(self):
        if self.head is None:
            return
        self.head = self.head.next

    def __str__(self):
        word = ""
        buf = self.head

        while buf is not None:
            word = word + str(buf.object) + " "
            buf = buf.next
        return word


class Deque:
    def __init__(self):
        self.list_of_pre = []
        self.local_list = List()

    def add_in_head(self, other):
        self.local_list.add_in_head(other)
        self.list_of_pre.insert(0, None)
        if self.local_list.head.next is not None:
            self.list_of_pre[1] = self.local_list.head

    def add_in_end(self, other):
        self.local_list.add_in_end(other)
        self.list_of_pre.append(self.list_of_pre[self.list_of_pre.__len__() - 1].next)

    def remove_in_head(self):
        self.local_list.remove()
        self.list_of_pre.pop(1)

    def remove_in_end(self):
        self.list_of_pre[self.list_of_pre.__len__() - 1].next = None
        self.list_of_pre.pop(self.list_of_pre.__len__() - 1)

    def print_list_of_pre(self):
        word = "None "
        for buf in self.list_of_pre[1:]:
            word = word + str(buf.object) + " "
        print(word)

    def __str__(self):
        word = ""
        buf = self.local_list.head

        while buf is not None:
            word = word + str(buf.object) + " "
            buf = buf.next
        return word


def main():
    deque = Deque()
    deque.add_in_head(5)
    deque.add_in_head(4)
    deque.add_in_head(3)
    deque.add_in_head(2)
    deque.add_in_end(10)
    deque.add_in_head(15)
    deque.add_in_end(15)
    deque.add_in_end(15)
    deque.remove_in_end()
    deque.add_in_head(15)
    deque.remove_in_head()
    deque.print_list_of_pre()
    print(deque)


if __name__ == "__main__":
    main()
