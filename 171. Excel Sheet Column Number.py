def titleToNumber(column_title: str) -> int:
    if not column_title:
        return 0

    char_digit = column_title[len(column_title) - 1]

    return (26 - (ord("Z") - ord(char_digit))) + 26 * titleToNumber(column_title[0:len(column_title) - 1])


print(titleToNumber("AA"))

