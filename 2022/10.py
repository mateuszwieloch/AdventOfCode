# Day 10: Cathode-Ray Tube (https://adventofcode.com/2022/day/10)

# Task 1
with open("10.in") as input_file:
    delay1:int = 0
    delay2:int = 0
    X:int = 1
    cycle = 0
    result = 0
    for line in input_file.read().strip().split("\n"):
        if line == 'noop':
            cycle += 1
            if cycle in {20, 60, 100, 140, 180, 220}:
                result += cycle * X
        else:
            cycle += 1
            if cycle in {20, 60, 100, 140, 180, 220}:
                result += cycle * X
            cycle += 1
            if cycle in {20, 60, 100, 140, 180, 220}:
                result += cycle * X
            X += int(line.split()[1])
        # print(f"After {cycle=} {X=}")
    print("Task 1 result:", result)
