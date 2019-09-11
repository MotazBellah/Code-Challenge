import operator

def x(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = [0]
    for token in expr.split(" ")[::-1]:
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            print(op1, op2)
            stack.append(OPERATORS[token](op2,op1))
        elif token:
            stack.append(float(token))
    return stack.pop()
