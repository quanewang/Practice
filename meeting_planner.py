def meeting_planner(slotsA, slotsB, dur):
    i, j = 0, 0
    while i < len(slotsA) and j < len(slotsB):
        a_beg, a_end, b_beg, b_end = slotsA[i][0], slotsA[i][1], slotsB[j][0], slotsB[j][1]
        smallest_end = min(a_end, b_end)
        biggest_beg = max(a_beg, b_beg)
        if a_beg == b_beg:
            if verify_difference(a_beg, smallest_end, dur):
                return [a_beg, a_beg + dur]
        if biggest_beg < smallest_end:
            if verify_difference(biggest_beg, smallest_end, dur):
                return [biggest_beg, biggest_beg + dur]

        if smallest_end == a_end:
            i += 1
        else:
            j += 1
    return []


def verify_difference(beg, end, dur):
    if end - beg >= dur:
        return True
    return False


slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8
print(meeting_planner(slotsA, slotsB, dur))

dur = 12
print(meeting_planner(slotsA, slotsB, dur))

dur = 5
print(meeting_planner(slotsA, slotsB, dur))
