def longest_non_repeating_substring(string):
    max_count = 0
    substring_set = set()
    i = 0
    count = 0
    while i < len(string):
        char = string[i]
        j = i + 1
        while j < len(string) and string[j] not in substring_set:
            substring_set.add(char)
            count += 1
            j += 1
        substring = string[i:j - 1]
        if count > max_count:
            max_count = count
            substring_set = set()
            count = 0
    return max_count


s = "abcabcbb"
print(longest_non_repeating_substring(s))

s = "bbbbb"
print(longest_non_repeating_substring(s))

s = "pwwkew"
print(longest_non_repeating_substring(s))

s = "abcaxyziuol"
print(longest_non_repeating_substring(s))
