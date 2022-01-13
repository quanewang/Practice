def eval_RPN(tokens):
    stack = []
    operators = {"+", "-", "*", "/"}
    for char in tokens:
        if char not in operators:
            stack.insert(len(stack), int(char))
        else:
            op_0 = stack.pop(len(stack) - 1)
            op_1 = stack.pop(len(stack) - 1)
            if char == '+':
                stack.insert(len(stack), op_1 + op_0)
            elif char == '-':
                stack.insert(len(stack), op_1 - op_0)
            elif char == '*':
                stack.insert(len(stack), op_1 * op_0)
            else:
                stack.insert(len(stack), int(op_1 / op_0))
    return stack[0]


tokens = ["2", "1", "+", "3", "*"]
print(eval_RPN(tokens))

tokens = ["4", "13", "5", "/", "+"]
print(eval_RPN(tokens))

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(eval_RPN(tokens))

tokens = ["a+b*d+c"]


def infix_to_postfix(expression):
    operators = []
    operands = []
    for char in expression:
        if char == '*' or char == '+':
            operators.append(char)
        else:
            operands.append(char)

    while operators:
        operator = operators.pop(len(operators) - 1)
        e_0 = operands.pop(len(operands) - 1)
        e_1 = operands.pop(len(operands) - 1)
        if operator == '*' and len(e_0) != 1:
            operands.insert(len(operands), e_1 + e_0[0] + operator + e_0[1:len(e_0)])
        else:
            operands.insert(len(operands), e_1 + e_0 + operator)
    return operands.pop(0)


expression = "1+2*3"
print(infix_to_postfix(expression))

expression = "1*2*3"
print(infix_to_postfix(expression))

expression = "1*2*3+4"
print(infix_to_postfix(expression))

expression = "1+2+3+4"
print(infix_to_postfix(expression))

expression = "1*2*3*4"
print(infix_to_postfix(expression))
