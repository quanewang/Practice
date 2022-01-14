def find_median(nums1, nums2):
    n = len(nums1) + len(nums2)
    med = n // 2
    if n % 2 == 0:
        med_1 = med + 1
        med = get_median(nums1, nums2, med)  # length of arr? len(nums) or len(nums) - 1
        med_1 = get_median(nums1, nums2, med_1)
        return (med + med_1) / 2
    else:
        med += 1
    return get_median(nums1, nums2, med)


def get_median(nums1, nums2, med):
    if med == 1 and nums1 and nums2:
        return min(nums1[0], nums2[0])
    if not nums1:
        return nums2[med - 1]
    elif not nums2:
        return nums1[med - 1]

    mid_0 = (len(nums1) - 1) // 2
    mid_1 = binary_search(nums2, 0, len(nums2) - 1, nums1[mid_0])

    if mid_0 + mid_1 + 2 > med:
        if mid_1 == -1:
            return get_median(nums1[0:mid_0], [], med)
        return get_median(nums1[0: mid_0], nums2[0: mid_1 + 1], med)  # fix  med
    elif mid_0 + mid_1 + 2 < med:
        if mid_1 == -1:
            return get_median(nums1[mid_0 + 1: len(nums1)], nums2, med - (mid_0 + 1 + mid_1 + 1))
        return get_median(nums1[mid_0 + 1: len(nums1)], nums2[mid_1 + 1: len(nums2)], med - (mid_0 + 1 + mid_1 + 1))
    else:
        if mid_1 == -1 or nums1[mid_0] > nums2[mid_1]:
            return nums1[mid_0]
        else:
            return nums2[mid_1]


def binary_search(arr, beg, end, key, closest=-1):
    if end == beg:
        if arr[beg] == key:
            return beg
        elif (closest == -1 and arr[beg] < key) or (closest != -1 and arr[closest] < arr[beg] < key):
            return beg
        else:
            return closest
    mid = (beg + end) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search(arr, mid + 1, end, key, mid)
    else:
        return binary_search(arr, beg, mid, key, closest)


nums1 = [1, 2, 4]
nums2 = [3]
print(find_median(nums1, nums2))

nums1 = [1, 4, 10, 30]
nums2 = [2, 3, 9, 12]
print(find_median(nums1, nums2))


nums1 = [1, 2, 3]
nums2 = [4, 11, 12, 15, 16]
print(find_median(nums1, nums2))


nums1 = [1, 10]
nums2 = [2, 3, 9, 12]
print(find_median(nums1, nums2))

nums1 = [3]
nums2 = [-2, -1]
print(find_median(nums1, nums2))

nums1 = [100001]
nums2 = [100000]
print(find_median(nums1, nums2))




