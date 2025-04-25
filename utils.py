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

class Node:
    def __init__(self, value):
        self.value = value
        self.negate = False
        self.left = None
        self.right = None