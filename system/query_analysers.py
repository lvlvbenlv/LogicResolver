import re
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

    def keyword_index(self, start):
        str = self.query
        index = start
        while re.match(self.KEYWORD_PATTERN, str[index]):
            index += 1
        self.query = str[index:]
        self.tokens.append(str[:index])