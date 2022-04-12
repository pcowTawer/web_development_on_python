class ListNode:
    def __init__(self, other):
        self.object = other
        self.next = None
        self.pre = None


class List:
    def __init__(self):
        self.head = None

    def add_in_top(self, other):
        pass

    def add_in_end(self, other):
        pass

    def __str__(self):
        word = ""
        buf = self.head

        while buf is not None:
            word = word + str(buf.object) + " "
            buf = buf.next
        return word

class Deque(List):
    def add_in_top(self, other):
        if self.head is None:
            self.head = ListNode(other)
            return
        buf = ListNode(other)
        self.head.pre = buf
        buf.next = self.head
        self.head = buf

    def add_in_end(self, other):
        if self.head is None:
            self.head = ListNode(other)
            return

        buf = self.head

        while buf.next is not None:
            buf = buf.next

        buf1 = ListNode(other)
        buf.next = buf1
        buf1.pre = buf




def main():
    deque = Deque()
    deque.add_in_top(5)
    deque.add_in_top(4)
    deque.add_in_top(3)
    deque.add_in_top(2)
    deque.add_in_end(6)
    print(deque)

if __name__ == "__main__":
    main()
