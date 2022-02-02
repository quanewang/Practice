def get_range(nums, target):
    first = binary_search(nums, target, 0, len(nums) - 1, lower_bound_compare)
    last = binary_search(nums, target, 0, len(nums) - 1, upper_bound_compare)
    if not nums or nums[last] != target:
        return [-1, -1]
    return [first + 1, last]


def binary_search(nums, target, beg, end, compare):
    mid = (beg + end) // 2
    if beg > end:
        return mid

    result = compare(nums[mid], target)

    if result == -1:
        return binary_search(nums, target, mid + 1, end, compare)
    else:
        return binary_search(nums, target, beg, mid - 1, compare)


def lower_bound_compare(current, target):
    if current < target:
        return -1
    else:
        return 1


def upper_bound_compare(current, target):
    if current <= target:
        return -1
    else:
        return 1


print(get_range([5, 7, 7, 8, 8, 10], 8))
print(get_range([5, 7, 7, 8, 8, 10], 6))
print(get_range([], 0))
print(get_range([2], 2))
print(get_range([5.0124, 7.02, 7.124, 8, 8, 10], 6))
