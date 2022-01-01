import heapq

def k_messed_array(arr, k):
    q = []
    for i in range(k + 1):
        heapq.heappush(q, arr[i])

    for i in range(len(arr)):
        arr[i] = heapq.heappop(q)
        next_index = i + k + 1
        if next_index < len(arr):
            heapq.heappush(q, arr[next_index])

    return arr


print(k_messed_array([1, 4, 5, 2, 3, 7, 8, 6, 10, 9], 2))
