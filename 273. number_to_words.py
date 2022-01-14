def number_to_words(num):
    magnitude_dict = {0: "",
                      1: " Thousand ",
                      2: " Million ",
                      3: " Billion "}

    digit_dict = {0: ["Zero"],
                  1: ["One"],
                  2: ["Two", "Twenty"],
                  3: ["Three", "Thirty"],
                  4: ["Four", "Forty"],
                  5: ["Five", "Fifty"],
                  6: ["Six", "Sixty"],
                  7: ["Seven", "Seventy"],
                  8: ["Eight", "Eighty"],
                  9: ["Nine", "Ninety"]}

    teen_dict = {10: "Ten",
                 11: "Eleven",
                 12: "Twelve",
                 13: "Thirteen",
                 14: "Fourteen",
                 15: "Fifteen",
                 16: "Sixteen",
                 17: "Seventeen",
                 18: "Eighteen",
                 19: "Nineteen"}

    count = 0
    result = ""
    s = str(num)
    while s:
        if len(s) < 3:
            sub = get_substring(s, digit_dict, teen_dict)
            if sub and sub[len(sub) - 1] == " ":
                sub = sub[0:len(sub) - 1]

            result = sub + magnitude_dict.get(count % 4) + result

            if result[len(result) - 1] == " ":
                return result[0:len(result) - 1]
            return result
        else:
            sub = get_substring(s[len(s) - 3:len(s)], digit_dict, teen_dict)
            if sub:
                if sub[len(sub) - 1] == " ":
                    sub = sub[0:len(sub) - 1]
                sub = sub + magnitude_dict.get(count % 4)

            result = sub + result

            if result and result[len(result) - 1] == " ":
                result = result[0:len(result) - 1]
        s = s[0:len(s) - 3]
        count += 1
    if result[len(result) - 1] == " ":
        return result[0:len(result) - 1]
    return result


def get_substring(s, digit_dict, teen_dict):
    if len(s) == 1:
        return digit_dict.get(int(s[0]))[0]

    if len(s) == 2 and s[0] == "1":
        return teen_dict.get(int(s))

    result = ""
    count = 0
    for i in range(len(s)).__reversed__():
        sub = ""
        if s[i] == "0" or (count == 0 and s[i - 1] == "1"):
            pass
        elif count == 0 or count == 2:
            sub = digit_dict.get(int(s[i]))[0]
            if count == 2:
                sub += " Hundred "
        elif count == 1:
            if s[i] == "1":
                sub = teen_dict.get(int(s[i:i + 2])) + " "
            else:
                sub = digit_dict.get(int(s[i]))[1] + " "

        result = sub + result
        count += 1

    return result


print(number_to_words(123))

print(number_to_words(12345))

print(number_to_words(1234567))

print(number_to_words(0))

print(number_to_words(21))

print(number_to_words(110))

print(number_to_words(111))

print(number_to_words(50868))

print(number_to_words(1000))

print(number_to_words(1000000))
