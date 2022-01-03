def get_shortest_unique_substring(arr, s):
    substring = ""
    occurrence_dict = {}
    if len(s) < len(arr):
        return substring

    for i in range(len(arr)):
        occurrence_dict.update({arr[i]: 0})

    j = 0
    i = 0
    distinct = 0
    while i < len(s):
        distinct = update(occurrence_dict, s[i], 1, distinct)

        while distinct == len(arr):
            if len(substring) == 0 or len(substring) > (i - j):
                substring = s[j:i + 1]
            removed = s[j]
            j += 1
            distinct = update(occurrence_dict, removed, -1, distinct)

        i += 1

    return substring


def update(occurrence_dict, element, increment, distinct):
    occurs = occurrence_dict.get(element)
    incremented = occurs + increment
    if incremented == 1 and occurs < increment:
        distinct += 1
    elif incremented == 0 and occurs > increment:
        distinct -= 1
    occurrence_dict.update({element: incremented})

    return distinct


arr = ['x', 'y', 'z']
str = "xyyzyzyx"

print(get_shortest_unique_substring(arr, str))
str = "xyyzxzxy"

print(get_shortest_unique_substring(arr, str))
