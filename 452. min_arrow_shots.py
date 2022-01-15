def min_arrow_shots(points):
    sorted_points = sorted(points)
    i = 0
    while i < len(sorted_points) and sorted_points:
        j = i + 1
        interval_1 = sorted_points[i]
        while j < len(sorted_points) and interval_1[0] <= sorted_points[j][0] <= interval_1[1]:
            sorted_points[i][0] = sorted_points[j][0]
            sorted_points[i][1] = min(interval_1[1], sorted_points[j][1])
            sorted_points.pop(j)
        i = j

    return len(sorted_points)


print(min_arrow_shots([[10,16],[2,8],[1,6],[7,12]]))

print(min_arrow_shots([[1,2],[3,4],[5,6],[7,8]]))

print(min_arrow_shots([[1,2],[2,3],[3,4],[4,5]]))
