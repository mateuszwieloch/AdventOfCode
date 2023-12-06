import math

with open("input") as f:
    lines = f.read().strip().split("\n")


# Task 1
race_times = [int(time) for time in lines[0].split(":")[1].split()]
record_distances = [int(dist) for dist in lines[1].split(":")[1].split()]

num_ways_to_win = [0] * len(race_times)

for race, (race_time, record_dist) in enumerate(zip(race_times, record_distances)):
    for hold_time in range(1, race_time):
        remaining_time = race_time - hold_time
        dist = remaining_time * hold_time
        if dist > record_dist:
            num_ways_to_win[race] += 1

print(math.prod(num_ways_to_win))


# Task 2 (brute force, but works just fine)
race_time = int("".join(lines[0].split(":")[1].split()))
record_dist = int("".join(lines[1].split(":")[1].split()))
num_ways_to_win = 0

for hold_time in range(1, race_time):
    remaining_time = race_time - hold_time
    dist = remaining_time * hold_time
    if dist > record_dist:
        num_ways_to_win += 1

print(num_ways_to_win)
