def bracket_match(text):
    stack = [text[0]]
    for i in range(1, len(text)):
        char = text[i]
        if char == ')' and stack[len(stack) - 1] == '(':
            stack.pop(len(stack) - 1)
        else:
            stack.append(char)
    return len(stack)


print(bracket_match(")))((("))
print(bracket_match("(())()("))
print(bracket_match(")()(()("))
