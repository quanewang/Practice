def count_zeros(list):

    i = 0
    count = 0
    while i in range(len(list)):
        if list[i] == 0:
            count += 1
        i = shuffle(list, i, count)

    for j in range(len(list) - count, len(list)):
        list[j] = 0

    return list

def shuffle(list, i, count):
    if count == 0 or list[i] == 0:
        return i + 1
    while list[i] != 0:
        list[i - count] = list[i]
        i += 1
    return i

print(count_zeros([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]))