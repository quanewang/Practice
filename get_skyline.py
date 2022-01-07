import heapq


def get_skyline(buildings):
    skyline = []
    max_heap = MaxHeap()
    i = 0
    while i < len(buildings):
        building = buildings[i]
        while (not max_heap.isEmpty()) and building[0] > max_heap.peek()[1]:
            largest_building = max_heap.pop()
            while (not max_heap.isEmpty()) and largest_building[1] > max_heap.peek()[1]:
                max_heap.pop()
            if not max_heap.isEmpty():
                next_building = max_heap.peek()
                if largest_building[1] < next_building[1]:
                    if largest_building[0] != next_building[0]:
                        skyline.append([largest_building[1], next_building[0]])
                elif largest_building[1] == next_building[1]:
                    pass
                else:
                    max_heap.pop()
            if max_heap.isEmpty():
                skyline.append([largest_building[1], 0])

        j = i + 1
        max_height = building[2]
        while j < len(buildings) and building[0] == buildings[j][0]:
            if buildings[j][2] > max_height:
                max_height = buildings[j][2]
            j += 1

        if max_heap.isEmpty() or max_height > max_heap.peek()[0]:
            skyline.append([building[0], max_height])
        max_heap.push([max_height, building[1]])
        i += 1

    while not max_heap.isEmpty():
        largest_building = max_heap.pop()
        while (not max_heap.isEmpty()) and largest_building[1] > max_heap.peek()[1]:
            max_heap.pop()
        if not max_heap.isEmpty():
            next_building = max_heap.peek()
            if largest_building[1] < next_building[1]:
                if largest_building[0] != next_building[0]:
                    skyline.append([largest_building[1], next_building[0]])
            elif largest_building[1] == next_building[1]:
                pass
            else:
                max_heap.pop()
        if max_heap.isEmpty():
            skyline.append([largest_building[1], 0])

    return skyline


class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, element):
        copy = [-element[0], element]
        heapq.heappush(self.heap, copy)

    def pop(self):
        copy = heapq.heappop(self.heap)
        return copy[1]

    def peek(self):
        if not self.isEmpty():
            return self.heap[0][1]

    def isEmpty(self):
        return len(self.heap) == 0


buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(get_skyline(buildings))

buildings = [[0, 2, 3], [2, 5, 3], [5, 10, 6], [7, 10, 8]]
print(get_skyline(buildings))

buildings = [[2, 6, 10], [3, 7, 15], [4, 10, 19], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(get_skyline(buildings))

buildings = [[1, 20, 1], [1, 21, 2], [1, 22, 3]]
print(get_skyline(buildings))

buildings = [[1, 2, 1], [1, 2, 2], [1, 2, 3], [2, 6, 10], [3, 7, 15], [4, 10, 19], [5, 12, 12], [15, 20, 10],
             [19, 24, 8]]
print(get_skyline(buildings))

buildings = [[3, 7, 8], [3, 8, 7], [3, 9, 6], [3, 10, 5], [3, 11, 4], [3, 12, 3], [3, 13, 2], [3, 14, 1]]
print(get_skyline(buildings))

buildings = [[1, 38, 219], [2, 19, 228], [2, 64, 106], [3, 80, 65], [3, 84, 8], [4, 12, 8], [4, 25, 14], [4, 46, 225],
             [4, 67, 187], [5, 36, 118], [5, 48, 211], [5, 55, 97], [6, 42, 92], [6, 56, 188], [7, 37, 42], [7, 49, 78],
             [7, 84, 163], [8, 44, 212], [9, 42, 125], [9, 85, 200], [9, 100, 74], [10, 13, 58], [11, 30, 179],
             [12, 32, 215], [12, 33, 161], [12, 61, 198], [13, 38, 48], [13, 65, 222], [14, 22, 1], [15, 70, 222],
             [16, 19, 196], [16, 24, 142], [16, 25, 176], [16, 57, 114], [18, 45, 1], [19, 79, 149], [20, 33, 53],
             [21, 29, 41], [23, 77, 43], [24, 41, 75], [24, 94, 20], [27, 63, 2], [31, 69, 58], [31, 88, 123],
             [31, 88, 146], [33, 61, 27], [35, 62, 190], [35, 81, 116], [37, 97, 81], [38, 78, 99], [39, 51, 125],
             [39, 98, 144], [40, 95, 4], [45, 89, 229], [47, 49, 10], [47, 99, 152], [48, 67, 69], [48, 72, 1],
             [49, 73, 204], [49, 77, 117], [50, 61, 174], [50, 76, 147], [52, 64, 4], [52, 89, 84], [54, 70, 201],
             [57, 76, 47], [58, 61, 215], [58, 98, 57], [61, 95, 190], [66, 71, 34], [66, 99, 53], [67, 74, 9],
             [68, 97, 175], [70, 88, 131], [74, 77, 155], [74, 99, 145], [76, 88, 26], [82, 87, 40], [83, 84, 132],
             [88, 99, 99]]
print(get_skyline(buildings))

buildings = [[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],[20,25,7]]
print(get_skyline(buildings))
