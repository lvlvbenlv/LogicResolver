from utils.tokens import *

class Values:

    TRUE = True
    FALSE = False
    UNKNOWN = None

    @staticmethod
    def And(val1, val2):
        if val1 == Values.FALSE or val2 == Values.FALSE:
            return Values.FALSE
        else:
            return val1 and val2

    @staticmethod
    def Or(val1, val2):
        if val1 == Values.TRUE or val2 == Values.TRUE:
            return Values.TRUE
        else:
            return val1 or val2

    @staticmethod
    def Not(val):
        if val == Values.UNKNOWN:
            return Values.UNKNOWN
        else:
            return not val

    @staticmethod
    def Imply(val1, val2):
        return Values.Or(Values.Not(val1), val2)

    @staticmethod
    def Iff(val1, val2):
        return Values.And(Values.Imply(val1, val2), Values.Imply(val2, val1))



class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0



class ParenStack(Stack):

    def take(self, paren):
        if paren == Delimiters.L_PAREN:
            self.push(paren)
        elif paren == Delimiters.R_PAREN:
            if self.is_empty():
                raise ValueError("Unmatched right parenthesis ')'")
            self.pop()



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
        self.__set_branch__('left', binary_tree)

    def set_right(self, binary_tree):
        self.__set_branch__('right', binary_tree)

    ### public methods ###

    def is_leaf(self):
        return self.left is None and self.right is None

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

    def __set_branch__(self, branch_name, binary_tree):
        branch = getattr(self, branch_name) # either self.left or self.right
        binary_tree.parent = self
        if branch:
            self.__update_leaves__(branch.leaves, binary_tree.leaves)
            self.__update_parent_leaves__(branch.leaves, binary_tree.leaves)
        else:
            self.__update_leaves__([self], binary_tree.leaves)
            self.__update_parent_leaves__([self], binary_tree.leaves)
        setattr(self, branch_name, binary_tree)

    def __update_leaves__(self, rm_leaves, add_leaves):
        self.__remove_leaves__(rm_leaves)
        self.leaves += add_leaves

    def __update_parent_leaves__(self, rm_leaves, add_leaves):
        if self.parent:
            self.parent.__remove_leaves__(rm_leaves)
            self.parent.leaves += add_leaves
            self.parent.__update_parent_leaves__(rm_leaves, add_leaves)

    def __remove_leaves__(self, rm):
        for leaf in rm:
            try:
                self.leaves.remove(leaf)
            except ValueError:
                pass