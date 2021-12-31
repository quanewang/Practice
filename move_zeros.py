def move_zeros(list):
    i = 0
    count = 0
    while i in range(len(list)):
        if list[i] == 0:
            count += 1
        else:
            list[i - count] = list[i]
        i += 1

    for j in range(len(list) - count, len(list)):
        list[j] = 0

    return list


print(move_zeros([1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]))
