with open("7.in") as input_file:
    positions = [int(p) for p in input_file.read().strip().split(",")]
    positions.sort()
    align_to = positions[len(positions) // 2]
    fuel = 0
    for p in positions:
        fuel += abs(align_to-p)
    print(f"Fuel needed {fuel}")


# Task 2
with open("7.in") as input_file:
    positions = [int(p) for p in input_file.read().strip().split(",")]
    min_pos = min(positions)
    max_pos = max(positions)
    minfuel = 999999999999

    for pos in range(min_pos, max_pos+1):
        fuel = 0
        for p in positions:
            dist = abs(p-pos)
            fuel += dist*(1+dist)//2
        minfuel = min(minfuel, fuel)

    print(minfuel)
