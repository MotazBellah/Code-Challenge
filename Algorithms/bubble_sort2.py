# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

def bubble_sort_2(l):
    start = len(sleep_times) - 1
    while start:
        for time in range(1, len(sleep_times)):
            prev_time, current_time = sleep_times[time-1], sleep_times[time]

            if prev_time[0] < current_time[0]:
                sleep_times[time-1], sleep_times[time] = current_time, prev_time

            elif prev_time[0] == current_time[0]:
                if prev_time[1] < current_time[1]:
                    sleep_times[time-1], sleep_times[time] = current_time, prev_time
                    
            else:
                continue

        start -= 1
    return sleep_times

print(bubble_sort_2(sleep_times))
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")
