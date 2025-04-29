from system.query_analysers import *
from utils.data_structures import *
from first_order_logic.stack_method import *
from itertools import product

class Statement:

    def __init__(self, statement):
        self.components = LexicalAnalyser(statement).tokens # a list of all statement components
        self.value = Values.UNKNOWN # the logic value of the statement
        

            


class StatementForm(Statement):

    def __init__(self, statement):
        super().__init__(statement)
        self.get_variables()

    # statements only consist of logic variables
    def get_variables(self):
        self.variables = []
        for i in range(len(self.components)):
            component = self.components[i]
            try:
                if component in [v.name for v in self.variables]:
                    var = next(v for v in self.variables if v.name == component)
                else:
                    var = Variable(component)
                index = self.components.index(component)
                self.components[index] = var
                if var.name not in [v.name for v in self.variables]:
                    self.variables.append(var)
            except ValueError:
                pass


    def is_tautology(self):
        self.get_variables()
        variable_count = len(self.variables)
        all_comb = list(product([0, 1], repeat=variable_count))
        logical_results = []
        for comb in all_comb:
            for i in range(variable_count):
                self.variables[i].set_value(comb[i])
            current_expression = self.components
            logical_results.append(evaluate_expression(current_expression).value)
        return (all(logical_results))
