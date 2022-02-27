import heapq

def findKthLargest(nums, k):
    k_nums = []
    for num in nums:

        if len(k_nums) == k:
            min = heapq.heappop(k_nums)
            if min < num:
                heapq.heappush(k_nums, num)
            else:
                heapq.heappush(k_nums, min)
        else:
            heapq.heappush(k_nums, num)

    return heapq.heappop(k_nums)

print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))