def available_meeting_time(schedule):
    available = []
    schedule = sorted(schedule)
    return available


schedule = [[1600, 1630], [600, 730], [800, 920], [800, 900], [1730, 1920]]
print(available_meeting_time(schedule))
