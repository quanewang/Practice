def shifted_arr_search(arr, num):
    shift_index = find_shift(arr, 0, len(arr) - 1)

    num_index = search(arr, 0, shift_index - 1, num)
    
    if num_index == -1:
        num_index = search(arr, shift_index, len(arr) - 1, num)

    return num_index


def search(arr, beg, end, num):
    mid = (beg + end) // 2
    if arr[mid] == num:
        return mid
    elif beg >= end:
        return -1
    if arr[mid] < num:
        return search(arr, mid + 1, end, num)
    else:
        return search(arr, beg, mid - 1, num)


def find_shift(arr, beg, end):
    mid = (beg + end) // 2
    if beg >= end:
        return mid
    if arr[mid] > arr[end]:
        return find_shift(arr, mid + 1, end)
    else:
        return find_shift(arr, beg, mid - 1)


print(shifted_arr_search([9, 12, 17, 2, 4, 5], 2))
