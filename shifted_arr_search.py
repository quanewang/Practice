def shifted_arr_search(arr, num):
    shift_index = -1
    mid_index = (len(arr) - 1) // 2
    shift_index = find_shift(arr, 0, len(arr) - 1, mid_index)

    mid_index = (shift_index - 1) // 2
    num_index = search(arr, 0, shift_index - 1, mid_index, num)
    if num_index == -1:
        mid_index = (shift_index + len(arr) - 1) // 2
        num_index = search(arr, shift_index, len(arr) - 1, mid_index, num)

    return num_index


def search(arr, beg, end, mid, num):
    if arr[mid] == num:
        return mid
    elif beg >= end:
        return -1
    if arr[mid] < num:
        new_mid = (mid + 1 + end) // 2
        return search(arr, mid + 1, end, new_mid, num)
    else:
        new_mid = (beg + mid - 1) // 2
        return search(arr, beg, mid - 1, new_mid, num)


def find_shift(arr, beg, end, mid):
    if beg >= end:
        return mid
    if arr[mid] > arr[end]:
        new_mid = (mid + 1 + end) // 2
        return find_shift(arr, mid + 1, end, new_mid)
    else:
        new_mid = (beg + mid - 1) // 2
        return find_shift(arr, beg, mid - 1, new_mid)


print(shifted_arr_search([9, 12, 17, 2, 4, 5], 2))
