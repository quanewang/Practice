def singleNumber(nums):
    bin_result = [0]

    for num in nums:
        if num >= 0:
            binary = get_binary_positive(num)
            binary.append(0)
        else:
            binary = get_binary_negative(num)
            binary.append(1)

        bin_result = xor(bin_result, binary)

    result = 0
    power = 1
    if bin_result[len(bin_result) - 1] == 0:
        for i in range(len(bin_result)):  # convert back to decimal
            if bin_result[i]:
                result += power

            power *= 2
    else:
        for i in range(len(bin_result)):  # convert back to decimal
            if not bin_result[i]:
                result += power

            power *= 2
        result += 1
        result *= -1

    return result


def get_binary_positive(num):
    bit_list = []
    while num != 0:
        bit_list.append(num % 2)
        num //= 2
    return bit_list


def get_binary_negative(num):
    bit_list = get_binary_positive(num * -1)
    for i in range(len(bit_list)):
        if bit_list[i]:
            bit_list[i] = 0
        else:
            bit_list[i] = 1

    i = 0
    while bit_list[i] == 1:
        bit_list[i] = 0
        i += 1
    bit_list[i] = 1
    return bit_list


def xor(num1, num2):

    if len(num1) > len(num2):  # guarantees num1 is smaller
        temp = num1
        num1 = num2
        num2 = temp

    sign_bit = num1[len(num1) - 1]
    for i in range(len(num2) - len(num1)):  # fill smaller bit with sign bits
        num1.append(sign_bit)
    i = 0
    while i < len(num1):  # xor num1 elements with num2 (implicit merge)
        bit1 = num1[i]
        bit2 = num2[i]
        if bit1 != bit2:
            num2[i] = 1
        else:
            num2[i] = 0
        i += 1

    return num2


print(singleNumber([-1, 1, 1]))
print(singleNumber([65, 1, 1, -4, 65]))
print(singleNumber([1, 4, 2, 1, 2]))

