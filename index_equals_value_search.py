def index_equals_value_search(arr):
    return search(arr, 0, len(arr) - 1, -1)


def search(arr, beg, end, lowest_index):
    mid = (beg + end) // 2
    if beg >= end:
        return lowest_index
    if mid > arr[mid]:
        return search(arr, mid + 1, end, lowest_index)
    if mid < arr[mid]:
        return search(arr, beg, mid - 1, lowest_index)
    else:
        if lowest_index == -1:
            lowest_index = mid
        elif lowest_index > mid:
            lowest_index = mid
        return search(arr, beg, mid - 1, lowest_index)


print(index_equals_value_search([-8, 0, 2, 5, 4, 6]))
print(index_equals_value_search([-1, 0, 3, 6, 7]))
