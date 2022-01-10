def get_permutations(nums):
    perms = []
    if len(nums) == 1:
        return [nums]
    for i in range(len(nums)):
        removed = nums.pop(i)
        copy = nums.copy()
        nums.insert(i, removed)
        get_perms = permutations(copy)
        for perm in get_perms:
            perm.append(removed)
        perms.extend(get_perms)

    return perms


nums = [1, 2, 3]
print(get_permutations(nums))

nums = [0, 1]
print(get_permutations(nums))

nums = [1]
print(get_permutations(nums))
