def find_pairs_with_given_difference(arr, k):
    pairs = []
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x] - arr[y] == k:
                pairs.insert(y, [arr[x], arr[y]])
    return pairs


print(find_pairs_with_given_difference([0, -1, -2, 2, 1], 1))
print(find_pairs_with_given_difference([1, 7, 5, 3, 32, 17, 12], 17))
