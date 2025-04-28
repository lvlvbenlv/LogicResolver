class Values:
    TRUE = 1
    FALSE = 0
    UNKNOWN = -1

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)