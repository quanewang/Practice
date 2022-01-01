def find_pairs_with_given_difference(arr, k):
    pairs = []
    elements = {}
    for x in range(len(arr)):
        complement = arr[x] - k
        other_complement = arr[x] + k

        val = elements.get(complement)
        if val is not None:
            pairs.insert(val, [arr[x], complement])

        val = elements.get(other_complement)
        if val is not None:
            pairs.insert(val, [other_complement, arr[x]])

        elements.update({arr[x]: x})

    return pairs


print(find_pairs_with_given_difference([0, -1, -2, 2, 1], 1))
print(find_pairs_with_given_difference([1, 7, 5, 3, 32, 17, 12], 17))
