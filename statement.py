from terms import *
from symbols import *
from utils import *

class Statement:

    def __init__(self, statement):
        self.components = statement.split() # a list of all statement components
        self.value = Values.UNKNOWN # the logic value of the statement

    def all_pairs(self):
        return self.find_pairs(0, len(self.components) - 1)

    def find_pairs(self, start, end):
        left_l = self.component_indexes(Brackets.LEFT_PARENTHESES)
        right_l = self.component_indexes(Brackets.RIGHT_PARENTHESES)
        pairs = []
        pare_count = 0
        current_start = start
        for i in range(start, end + 1):
            if i in left_l:
                pare_count += 1
            if i in right_l:
                pare_count -= 1
            if pare_count == 0:
                current_end = i
                small_list_pairs = []
                small_list_pairs.append((current_start, current_end))
                inner_pairs = self.find_pairs(current_start + 1, current_end - 1)
                if inner_pairs:
                    small_list_pairs.extend(inner_pairs)
                pairs.append(small_list_pairs)
                current_start = i + 1
        return pairs

    def component_indexes(self, component):
        return [i for i, c in enumerate(self.components) if c == component]

    def initialize_bst(self):
        return self.insert(Node(None), self.all_pairs())

    def insert(self, root, pare_pairs): # initialize the bst, parent node value contains operations, leave value is the variable
        def get_first_operator(pare_pairs):
            if isinstance(pare_pairs[0], list):
                return get_first_operator(pare_pairs[0])
            elif isinstance(pare_pairs[0], tuple):
                return pare_pairs[0][0]

        def check_children(node):
            if node.left is None:
                node.left = Node(None)
            if node.right is None:
                node.right = Node(None)

        if not pare_pairs:
            return None

        if len(pare_pairs) == 1:  # base case
            root.value = pare_pairs[0][1] - 2  # should only contain 3 elements inside pair
            root.left = Node(pare_pairs[0][1] - 3)
            root.right = Node(pare_pairs[0][1] - 1)

        elif len(pare_pairs) == 2 and isinstance(pare_pairs[0], list) and isinstance(pare_pairs[1], list):  # existing smaller independent expression components
            outter_operator = get_first_operator(pare_pairs[1])
            root.value = outter_operator - 1
            check_children(root)
            root.left = self.insert(root.left, pare_pairs[0])
            root.right = self.insert(root.right, pare_pairs[1])

        elif len(pare_pairs) == 3:  # case with 1 larger parenthesis, following two base cases
            root.value = pare_pairs[2][0][0] - 1  # pair list only contains base cases
            check_children(root)
            root.left = self.insert(root.left, pare_pairs[1])
            root.right = self.insert(root.right, pare_pairs[2])

        elif len(pare_pairs) == 2:  # case with 1 larger parenthesis, following 1 base cases
            left_or_right = (pare_pairs[1][0] - pare_pairs[0][0]) == 1  # if left tuple is just next to the outer parenthesis
            if left_or_right:
                root.value = pare_pairs[0][1] - 2  # second last element
                if root.left is None:
                    root.left = Node(None)
                root.left = self.insert(root.left, [pare_pairs[1]])
                if root.right is None:
                    root.right = Node(pare_pairs[0][1] - 1)
            else:
                root.value = pare_pairs[0][0] + 2  # second element
                if root.left is None:
                    root.left = Node(pare_pairs[0][0] + 1)
                if root.right is None:
                    root.right = Node(None)
                root.right = self.insert(root.right, [pare_pairs[1]])

            negate = (pare_pairs[1][0] - pare_pairs[0][0]) == 2
            if negate:
                root.negate = True
                root.value = pare_pairs[1][1] - 2
                root.left = Node(pare_pairs[1][1] - 3)
                root.right = Node(pare_pairs[1][1] - 1)
        return root



# statements only consist of logic variables
class StatementForm(Statement):

    def get_variables(self):
        self.variables = []
        for component in self.components:
            try:
                var = Variable(component)
                if var not in self.variables:
                    self.variables.append(var)
            except ValueError:
                continue