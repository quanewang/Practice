def get_shortest_unique_substring(arr, s):
    substring = ""
    occurrence_dict = {}
    if len(s) < len(arr):
        return substring

    for i in range(len(arr)):
        occurrence_dict.update({arr[i]: 0})

    queue = []
    temp_string = ""
    for i in range(len(s)):
        (temp_string, substring) = helper_parse(arr, s, occurrence_dict, queue, temp_string, i, substring)
        for j in range(i + 1, len(s)):
            (temp_string, substring) = helper_parse(arr, s, occurrence_dict, queue, temp_string, j, substring)

    return substring


def helper_parse(arr, s, occurrence_dict, queue, temp_string, i, substring):
    if check(occurrence_dict, arr, len(arr)):
        if len(substring) == 0 or len(substring) > len(temp_string):
            substring = temp_string
        removed = queue.pop(0)
        update(occurrence_dict, removed, -1)
        temp_string = temp_string.replace(temp_string[0], "", 1)
    else:
        queue.append(s[i])
        temp_string = temp_string + s[i]
        update(occurrence_dict, s[i], 1)
    return temp_string, substring


def update(occurrence_dict, element, increment):
    occurs = occurrence_dict.get(element)
    occurrence_dict.update({element: occurs + increment})


def check(occurrence_dict, arr, length):
    for i in range(length):
        if occurrence_dict.get(arr[i]) < 1:
            return False
    return True

arr = ['x', 'y', 'z']
str = "xyyzyzyx"

print(get_shortest_unique_substring(arr, str))
