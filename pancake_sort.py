import sys


def pancake_sort(arr):
    max_index = 0
    k = len(arr)
    while k != 0:
        curr_max = -sys.maxsize - 1
        i = 0
        while i < k:
            number = arr[i]
            if number > curr_max:
                curr_max = number
                max_index = i
            i += 1
        flip(arr, max_index + 1)
        flip(arr, k)
        k -= 1

    return arr


def flip(arr, k):
    for i in range((k - 1) // 2 + 1):
        swap_index = (k - 1) - i
        temp = arr[i]
        arr[i] = arr[swap_index]
        arr[swap_index] = temp
    return None


arr = [2, 4, 3, 1, 5]

print(pancake_sort(arr))

arr = [1, 2, 3, 4, 5]
print(pancake_sort(arr))

arr = [1, 5, 4, 3, 2]
print(pancake_sort(arr))

arr = [5, 1, 4, 3, 2]
print(pancake_sort(arr))
