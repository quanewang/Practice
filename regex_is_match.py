def is_match(text, pattern):
    i = 0
    j = 0
    return match_helper(text, pattern, i, j)


def match_helper(text, pattern, i=0, j=0):
    match = False
    if i >= len(text) and j >= len(pattern):
        return True
    if j >= len(pattern):
        return match
    char = pattern[j]
    text_char = text[i]
    if j + 1 < len(pattern) and pattern[j + 1] == '*':
        match = match_helper(text[i:len(text)], pattern[j + 2:len(pattern)])
        if match:
            return match
        if compare(char, text_char):
            return match_helper(text[i + 1:len(text)], pattern[j:len(pattern)])
    elif compare(char, text_char):
        i += 1
        j += 1
    else:
        return False

    match = match_helper(text, pattern, i, j)
    return match


def compare(char, other):
    if char == '.' or other == '.':
        return True
    return char == other


text = "acd"
pattern = "ab*cd"

print(is_match(text, pattern))

text = "abcd"
print(is_match(text, pattern))

text = "abbbbcd"
print(is_match(text, pattern))

text = "abcd"
pattern = "ab*bcd"
print(is_match(text, pattern))

text = "aa"
print(is_match(text, pattern))

text = "abcd"
pattern = "ab.d"
print(is_match(text, pattern))

text = "acxbc"
pattern = "a.*bc"
print(is_match(text, pattern))
