import math
def maxPoints(points):
    max_count = 1
    for i in range(len(points)):
        p0 = points[i]
        for j in range(i + 1, len(points)):
            p1 = points[j]
            slope_0_1 = computeSlope(p0, p1)
            count = 2
            for k in range(j + 1, len(points)):
                p2 = points[k]
                slope_0_2 = computeSlope(p0, p2)
                if slope_0_1 == slope_0_2:
                    count += 1
            if count > max_count:
                max_count = count

    return max_count


def computeSlope(p0, p1):
    if p0[0] == p1[0]:
        return math.inf
    return (p1[1] - p0[1]) / (p1[0] - p0[0])


print(maxPoints([[1, 1], [2, 2], [3, 3]]))

