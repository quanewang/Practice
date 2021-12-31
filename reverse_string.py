def reverse_string(str):
    n = len(str) - 1
    # reverse the entire string
    reverse_helper(str, 0, n)

    beg = 0
    end = 0
    while end < len(str):
        if str[end] == ' ':
            reverse_helper(str, beg, end - 1)
            beg = end + 1
        elif end == len(str) - 1:
            reverse_helper(str, beg, end)
        end += 1

    return str


def reverse_helper(str, beg, end):
    left = beg
    right = end
    while left < right:
        temp = str[left]
        str[left] = str[right]
        str[right] = temp
        left += 1
        right -= 1



print(reverse_string(['g', 'o', 'w', 'i', 't', 'h', 'o', 'u', 't', 'w', 'i', 'n', 'd']))
