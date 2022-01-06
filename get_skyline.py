import heapq


def get_skyline(buildings):
    skyline = []
    heap_ends = []
    current_height = 0
    max_end = 0
    for building in buildings:
        building_height = building[2]
        if building != buildings[0] and building[0] > max_end:
            heap_ends = []
            current_height = 0
            skyline.append([max_end, current_height])

        if not heap_ends:  # empty heap == new building is start of block
            skyline.append([building[0], building[2]])
            
        elif building_height > current_height:
            skyline.append([building[0], building_height])

        elif building_height < current_height:
            if heap_ends[0][0] > building[0]:
                skyline.append([heapq.heappop(heap_ends)[0], building[2]])

        if building[1] > max_end:
            max_end = building[1]
        current_height = building_height
        heapq.heappush(heap_ends, [building[1], building[2]])

    skyline.append([max_end, 0])

    return skyline


buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(get_skyline(buildings))

buildings = [[0, 2, 3], [2, 5, 3]]
print(get_skyline(buildings))
