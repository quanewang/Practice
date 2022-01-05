def koch_snowflake(length=1, depth=0):
    i = 0
    count = 0
    while i < 3:
        count += draw_helper(length, depth)
        turn(120, "right")
        i += 1
    return count // 4


def draw_helper(length, depth):
    count = 0
    if depth == 0:
        print("draw(" + str(length // 3) + ")")
        return count + 1
    print()
    count += draw_helper(length, depth - 1)
    turn(60, "left")
    count += draw_helper(length, depth - 1)
    turn(120, "right")
    count += draw_helper(length, depth - 1)
    turn(60, "left")
    count += draw_helper(length, depth - 1)
    print()
    return count


def turn(degrees, direction):
    print("turn " + str(degrees) + " degrees " + direction)


print(koch_snowflake(9, 3))