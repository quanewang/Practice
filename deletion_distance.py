def deletion_distance(str1, str2):
    deletion_count = 0
    if str1 == str2:
        return deletion_count
    set_1 = set()
    set_2 = set()
    for char in str1:
        set_1.add(char)

    for char in str2:
        set_2.add(char)

    for char in str1:
        if char not in set_2:
            deletion_count += 1
    for char in str2:
        if char not in set_1:
            deletion_count += 1
    return deletion_count


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
