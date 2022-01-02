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


print(rearrange_array(["a0", "a1", "a2", "a3", "b0", "b1", "b2", "b3"]))
