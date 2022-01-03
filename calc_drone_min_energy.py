def calc_drone_mind_energy(route):
    energy_needed = 0
    total_energy = 0

    previous_height = route[0][2]
    for _, _, height in route:
        if previous_height > height:
            total_energy += (previous_height - height)
        elif previous_height < height:
            total_energy -= (height - previous_height)

        if total_energy < 0:
            energy_needed += abs(total_energy)
            total_energy += energy_needed
            
        previous_height = height

    return energy_needed


route = [[0,   2, 10],
         [3,   5,  0],
         [9,  20,  6],
         [10, 12, 15],
         [10, 10,  8] ]
print(calc_drone_mind_energy(route))
