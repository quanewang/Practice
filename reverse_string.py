def reverse_string(str):
    n = len(str) - 1
    # reverse the entire string
    for i in range(0, len(str) // 2):
        temp = str[i]
        str[i] = str[n - i]
        str[n - i] = temp

    print(str)
    #end = len(str) - 1

    #for i in range(len(str)).__reversed__():
        #if str[i] == ' ':
            #beg = i + 1
            #for j in range(beg, (end + beg) // 2 + 1):
               # opposite = (end - j) + beg
              #  temp = str[j]
              #  str[j] = str[opposite]
              #  str[opposite] = temp
           # end = i - 1

    beg = 0
    for i in range(len(str)):
        if str[i] == ' ':
            end = i - 1
            for j in range(beg, (end + beg) // 2 + 1):
                opposite = (end - j) + beg
                temp = str[j]
                str[j] = str[opposite]
                str[opposite] = temp
            beg = i + 1

        elif i == len(str) - 1:
            end = i
            for j in range(beg, (end + beg) // 2 + 1):
                opposite = (end - j) + beg
                temp = str[j]
                str[j] = str[opposite]
                str[opposite] = temp

    return str


def reverse_entire_string(str, beg, end):
    pass


print(reverse_string(['g', 'o', ' ', 'w', 'i', 't', 'h', 'o', 'u', 't', ' ', 'w', 'i', 'n', 'd']))
