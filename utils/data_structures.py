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
        self.leaves = [self.value]

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    def set_left(self, binary_tree):
        self._remove_leaves(self.leaves, self.left.leaves)
        self.leaves += binary_tree.leaves
        self.left = binary_tree

    def set_right(self, binary_tree):
        self._remove_leaves(self.leaves, self.right.leaves)
        self.leaves += binary_tree.leaves
        self.right = binary_tree

    def print_tree(self, indent=0):
        print('  ' * indent + str(self.value))
        if self.left:
            print('  ' * (indent + 1) + 'L:', end='')
            self.left.print_tree(indent + 2)
        if self.right:
            print('  ' * (indent + 1) + 'R:', end='')
            self.right.print_tree(indent + 2)

    def _remove_leaves(self, ls, rm):
        for leaf in rm:
            try:
                ls.remove(leaf)
            except ValueError:
                print(f"Leaf {leaf} doesn't exist")