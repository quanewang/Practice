def get_subsets(nums):
    if len(nums) == 0:
        return [[]]
    subsets = []
    removed = nums.pop(0)
    smaller_subsets = get_subsets(nums)
    subsets.extend(smaller_subsets)

    for set in smaller_subsets:
        copy = set.copy()
        copy.append(removed)
        subsets.append(copy)

    return subsets


nums = [1, 2, 3]
print(get_subsets(nums))
