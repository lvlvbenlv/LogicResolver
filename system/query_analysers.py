import re
from copy import deepcopy
from utils.data_structures import BinaryTree
from utils.tokens import *

class LexicalAnalyser:

    KEYWORD_PATTERN = r"[a-zA-Z0-9_]"

    def __init__(self, query):
        self.query = query
        self.tokens = []
        self.tokenize()

    def tokenize(self):
        while len(self.query) > 0:
            first_char = self.query[0]
            if first_char == " ":
                self.skip_space()
            elif Delimiters.is_delimiter(first_char):
                self.extract_delimiter()
            elif first_char == Symbols.HEAD:
                self.extract_symbol()
            elif re.match(self.KEYWORD_PATTERN, first_char):
                self.extract_term()
            else:
                raise ValueError(f"Unable to recognize token head {first_char}")

    def skip_space(self):
        self.query = self.query[1:]

    def extract_delimiter(self):
        str = self.query
        self.query = str[1:]
        self.tokens.append(str[0])

    def extract_symbol(self):
        self.keyword_index(1)

    def extract_term(self):
        self.keyword_index(0)

    def keyword_index(self, index):
        str = self.query
        while (index < len(str)) and re.match(self.KEYWORD_PATTERN, str[index]):
            index += 1
        self.query = str[index:]
        self.tokens.append(str[:index])



class ASTConstructor:

    def __init__(self, tokens):
        self.tokens = tokens
        self.AST = BinaryTree(self.tokens)
        self.construct()

    def construct(self):
        for connective in Connectives.PRIORITY:
            leaves = self.AST.leaves[:]
            for leaf in leaves:
                self._construct_by_token(leaf, connective)

    def _construct_by_token(self, binary_tree, token):
        for index, t in enumerate(binary_tree.value):
            if t == token:
                if token != Connectives.NOT:
                    binary_tree.set_left(BinaryTree(binary_tree.value[:index]))
                binary_tree.set_right(BinaryTree(binary_tree.value[index+1:]))
                binary_tree.set_value(token)
                self._construct_by_token(binary_tree.right, token)

tokens = LexicalAnalyser("\\not A\\and B\\or C \\imply D\\and \\not E\\or F\\iff G\\or H\\imply I").tokens
print(tokens)
ASTConstructor(tokens).AST.print_tree()















