class Node:
    def __init__(self, value: int, left: "Node" = None, right: "Node" = None) -> None:
        self.value = value
        self.left = left
        self.right = right

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def __iter__(self) -> "InOrderIterator":
        return InOrderIterator(self)


class InOrderIterator:
    def __init__(self, root: "Node") -> None:
        self.root = self.current = root
        self.yielder_start = False

        while self.current.left:
            self.current = self.current.left

    def __next__(self):
        if not self.yielder_start:
            self.yielder_start = True
            return self.current

        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current
        else:
            p = self.current.parent
            while p and self.current == p.right:
                self.current = p
                p = p.parent
            self.current = p
            if self.current:
                return self.current
            else:
                raise StopIteration


def traverse_in_order(root: "Node") -> "Node":
    def traverse(current: "Node") -> "Node":
        if current.left:
            for left in traverse(current.left):
                yield left
        yield current

        if current.right:
            for right in traverse(current.right):
                yield right

    for node in traverse(root):
        yield node


if __name__ == "__main__":
    _root = Node(
        1,
        Node(4, Node(2), Node(3)),
        Node(5, Node(7), Node(8)),
    )
    print("iter")
    for i in _root:
        print(i.value, end=", ")
        print("\nyield")

    for i in traverse_in_order(_root):
        print(i.value, end=", ")

if __name__ == "__main__":
    _root = Node(1, Node(2), Node(3))
