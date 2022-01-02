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
    j = 1

    for i in range(1, len(arr)):
        j = i
        pointed_to = arr[j]
        while available[i]:
            if j < middle:
                if 2 * j < len(arr):
                    available[2 * j] = 0
                    temp = arr[2 * j]
                    arr[2 * j] = pointed_to
                    j *= 2
                    pointed_to = temp
            else:
                b_number = j - middle
                index = b_number * 2 + 1

                available[index] = 0
                temp = arr[index]
                arr[index] = pointed_to
                j = index
                pointed_to = temp
    return arr


print(rearrange_array(["a0", "a1", "a2", "a3", "b0", "b1", "b2", "b3"]))

print(extra_space_rearrange(["a0", "a1", "a2", "a3", "b0", "b1", "b2", "b3"]))
