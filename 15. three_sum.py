def three_sum(nums):
    nums = sorted(nums)
    three_sums = []
    traversed_over = set()
    for i in range(len(nums)):
        if nums[i] in traversed_over:
            pass
        else:
            three_sums.extend(find_pairs(nums, i + 1, len(nums) - 1, -nums[i], nums[i]))
            traversed_over.add(nums[i])

    return three_sums


def find_pairs(nums, l, r, expected, num):
    duplicate = set()
    pairs = []
    while l < len(nums) and r >= 0 and l < r:
        sum = nums[l] + nums[r]
        if sum < expected:
            l += 1
        elif sum > expected:
            r -= 1
        else:
            if (num, nums[l], nums[r]) not in duplicate:
                pairs.append([num, nums[l], nums[r]])
                duplicate.add((num, nums[l], nums[r]))
            l += 1

    return pairs


print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([0, 0, 0, 0]))
