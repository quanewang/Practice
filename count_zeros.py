def count_zeros(list):
    i = 0
    while i in range(len(list)):
        j = i
        while j < len(list) and list[j] == 0:
            j += 1

        i = shuffle(list, i, j)
    return list

def shuffle(list, i, j):
    if j == i or j >= len(list):
        return i + 1
    while list[j] != 0:
        temp = list[j]
        list[j] = list[i]
        list[i] = temp
        i += 1
        j += 1
    return i

print(count_zeros([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]))