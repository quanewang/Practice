def get_range(nums, target):
    first = (target + target - 1) / 2
    last = (target + target + 1) / 2

    first = binary_search(nums, first, 0, len(nums) - 1)
    last = binary_search(nums, last, 0, len(nums) - 1)
    if first == last:
        return [-1, -1]
    return [first + 1, last]


def binary_search(nums, target, beg, end):
    mid = (beg + end) // 2

    if beg > end:
        return mid
    if nums[mid] == target:
        return mid
    if nums[mid] > target:
        return binary_search(nums, target, beg, mid - 1)
    else:
        return binary_search(nums, target, mid + 1, end)


print(get_range([5, 7, 7, 8, 8, 10], 8))
print(get_range([5, 7, 7, 8, 8, 10], 6))
print(get_range([], 0))
