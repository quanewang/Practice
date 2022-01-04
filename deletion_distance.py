def deletion_distance(str1, str2):
    if str1 == str2:
        return 0
    queue = [(str1, str2, 0)]

    while len(queue):
        copy_1, copy_2, deletion_count = queue.pop(0)
        while len(copy_1) and len(copy_2) and copy_1[0] == copy_2[0]:
            copy_1 = copy_1.replace(copy_1[0], "", 1)
            copy_2 = copy_2.replace(copy_2[0], "", 1)

        if (copy_1 == copy_2) or (not len(copy_1) and not len(copy_2)):
            return deletion_count

        if len(copy_1):
            new_copy_1 = copy_1.replace(copy_1[0], "", 1)
            queue.append((new_copy_1, copy_2, deletion_count + 1))
        if len(copy_2):
            new_copy_2 = copy_2.replace(copy_2[0], "", 1)
            queue.append((copy_1, new_copy_2, deletion_count + 1))
    return 0


def replace_next(string, i):
    if i < len(string):
        return string.replace(string[i], "", 1)
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
