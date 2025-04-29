import re

from utils.data_structures import *
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
        self.construct(self.AST)

    def construct(self, binary_tree):
        for connective in Connectives.PRIORITY:
            leaves = self.AST.leaves[:] # copy the leaves list, shouldn't use deep copy
            for leaf in leaves:
                if self._remove_parens(leaf.value):
                    # there's a substructure in parentheses, recursively construct it from the first connective
                    self.construct(leaf)
                else:
                    self._construct_by_token(leaf, connective)

    def _construct_by_token(self, binary_tree, token):
        index = self._token_ignore_parens(binary_tree, token)
        if index is not None:
            if token != Connectives.NOT:
                binary_tree.set_left(BinaryTree(binary_tree.value[:index]))
            binary_tree.set_right(BinaryTree(binary_tree.value[index+1:]))
            binary_tree.set_value(token)
            self._construct_by_token(binary_tree.right, token)

    def _token_ignore_parens(self, binary_tree, token):
        parens = ParenStack()
        for index, t in enumerate(binary_tree.value):
            parens.take(t)
            if parens.is_empty() and t == token:
                return index

    def _remove_parens(self, lst):
        if lst and lst[0] == Delimiters.L_PAREN and lst[-1] == Delimiters.R_PAREN:
            del lst[0]
            del lst[-1]
            return True
        else:
            return False

# tokens = LexicalAnalyser("\\iff A").tokens
# print(tokens)
# ASTConstructor(tokens).AST.print_tree()















