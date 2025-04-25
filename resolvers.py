class TruthTables:
    def resolveAnd(self, statement1, statement2):
        if statement1.value != -1 and statement2 != -1:
            return bool(statement1.value) and bool(statement2.value)

    def resolveOr(self, statement1, statement2):
        if statement1.value != -1 or statement2.value != -1:
            return bool(statement1.value) or (statement2.value)

    def resolveNot(self, statement1):
        if statement1.value != -1:
            return not statement1.value

    def resolveImply(self, condition, consequence):
        if condition.value != -1 and consequence != -1:
            return (not condition.value) or consequence.value

    def resolveIff(self, s1, s2):
        if s1.value != -1 and s2.value != -1:
            return s1.value == s2.value