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

        if not heap_ends or building_height > current_height:  # empty heap == new building is start of block
            skyline.append([building[0], building[2]])

        elif building_height < current_height:
            adjusted_start = check_heap(heap_ends, building[0], building_height)
            skyline.append([adjusted_start, building[2]])

        if building[1] > max_end:
            max_end = building[1]
        current_height = building_height
        heapq.heappush(heap_ends, [building[1], building[2]])

    skyline.append([max_end, 0])

    return skyline


def check_heap(heap_ends, building_start, building_height):
    adjusted_start = building_start
    for end_height_pair in heap_ends:
        end, height = end_height_pair[0], end_height_pair[1]
        if end > building_start and height > building_height:
            if end > adjusted_start:
                adjusted_start = end
    return adjusted_start



buildings = [[2, 6, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(get_skyline(buildings))

buildings = [[0, 2, 3], [2, 5, 3]]
print(get_skyline(buildings))
