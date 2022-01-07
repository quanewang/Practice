import heapq


def get_skyline(buildings):
    skyline = []
    max_heap = []
    for i in range(len(buildings)):
        building = buildings[i]
        while max_heap and building[0] > max_heap[0][1]:
            largest_building = heapq.heappop(max_heap)
            if max_heap:
                next_building = max_heap[0]
                if largest_building[1] < next_building[1]:
                    if largest_building[0] != next_building[0]:
                        skyline.append([largest_building[1], -next_building[0]])
                elif largest_building[1] == next_building[1]:
                    pass
                else:
                    heapq.heappop(max_heap)
            if not max_heap:
                skyline.append([largest_building[1], 0])
        
        if not max_heap or building[2] > -max_heap[0][0]:
            skyline.append([building[0], building[2]])

        heapq.heappush(max_heap, [-building[2], building[1]])

    while max_heap:
        largest_building = heapq.heappop(max_heap)
        if max_heap:
            next_building = max_heap[0]
            if largest_building[1] < next_building[1]:
                if largest_building[0] != next_building[0]:
                    skyline.append([largest_building[1], -next_building[0]])
            elif largest_building[1] == next_building[1]:
                pass
            else:
                heapq.heappop(max_heap)
        if not max_heap:
            skyline.append([largest_building[1], 0])

    return skyline


def check_heap(heap_ends, building_start, building_height):
    adjusted_start = building_start
    for end_height_pair in heap_ends:
        start, end, height = end_height_pair[0], end_height_pair[1], end_height_pair[2]

        if end > building_start and height > building_height:
            if end > adjusted_start:
                adjusted_start = end

        if end < building_start:
            heap_ends.remove(end_height_pair)

    return adjusted_start


def merge_blocks(buildings):
    copy = []
    previous_block = None
    for i in range(len(buildings) - 1):
        if previous_block is None:
            previous_block = merge(buildings[i], buildings[i + 1])
        else:
            previous_block = merge(previous_block, buildings[i])
        if len(previous_block) == 2:
            copy.append(previous_block[0])
            copy.append(previous_block[1])
            previous_block = buildings[i + 1]
    copy.append(previous_block)
    return copy


def merge(first, second):
    if first[0] == second[0] and first[1] == second[1]:
        height = max(first[2], second[2])
        return [first[0], first[1], height]

    elif first[0] == second[0]:
        if first[2] <= second[2]:
            return second
        else:
            return first, [first[1], second[1], second[2]]

    elif first[1] == second[1]:
        if first[2] >= second[2]:
            return [first]
        else:
            return [first[0], second[0], first[2]], second

    return first, second


buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(get_skyline(buildings))

buildings = [[0, 2, 3], [2, 5, 3], [5, 10, 6], [7, 10, 8]]
print(get_skyline(buildings))

buildings = [[2, 6, 10], [3, 7, 15], [4, 10, 19], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(get_skyline(buildings))

buildings = [[1, 2, 1], [1, 2, 2], [1, 2, 3], [2, 6, 10], [3, 7, 15], [4, 10, 19], [5, 12, 12], [15, 20, 10],
             [19, 24, 8]]
print(get_skyline(buildings))

buildings = [[1, 20, 1], [1, 21, 2], [1, 22, 3]]
print(get_skyline(buildings))

buildings = [[3, 7, 8], [3, 8, 7], [3, 9, 6], [3, 10, 5], [3, 11, 4], [3, 12, 3], [3, 13, 2], [3, 14, 1]]
print(get_skyline(buildings))
