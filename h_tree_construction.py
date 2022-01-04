def draw_h_tree(x, y, length, depth):
    if depth == 0:
        return None
    draw_line(x, y, length, 0)
    draw_line(x - length, y, 0, length)
    draw_line(x + length, y, 0, length)

    draw_h_tree(x - length, y - length, length // 2, depth - 1)
    draw_h_tree(x - length, y + length, length // 2, depth - 1)
    draw_h_tree(x + length, y - length, length // 2, depth - 1)
    draw_h_tree(x + length, y + length, length // 2, depth - 1)


def draw_line(x, y, delta_x, delta_y):
    print("center coordinate " + str((x, y)))
    print("start coordinate " + str((x - delta_x, y - delta_y)))
    print("end coordinate " + str((x + delta_x, y + delta_y)))
    print()


print(draw_h_tree(0, 0, 4, 2))

