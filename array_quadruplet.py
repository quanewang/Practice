def array_quadruplet(arr, s):
    if len(arr) < 4:
        return []

    arr = sorted(arr)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            x = j + 1
            y = len(arr) - 1
            remainder = s - arr[i] - arr[j]
            while x < y:
                if x + y > remainder:
                    y -= 1
                elif x + y < remainder:
                    x += 1
                else:
                    return [i, j, x, y]

    return []


print(array_quadruplet([2, 7, 4, 0, 9, 5, 1, 3], 20))
