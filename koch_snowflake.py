def koch_snowflake(length=1, depth=0):
    i = 0
    count = 0
    while i < 3:
        count += draw_helper(length, depth)
        print("turn 120 degrees right")
        i += 1
    return count // 4

def draw_helper(length, depth):
    count = 0
    if depth == 0:
        print("draw(" + str(length // 3) + ")")
        return count + 1
    print()
    count += draw_helper(length, depth - 1)
    print("turn 60 degrees left")
    count += draw_helper(length, depth - 1)
    print("turn 120 degrees right")
    count += draw_helper(length, depth - 1)
    print("turn 60 degrees left")
    count += draw_helper(length, depth - 1)
    print()
    return count



print(koch_snowflake(9, 3))