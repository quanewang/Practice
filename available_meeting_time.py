def available_meeting_time(schedule):
    available = []
    copy = sorted(schedule)
    copy = merge_blocks(copy)

    if copy[0][0] > 700:
        available.append([700, copy[0][0]])

    for i in range(len(copy)):
        block = copy[i]
        if i < len(copy) - 1:
            next_block = copy[i + 1]
            if block[1] >= next_block[0]:
                i += 1
            else:
                available.append([block[1], next_block[0]])
        else:
            if block[1] < 1800:
                available.append([block[1], 1800])
    return available


def merge_blocks(schedule):
    copy = []
    previous_block = None
    for block in schedule:
        if previous_block is None:
            previous_block = block
        if previous_block[0] == block[0] or previous_block[1] == block[0]:
            block[0] = previous_block[0]
            previous_block = block
        else:
            copy.append(previous_block)
            previous_block = block
    copy.append(previous_block)
    return copy


schedule = [[1600, 1630], [600, 730], [800, 920], [800, 900], [1730, 1920]]
print(available_meeting_time(schedule))
print(merge_blocks(sorted(schedule)))


schedule = [[1200, 1730], [800, 1000], [1000, 1130]]
print(merge_blocks(sorted(schedule)))
print(available_meeting_time(schedule))

schedule = [[1200, 1730]]
print(merge_blocks(sorted(schedule)))
print(available_meeting_time(schedule))
