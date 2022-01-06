def max_area(height):
    left = 0
    right = len(height) - 1
    maximum_area = 0
    while left < right:
        if height[left] < height[right]:
            current_area = height[left] * (right - left)
            left += 1
        else:
            current_area = height[right] * (right - left)
            right -= 1
        if current_area > maximum_area:
            maximum_area = current_area
    return maximum_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))

height = [1, 1]
print(max_area(height))

height = [0, 1]
print(max_area(height))
