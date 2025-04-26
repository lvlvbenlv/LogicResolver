def evaluate_expression(expression):
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
            stack.append(result)
    return stack[0] if stack else None

def evaluate_sub_expression(sub_expr):
    print(sub_expr)
    while len(sub_expr) > 1:
        left = sub_expr.pop(0)
        operator = sub_expr.pop(0)
        right = sub_expr.pop(0)
        result = logit_oper(operator, left, right)
        sub_expr.insert(0, result)
    return sub_expr[0]