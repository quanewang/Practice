def reverse_string(str):
    n = len(str) - 1
    # reverse the entire string
    reverse_helper(str, 0, n)

    beg = 0
    for i in range(len(str)):
        if str[i] == ' ':
            end = i - 1
            reverse_helper(str, beg, end)
            beg = i + 1

        elif i == len(str) - 1:
            end = i
            reverse_helper(str, beg, end)

    return str


def reverse_helper(str, beg, end):
    for j in range(beg, (end + beg) // 2 + 1):
        opposite = (end - j) + beg
        temp = str[j]
        str[j] = str[opposite]
        str[opposite] = temp


print(reverse_string(['g', 'o', ' ', 'w', 'i', 't', 'h', 'o', 'u', 't', ' ', 'w', 'i', 'n', 'd']))
