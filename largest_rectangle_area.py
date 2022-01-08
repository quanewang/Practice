def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    for i in range(len(heights)):
        last_higher = i
        while stack and heights[i] < heights[stack[len(stack) - 1]]:
            last_higher = stack[len(stack) - 1]
            width = i - stack[len(stack) - 1]
            height = heights[stack.pop(len(stack) - 1)]
            max_area = max(max_area, width * height)
        if last_higher < i:
            heights[last_higher] = heights[i]
            stack.append(last_higher)

        stack.append(i)

    while stack:
        width = len(heights) - stack[len(stack) - 1]
        height = heights[stack.pop(len(stack) - 1)]
        max_area = max(max_area, width * height)

    return max_area


heights = [2, 1, 5, 6, 2, 3]
print(largest_rectangle_area(heights))

heights = [2, 4]
print(largest_rectangle_area(heights))

heights = [2, 1, 2]
print(largest_rectangle_area(heights))
