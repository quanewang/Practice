def count_ones(n, unit_place=0, running_sum=0):
    if n == 0:
        return 0
    digit = n % 10

    count = n // 10 * pow(10, unit_place)

    if digit > 1:
        count += 1 * pow(10, unit_place)

    if digit == 1:
        count += running_sum + 1

    running_sum += digit * pow(10, unit_place)
    unit_place += 1
    return count + count_ones(n // 10, unit_place, running_sum)


print(count_ones(6189))
print(count_ones(6089))
print(count_ones(100))
print(count_ones(13))

