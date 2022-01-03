def bracket_match(text):
    stack = []
    for i in range(len(text)):
        char = text[i]
        if len(stack) == 0:
            stack.append(char)
        elif char == ')' and stack[len(stack) - 1] == '(':
            stack.pop(len(stack) - 1)
        else:
            stack.append(char)
    return len(stack)


print(bracket_match(")))((("))
print(bracket_match("(())()("))
print(bracket_match(")()(()("))
