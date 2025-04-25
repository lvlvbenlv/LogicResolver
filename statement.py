from binarytree import Node

class Statement:

    def __init__(self, statement, value):
        self.components = statement.split()
        self.value = value
