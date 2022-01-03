def calc_drone_mind_energy(route):
    energy_needed = 0
    total_energy = 0
    heights = []
    for coordinates in route:
        heights.append(coordinates[2])

    previous_height = heights[0]
    for i in range(len(heights)):
        if previous_height > heights[i]:
            total_energy += (previous_height - heights[i])
        elif previous_height < heights[i]:
            total_energy -= (heights[i] - previous_height)

        if total_energy < 0:
            energy_needed += abs(total_energy)
            total_energy += energy_needed
        previous_height = heights[i]
    return energy_needed


route = [[0,   2, 10],
         [3,   5,  0],
         [9,  20,  6],
         [10, 12, 15],
         [10, 10,  8] ]
print(calc_drone_mind_energy(route))