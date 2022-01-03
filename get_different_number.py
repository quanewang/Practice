def get_different_number(arr):  # count-sort
    element_set = set()
    for i in range(len(arr)):
        element_set.add(arr[i])

    for i in range(len(arr)):
        if i not in element_set:
            return i
    return len(arr)


print(get_different_number([0, 1, 2, 3, 4]))
print(get_different_number([0, 3, 2, 1, 5, 7]))
print(get_different_number([7, 5, 4, 3, 2, 1]))
