comparable = [int, float]


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def compare_to(self, other):
        if self.value > other:
            return 1
        if self.value < other:
            return -1
        return 0


class BinaryTree:

    def __init__(self):
        self._head = None
        self._count = 0

    def get_count(self):
        return self._count

    def add(self, value):
        if self._head is None:
            self._head = BinaryTreeNode(value)
        else:
            self.add_to(self._head, value)
        self._count += 1

    def add_to(self, node: BinaryTreeNode, value):
        if value < node.value:
            if node.left is None:
                node.left = BinaryTreeNode(value)
            else:
                self.add_to(node.left, value)
        else:
            if node.right is None:
                node.right = BinaryTreeNode(value)
            else:
                self.add_to(node.right, value)

    def clear(self):
        self._head = None
        self._count = 0

    def find_with_parent(self, value):
        current: BinaryTreeNode = self._head
        parent = None

        while current is not None:
            result = current.compare_to(value)
            if result > 0:
                parent = current
                current = current.left
            elif result < 0:
                parent = current
                current = current.right
            else:
                break

        return current, parent

    def contains(self, value):
        result, parent = self.find_with_parent(value)
        return result is not None

    def remove(self, value):
        current, parent = self.find_with_parent(value)

        if current is None:
            return False

        self._count -= 1

        if current.right is None:
            if parent is None:
                self._head = current.left
            else:
                result = parent.compare_to(current.value)
                if result > 0:
                    parent.left = current.left
                elif result < 0:
                    parent.right = current.left
        elif current.right.left is None:
            current.right.left = current.left
            if parent is None:
                self._head = current.right
            else:
                result = parent.compare_to(current.value)
                if result > 0:
                    parent.left = current.right
                elif result < 0:
                    parent.right = current.right
        else:
            left_most: BinaryTreeNode = current.right.left
            left_most_parent = current.right
            while left_most.left is not None:
                left_most_parent = left_most
                left_most = left_most.left
            left_most_parent.left = left_most.right
            left_most.left = current.left
            left_most.right = current.right
            if parent is None:
                self._head = left_most
            else:
                result = parent.compare_to(current.value)
                if result > 0:
                    parent.left = left_most
                elif result < 0:
                    parent.right = left_most
        return True

    def pre_order_traversal(self):
        self._pre_order_traversal(self._head)

    def _pre_order_traversal(self, node: BinaryTreeNode):
        if node is not None:
            print(node.value)
            self._pre_order_traversal(node.left)
            self._pre_order_traversal(node.right)

    def post_order_traversal(self):
        self._post_order_traversal(self._head)

    def _post_order_traversal(self, node: BinaryTreeNode):
        if node is not None:
            self._post_order_traversal(node.left)
            self._post_order_traversal(node.right)
            print(node.value)

    def in_order_traversal(self):
        self._in_order_traversal(self._head)

    def _in_order_traversal(self, node: BinaryTreeNode):
        if node is not None:
            self._in_order_traversal(node.left)
            print(node.value)
            self._in_order_traversal(node.right)


def main():
    tree = BinaryTree()
    tree.add(4)
    tree.add(2)
    tree.add(5)
    tree.add(1)
    tree.add(3)
    tree.add(7)
    tree.add(6)
    tree.add(8)
    print(tree.contains(10))
    print('\n', tree.get_count(), '\n')
    tree.remove(4)
    print('\n', tree.get_count(), '\n')
    tree.in_order_traversal()
    tree.clear()
    print('\n', tree.get_count(), '\n')


if __name__ == "__main__":
    main()
