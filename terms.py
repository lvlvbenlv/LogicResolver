import re
from utils import *

class Atom:

    def __init__(self, name):
        if self.valid_name(name):
            self.name = name
        else:
            raise ValueError("Invalid name")

    def valid_name(s):
        pattern = r"^[a-z][A-Za-z0-9_]*$"
        return bool(re.match(pattern, s))


class Variable:

    def __init__(self, name):
        if self.valid_name(name):
            self.name = name
        else:
            raise ValueError("Invalid name")
        self.value = Values.UNKNOWN

    def set_value(self, value):
        self.value = value

    def valid_name(self, s):
        pattern = r"^[A-Z][A-Za-z0-9_]*$"
        return bool(re.match(pattern, s))
