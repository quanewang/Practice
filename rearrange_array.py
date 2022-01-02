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


print(rearrange_array(["a0", "a1", "a2", "a3", "b0", "b1", "b2", "b3"]))

print(extra_space_rearrange(["a0", "a1", "a2", "a3", "b0", "b1", "b2", "b3"]))
