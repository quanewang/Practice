def count_and_say(n: int) -> str:
    if n == 1:
        return "1"
    digit_string = count_and_say(n - 1)
    count_say = ""
    i = 0
    while i < len(digit_string):
        count = 1
        for j in range(i + 1, len(digit_string)):
            if digit_string[i] != digit_string[j]:
                break
            else:
                count += 1
        count_say += str(count)
        count_say += digit_string[i]
        i += count
    return count_say


print(count_and_say(1))
print(count_and_say(2))
print(count_and_say(3))
print(count_and_say(4))
