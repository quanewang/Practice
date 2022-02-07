def singleNumber(nums):
    bin_result = [0]

    for num in nums:
        binary = get_binary(num)

        bin_result = xor(bin_result, binary)

    result = 0
    power = 1
    for i in range(len(bin_result)):
        if bin_result[i]:
            result += power

        power *= 2

    return result


def get_binary(num):
    bin_list = []
    while num != 0:
        bin_list.append(num % 2)
        num //= 2

    return bin_list


def xor(num1, num2):

    if len(num1) > len(num2):  # guarantees num1 is smaller
        temp = num1
        num1 = num2
        num2 = temp

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


print(singleNumber([4, 1, 2, 1, 2]))
print(singleNumber([1, 2, 1, 65, 2]))
print(singleNumber([65]))

