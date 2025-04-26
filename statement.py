from terms import *
from symbols import *
from utils import *
from stackmethod import *
from itertools import product

class Statement:

    def __init__(self, statement):
        self.components = statement.split() # a list of all statement components
        self.value = Values.UNKNOWN # the logic value of the statement
        
    # statements only consist of logic variables
    def get_variables(self):
        self.variables = []
        self.var_index = []
        for i in range(len(self.components)):
            component = self.components[i]
            try:
                var = Variable(component)
                if var not in self.variables:
                    self.variables.append(var)
                    self.var_index.append(i)
            except ValueError:
                continue
            
    def generate_combinations(self):
        self.get_variables()
        variable_count = len(self.variables)
        all_comb = list(product([0, 1], repeat=variable_count))
        print(all_comb)
        logical_results = []
        for comb in all_comb:
            for i in range(variable_count):
                self.variables[i].set_value(comb[i])
                self.components[self.var_index[i]] = self.variables[i]
            current_expression = self.components
            logical_results.append(evaluate_expression(current_expression).value)
        return (all(logical_results))



