import re
from utils.data_structures import *
from utils.tokens import *
from itertools import product
from copy import deepcopy

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



class AbstractSyntaxTree(BinaryTree):

    def __init__(self, tokens):
        super().__init__(tokens)
        self.__construct__(self)

    @classmethod
    def __construct__(cls, ast):
        for connective in Connectives.PRIORITY:
            leaves = ast.leaves[:] # copy the leaves list, shouldn't use deepcopy
            for leaf in leaves:
                if cls.__remove_parens__(leaf.value) and leaf.value:
                    # there's a substructure in parentheses, recursively construct it from the first connective
                    cls.__construct__(leaf)
                elif leaf.value:
                    cls.__construct_by_token__(leaf, connective)

    @classmethod
    def __construct_by_token__(cls, ast, token):
        index = cls.__token_ignore_parens__(ast, token)
        if index is not None:
            if token != Connectives.NOT:
                ast.set_left(cls(ast.value[:index]))
            ast.set_right(cls(ast.value[index + 1:]))
            ast.set_value(token)
            cls.__construct_by_token__(ast.right, token)

    @classmethod
    def __token_ignore_parens__(cls, binary_tree, token):
        parens = ParenStack()
        for index, t in enumerate(binary_tree.value):
            parens.take(t)
            if parens.is_empty() and t == token:
                return index

    @staticmethod
    def __remove_parens__(lst):
        if lst and lst[0] == Delimiters.L_PAREN and lst[-1] == Delimiters.R_PAREN:
            parens = ParenStack()
            for index, t in enumerate(lst):
                parens.take(t)
                if parens.is_empty():
                    if index == len(lst) - 1:
                        lst[:] = lst[1:-1]
                        return True
                    else:
                        return False
        else:
            return False



class StatementForm(AbstractSyntaxTree):

    def __init__(self, tokens):
        super().__init__(tokens)
        self.logic_value = Values.UNKNOWN

    def set_var(self, name, logic_value):
        for leaf in self.leaves:
            if leaf.value == [name]:
                leaf.logic_value = logic_value

    def evaluate(self):
        if self.is_leaf():
            return self.logic_value
        else:
            if self.value == Connectives.NOT:
                return Values.Not(self.right.evaluate())
            elif self.value == Connectives.AND:
                return Values.And(self.left.evaluate(), self.right.evaluate())
            elif self.value == Connectives.OR:
                return Values.Or(self.left.evaluate(), self.right.evaluate())
            elif self.value == Connectives.IMPLY:
                return Values.Imply(self.left.evaluate(), self.right.evaluate())
            elif self.value == Connectives.IFF:
                return Values.Iff(self.left.evaluate(), self.right.evaluate())
            else:
                raise ValueError(f"Unrecognized connective {repr(self.value)}")

    def is_tautology(self):
        vars = list(set([leaf.value[0] for leaf in self.leaves]))
        vars_num = len(vars)
        all_comb = list(product([0, 1], repeat=vars_num))
        logical_results = []
        for comb in all_comb:
            self_copy = deepcopy(self)
            for i in range(vars_num):
                self_copy.set_var(vars[i], comb[i])
            logical_results.append(self_copy.evaluate())
        return all(logical_results)

# query = "\\not A\\and (B\\or(C \\imply D\\and \\not E)\\or F\\iff G)\\or H\\imply I"
# tokens = LexicalAnalyser(query).tokens
# s = statementForm(tokens)
# s.set_var("A", Values.TRUE)
# s.set_var("B", Values.TRUE)
# s.set_var("C", Values.TRUE)
# s.set_var("D", Values.TRUE)
# s.set_var("E", Values.TRUE)
# s.set_var("F", Values.TRUE)
# s.set_var("G", Values.TRUE)
# s.set_var("H", Values.FALSE)
# s.set_var("I", Values.FALSE)
# print(s.evaluate())

# query = "( ( ( A \\or B ) \\and ( C \\or D ) ) \\and ( C \\or D ) )"
# tokens = LexicalAnalyser(query).tokens
# s = statementForm(tokens)
# print(s.is_tautology())