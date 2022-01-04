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
        if char != text_char:
            j += 2
        else:
            match = match_helper(text[i + 1:len(text)], pattern[j:len(pattern)])
            if match:
                return match
            return match_helper(text[i:len(text)], pattern[j + 2:len(pattern)])
    elif char == "." or char == text_char:
        i += 1
        j += 1
    elif char != text_char:
        return False

    match = match_helper(text, pattern, i, j)
    return match

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

