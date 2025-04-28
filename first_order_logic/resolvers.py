from utils.data_structures import *

class TruthTables:
    def resolveAnd(self, statement1, statement2):
        if statement1.value != Values.UNKNOWN and statement2 != Values.UNKNOWN:
            return bool(statement1.value) and bool(statement2.value)

    def resolveOr(self, statement1, statement2):
        if statement1.value != Values.UNKNOWN and statement2.value != Values.UNKNOWN:
            return bool(statement1.value) or (statement2.value)

    def resolveNot(self, statement1):
        if statement1.value != Values.UNKNOWN:
            return not statement1.value

    def resolveImply(self, condition, consequence):
        if condition.value != Values.UNKNOWN and consequence != Values.UNKNOWN:
            return (not condition.value) or consequence.value

    def resolveIff(self, s1, s2):
        if s1.value != Values.UNKNOWN and s2.value != Values.UNKNOWN:
            return s1.value == s2.value