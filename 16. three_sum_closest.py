import sys


def three_sum_closest(nums, target):
    nums = sorted(nums)
    traversed_over = set()
    closest = None
    for i in range(len(nums)):
        if nums[i] in traversed_over:
            pass
        else:
            current = find_closest(nums, i + 1, len(nums) - 1, nums[i], target)
            if closest is None:
                closest = current
            elif current is not None and abs(target - current) < abs(target - closest):
                closest = current
            if closest == target:
                return closest
            traversed_over.add(nums[i])
    return closest


def find_closest(nums, l, r, num, target):
    closest = None
    while l < len(nums) and r >= 0 and l < r:
        current = nums[l] + nums[r] + num
        if current == target:
            return current
        elif closest is None or abs(target - current) < abs(target - closest):
            closest = current

        if current < target:
            l += 1
        else:
            r -= 1

    return closest


print(three_sum_closest([-1, 2, 1, -4], 1))

print(three_sum_closest([0, 0, 0], 1))

print(three_sum_closest([1,1,-1,-1,3], -1))

print(three_sum_closest([-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33], 0))
