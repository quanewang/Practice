def rearrange_array(arr):
    upper_half = len(arr) // 2
    count = 1
    for k in range(upper_half, len(arr)):
        j = k
        while j != count:
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp
            j -= 1
        count += 2
    return arr


def extra_space_rearrange(arr):
    available = [1] * len(arr)
    available[0] = 0

    middle = len(arr) // 2

    for i in range(1, len(arr)):
        goal_index = i
        pointed_to = arr[goal_index]
        while available[i]:
            goal_index = get_index(middle, goal_index)
            available[goal_index] = 0
            temp = arr[goal_index]
            arr[goal_index] = pointed_to
            pointed_to = temp
    return arr


def get_index(middle, index):
    if index < middle:
        return 2 * index
    return (index - middle) * 2 + 1


def swap_rearrange(arr, pair_size=1):
    if len(arr) == 2:
        return arr

    return swap_helper(arr, len(arr))


def swap_helper(arr, end, pair_size=1):
    if end // pair_size == 2 or pair_size >= end:
        return arr
    end = shuffle_helper(arr, 0, end, pair_size)
    middle = end // 2 - pair_size // 2
    b = middle
    swap_ind = 1 + pair_size // 2
    while b < end - pair_size:
        for i in range(pair_size):
            temp = arr[swap_ind]
            arr[swap_ind] = arr[b]
            arr[b] = temp
            b += 1
            swap_ind += 1
        b += pair_size
        swap_ind += pair_size
    swap_helper(arr, end, pair_size * 2)

    return arr


def shuffle_helper(arr, beg, end, pair_size,):
    middle = (beg + end) // 2
    pairs = middle // pair_size
    if pairs % 2:
        shuffle_ind = middle - pair_size
        for i in range(pair_size):
            while shuffle_ind != end - 2 * pair_size:
                temp = arr[shuffle_ind]
                arr[shuffle_ind] = arr[shuffle_ind + pair_size]
                arr[shuffle_ind + pair_size] = temp
                shuffle_ind += 1
        return end - 2
    else:
        return end


# print(rearrange_array(["a0", "a1", "a2", "a3", "b0", "b1", "b2", "b3"]))

# print(extra_space_rearrange(["a0", "a1", "a2", "a3", "b0", "b1", "b2", "b3"]))

print(swap_rearrange(["a0", "a1", "a2", "a3", "a4", "a5", "a6", "b0", "b1", "b2", "b3", "b4", "b5", "b6"]))

print(swap_rearrange(["a0", "a1", "a2", "a3", "a4", "a5", "b0", "b1", "b2", "b3", "b4", "b5"]))

arr = ["a0", "b0", "a2", "b2", "a4", "b4", "a1", "b1", "a3", "b3", "a5", "b5"]
print(shuffle_helper(arr, 0, len(arr), 2))


