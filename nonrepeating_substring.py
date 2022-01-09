def longest_non_repeating_substring(string):
    max_count = 0
    substring_set = set()
    i = 0
    current_string = ""
    while i < len(string):
        char = string[i]
        substring_set.add(char)
        start_index = i - len(current_string)

        current_string += char
        count = len(current_string)

        j = i + 1
        while j < len(string) and string[j] not in substring_set:
            substring_set.add(string[j])
            count += 1
            current_string += string[j]
            j += 1
        if count > max_count:
            max_count = count
        if j < len(string) and current_string[0] == string[j]:
            i = j
            current_string = current_string.replace(string[j], "", 1)
            substring_set.remove(string[j])
        elif j >= len(string) - 1:
            break
        else:
            i = string.index(string[j], start_index, j) + 1
            substring_set = set()
            current_string = ""

    return max_count

s = "kdgjyzkjhglfp"
print(longest_non_repeating_substring(s))

s = "abcabcbb"
print(longest_non_repeating_substring(s))

s = "bbbbb"
print(longest_non_repeating_substring(s))

s = "pwwkew"
print(longest_non_repeating_substring(s))

s = "bacaxyziuol"
print(longest_non_repeating_substring(s))


