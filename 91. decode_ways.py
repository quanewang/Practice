def decode_ways(s):
    count_dict = {}
    return get_ways(s, count_dict)


def get_ways(s, count_dict, i=0):
    sub_str = s[i:len(s)]
    if not sub_str:
        return 1

    if sub_str[0] == "0":
        return 0

    if len(sub_str) == 1:  # 0 case covered by above
        return 1

    count = 0
    if count_dict.get(i + 1) is None:
        new_count = get_ways(s, count_dict, i + 1)
        count_dict.update({i + 1: new_count})
        count = new_count
    else:
        count += count_dict.get(i + 1)
    if int(sub_str[0:2]) <= 26:
        if count_dict.get(i + 2) is None:
            new_count = get_ways(s, count_dict, i + 2)
            count_dict.update({i + 2: new_count})
            count += new_count
        else:
            count += count_dict.get(i + 2)

    return count


print(decode_ways("226"))

print(decode_ways("12"))

print(decode_ways("111111111111111111111111111111111111111111111"))
