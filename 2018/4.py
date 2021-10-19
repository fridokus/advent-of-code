#!/usr/bin/env python3

import calendar as ca
import numpy as np
from datetime import datetime as dt

name = input("Specify name (which in-file to be used):")
file_name = "4_%s.in" % name if name else "4.in"
# Sort watchlist
with open(file_name, "r") as f:
    watchlist = []
    for line in f.readlines():
        watchlist.append(line.replace("[", "").replace("]", "").strip())
watchlist = sorted(watchlist)

# Create sleep stats for guards based on watchlist
hour_in_seconds = 60 * 60
guard_sleep_stats = dict()
for line in watchlist:
    elements = line.split()
    time_stamp = elements[1]
    event = elements[2]
    if event == "Guard":
        guard = elements[3]
        if guard not in guard_sleep_stats:
            guard_sleep_stats[guard] = np.zeros((1, 60), int)
    elif event == "wakes":
        end_minute = int(time_stamp[-2:])
        guard_sleep_stats[guard][0, start_minute:end_minute] += 1
    elif event == "falls":
        start_minute = int(time_stamp[-2:])

# Summarize data from stats
total_sleep_stats = dict()
favorite_minute = dict()
for guard in guard_sleep_stats:
    total_sleep_stats[guard] = np.sum(guard_sleep_stats[guard])
    favorite_minute[guard] = [np.max(guard_sleep_stats[guard]), np.argmax(guard_sleep_stats[guard])]
# Strategy 1: Most asleep guard's most asleep minute
most_asleep_guard = max(total_sleep_stats, key = total_sleep_stats.get)
most_slept_minute = np.argmax(guard_sleep_stats[most_asleep_guard])
answer_one = int(most_asleep_guard.strip("#")) * most_slept_minute
# Strategy 2: Most asleep minute of any guard
max_favorite_minute = max(favorite_minute.values())[1]
guard_max_favorite_minute = max(favorite_minute, key=favorite_minute.get).strip("#")
answer_two = int(guard_max_favorite_minute) * max_favorite_minute

# Print the summary
print("AoC 2018 Day 4: Repose Record")
print("  Part 1:")
print("\tStrategy 1:")
print("\tMost asleep guard is:                 ", most_asleep_guard)
print("\tMost slept minute is of that guard is:", most_slept_minute)
print("\tAnswer to strategy 1 (guard * minute):", answer_one)
print("  Part 2:")
print("\tStrategy 2:")
print("\tMost slept minute of any guard is:    ", max_favorite_minute)
print("\tThe corresponding guard:              ", guard_max_favorite_minute)
print("\tAnswer to strategy 2 (guard * minute):", answer_two)
