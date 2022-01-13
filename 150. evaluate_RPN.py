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


tokens = ["2","1","+","3","*"]
print(eval_RPN(tokens))

tokens = ["4","13","5","/","+"]
print(eval_RPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(eval_RPN(tokens))

