wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
def bubble_sort_1(l):
    start = len(wakeup_times) - 1
    while start:
        for time in range(1, len(wakeup_times)):
            prev_time, current_time = wakeup_times[time-1], wakeup_times[time]
            if prev_time > current_time:
                wakeup_times[time-1], wakeup_times[time] = current_time, prev_time
        start -= 1
    return wakeup_times

print(bubble_sort_1(wakeup_times))
