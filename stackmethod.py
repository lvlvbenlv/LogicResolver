from symbols import Connectives
from resolvers import TruthTables
from terms import Variable


def logit_oper(operator, left, right=None):
    truth_table = TruthTables()
    if operator == Connectives.AND:
        return truth_table.resolveAnd(left, right)
    elif operator == Connectives.OR:
        return truth_table.resolveOr(left, right)
    elif operator == Connectives.NOT:
        return truth_table.resolveNot(left)
    elif operator == Connectives.IMPLY:
        return truth_table.resolveImply(left, right)
    elif operator == Connectives.IFF:
        return truth_table.resolveIff(left, right)

def evaluate_expression(expression): # return an variable object, access by .value
    stack = []
    for i in range(len(expression)):
        stack.append(expression[i])
        if expression[i] == ')':
            sub_expr = []
            
            stack.pop() # Drop the last ')'
            while stack and stack[-1] != '(':
                sub_expr.append(stack.pop())
            stack.pop()  # Remove the '('
            sub_expr = sub_expr[::-1]
            result = evaluate_sub_expression(sub_expr)
            
            sub_statement_result = Variable("Sub_tmp")
            sub_statement_result.set_value(result)
            stack.append(sub_statement_result)
            
    return stack[0] if stack else None

def evaluate_sub_expression(sub_expr):
    if len(sub_expr) == 1:
        return sub_expr[0].value  # Directly return the single variable
    while len(sub_expr) > 1 or (len(sub_expr) == 2 and sub_expr[0] == Connectives.NOT):
        if len(sub_expr) == 2 and sub_expr[0] == Connectives.NOT:
            operator = sub_expr.pop(0)
            operand = sub_expr.pop(0)
            result = logit_oper(operator, operand)
            sub_expr.insert(0, result)
        else:
            left = sub_expr.pop(0)
            operator = sub_expr.pop(0)
            right = sub_expr.pop(0)
            result = logit_oper(operator, left, right)
            sub_expr.insert(0, result)
    return sub_expr[0]