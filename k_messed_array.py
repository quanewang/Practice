import heapq


def k_messed_array(arr, k):
    q = []
    result = []

    for i in range(len(arr)):
        if len(q) == k + 1:
            result.append(heapq.heappop(q))

        heapq.heappush(q, arr[i])

    while q:
        result.append(heapq.heappop(q))

    return result


print(k_messed_array([1, 4, 5, 2, 3, 7, 8, 6, 10, 9], 2))
