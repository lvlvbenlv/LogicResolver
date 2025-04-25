from binarytree import Node

class Statement:

    def __init__(self, statement, value):
        self.components = statement.split()
        self.value = value
        
    def find_all_parentheses_positions(lst):
        left_indices = []
        right_indices = []
        for i, element in enumerate(lst):
            if element == '(':
                left_indices.append(i)
            elif element == ')':
                right_indices.append(i)
        return left_indices, right_indices

    def find_pairs(lst, start, end): 
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
                small_list_pairs =[]
                small_list_pairs.append((current_start, current_end))
                inner_pairs = find_pairs(lst, current_start + 1, current_end - 1)
                if inner_pairs:
                    small_list_pairs.extend(inner_pairs)
                pairs.append(small_list_pairs)
                current_start = i + 1
        return pairs
