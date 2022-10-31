import sys


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def traverse_preorder(self):
        def traverse(current):
            yield current.value
            if current.left:
                yield from traverse(current.left)
            if current.right:
                yield from traverse(current.right)

        yield from traverse(self)


# код ниже руками не трогать
a, b, c, d, e = 'a', 'b', 'c', 'd', 'e'
node = Node(a,
            Node(b,
                 Node(c),
                 Node(d)),
            Node(e))
print(''.join([x for x in node.traverse_preorder()]))
