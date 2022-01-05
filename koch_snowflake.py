def koch_snowflake(length=1, depth=0):
    i = 0
    while i < 3:
        draw_helper(length, depth)
        print("turn 120 degrees right")
        i += 1


def draw_helper(length, depth):
    if depth == 0:
        print("draw(" + str(length // 3) + ")")
        return
    print()
    draw_helper(length, depth - 1)
    print("turn 60 degrees left")
    draw_helper(length, depth - 1)
    print("turn 120 degrees right")
    draw_helper(length, depth - 1)
    print("turn 60 degrees left")
    draw_helper(length, depth - 1)
    print()
    return



koch_snowflake(9, 2)