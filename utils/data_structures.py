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
        self.parent = None
        self.leaves = [self]

    ### setters ###

    def set_value(self, value):
        self.value = value

    def set_left(self, binary_tree):
        self._set_branch('left', binary_tree)

    def set_right(self, binary_tree):
        self._set_branch('right', binary_tree)

    def set_parent(self, parent):
        self.parent = parent

    ### public methods ###

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    def print_tree(self, indent=0):
        print('  ' * indent + str(self.value))
        if self.left:
            print('  ' * (indent + 1) + 'L:', end='')
            self.left.print_tree(indent + 2)
        if self.right:
            print('  ' * (indent + 1) + 'R:', end='')
            self.right.print_tree(indent + 2)

    ### internal methods ###

    def _set_branch(self, branch_name, binary_tree):
        branch = getattr(self, branch_name) # either self.left or self.right
        binary_tree.parent = self
        if branch:
            self._update_leaves(branch.leaves, binary_tree.leaves)
            self._update_parent_leaves(branch.leaves, binary_tree.leaves)
        else:
            self._update_leaves([self], binary_tree.leaves)
            self._update_parent_leaves([self], binary_tree.leaves)
        setattr(self, branch_name, binary_tree)


    def _update_leaves(self, rm_leaves, add_leaves):
        self._remove_leaves(rm_leaves)
        self.leaves += add_leaves

    def _update_parent_leaves(self, rm_leaves, add_leaves):
        if self.parent:
            self.parent._remove_leaves(rm_leaves)
            self.parent.leaves += add_leaves
            self.parent._update_parent_leaves(rm_leaves, add_leaves)

    def _remove_leaves(self, rm):
        for leaf in rm:
            try:
                self.leaves.remove(leaf)
            except ValueError:
                pass

    def _is_leaf(self):
        return self.left is None and self.right is None

# bt = BinaryTree(5)
# bt.set_left(BinaryTree(3))
# bt.set_right(BinaryTree(9))
# print(bt.leaves)
# bt.print_tree()