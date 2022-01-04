def deletion_distance(str1, str2):
    if str1 == str2:
        return 0
    queue = [(str1, str2, 0)]

    while len(queue):
        copy_1, copy_2, deletion_count = queue.pop(0)
        if copy_1 == copy_2:
            return deletion_count
        i = 0
        if len(copy_1) and len(copy_2):
            char_1, char_2 = copy_1[0], copy_2[0]
            if char_1 == char_2:
                while i < len(copy_1) and i < len(copy_2) and copy_1[i] == copy_2[i]:
                    i += 1
        if len(copy_1):
            new_copy_1 = replace_next(copy_1, i)
            queue.append((new_copy_1, copy_2, deletion_count + 1))
        if len(copy_2):
            new_copy_2 = replace_next(copy_2, i)
            queue.append((copy_1, new_copy_2, deletion_count + 1))
    return 0


def replace_next(string, i):
    if i < len(string):
        return string.replace(string[1], "", 1)
    return string



str1 = "dog"
str2 = "frog"

print(deletion_distance(str1, str2))

str1 = "some"
str2 = "some"
print(deletion_distance(str1, str2))

str1 = "some"
str2 = "thing"
print(deletion_distance(str1, str2))

str1 = ""
str2 = ""
print(deletion_distance(str1, str2))

str1 = "heat"
str2 = "htea"
print(deletion_distance(str1, str2))
