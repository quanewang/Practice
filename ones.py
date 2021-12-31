def count_ones(n, unit_place=0, digits=[]):
    if n == 0:
        return 0
    digit = n % 10

    count = n // 10 * pow(10, unit_place)

    if digit > 1:
        count += 1 * pow(10, unit_place)

    if digit == 1:
        places = unit_place - 1
        dig = 0
        for i in range(unit_place):
            dig += digits[i] * pow(10, places)
            places -= 1
        count += dig + 1


    digits.insert(0, digit)
    unit_place += 1
    return count + count_ones(n // 10, unit_place, digits)


print(count_ones(6189))
print(count_ones(6089))
print(count_ones(100))
print(count_ones(13))

