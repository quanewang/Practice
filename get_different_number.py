def get_different_number(arr):
    element_dict = {}
    for i in range(len(arr)):
        element_dict.update({arr[i]: True})

    for i in range(len(arr)):
        if not element_dict.get(i):
            return i
    return len(arr)


print(get_different_number([0, 1, 2, 3, 4]))
print(get_different_number([0, 3, 2, 1, 5, 7]))
print(get_different_number([7, 5, 4, 3, 2, 1]))
