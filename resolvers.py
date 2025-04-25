class TruthTables:
    def resolveAnd(self, statement1, statement2):
        return statement1.value and statement2.value

    def resolveOr(self, statement1, statement2):
        return statement1.value or statement2.value

    def resolveNot(self, statement1):
        return not statement1.value

    def resolveImply(self, condition, consequence):
        return (not condition.value) or consequence.value

    def resolveIff(self, s1, s2):
        return (s1.value or (not s2.value)) and ((not s1.value) or s2.value)