from binarytree import Node
from symbols import *
from utils import Stack

class Statement:

    def __init__(self, statement, value):
        self.components = statement.split()
        self.value = value

    def find_pairs(lst, start, end):
        def find_all_parentheses_positions(lst):
            left_indices = []
            right_indices = []
            for i, element in enumerate(lst):
                if element == Brackets.LEFT_PARENTHESES:
                    left_indices.append(i)
                elif element == Brackets.RIGHT_PARENTHESES:
                    right_indices.append(i)
            return left_indices, right_indices

        left_l, right_l = find_all_parentheses_positions(lst)
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
                inner_pairs = find_pairs(lst, current_start + 1, current_end - 1)
                if inner_pairs:
                    small_list_pairs.extend(inner_pairs)
                pairs.append(small_list_pairs)
                current_start = i + 1
        return pairs
    

class Node:
    def __init__(self, value):
        self.value = value
        self.negate = False
        self.left = None
        self.right = None 

def insert(root, pare_pairs): #initialize the bst, parents node value contains operations, leave value is the variable
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
        root.left = insert(root.left, pare_pairs[0])
        root.right = insert(root.right, pare_pairs[1])

    elif len(pare_pairs) == 3:  # case with 1 larger parenthesis, following two base cases
        root.value = pare_pairs[2][0][0] - 1  # pair list only contains base cases
        check_children(root)
        root.left = insert(root.left, pare_pairs[1])
        root.right = insert(root.right, pare_pairs[2])

    elif len(pare_pairs) == 2:  # case with 1 larger parenthesis, following 1 base cases
        left_or_right = (pare_pairs[1][0] - pare_pairs[0][0]) == 1  # if left tuple is just next to the outer parenthesis
        if left_or_right:
            root.value = pare_pairs[0][1] - 2  # second last element
            if root.left is None:
                root.left = Node(None)
            root.left = insert(root.left, [pare_pairs[1]])
            if root.right is None:
                root.right = Node(pare_pairs[0][1] - 1)
        else:
            root.value = pare_pairs[0][0] + 2  # second element
            if root.left is None:
                root.left = Node(pare_pairs[0][0] + 1)
            if root.right is None:
                root.right = Node(None)
            root.right = insert(root.right, [pare_pairs[1]])
        
        negate = (pare_pairs[1][0] - pare_pairs[0][0]) == 2
        if negate:
            root.negate = True
            root.value = pare_pairs[1][1] - 2 
            root.left = Node(pare_pairs[1][1] - 3)
            root.right = Node(pare_pairs[1][1] - 1)
    return root