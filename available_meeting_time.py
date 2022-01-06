def available_meeting_time(schedule):
    available = []
    copy = sorted(schedule)
    merge_blocks(copy)
    min_start = 700
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


    return available


def merge_blocks(schedule):
    for i in range(len(schedule)):
        if i < len(schedule) - 1 and schedule[i][0] == schedule[i + 1][0]:
            schedule[i][1] = schedule[i + 1][1]
            schedule.pop(i)


schedule = [[1600, 1630], [600, 730], [800, 920], [800, 900], [1730, 1920]]
print(available_meeting_time(schedule))

schedule = [[1200, 1730], [800, 1000], [1000, 1130]]
print(available_meeting_time(schedule))
