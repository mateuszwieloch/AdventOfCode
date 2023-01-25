# Day 4: Camp Cleanup (https://adventofcode.com/2022/day/4)

def range_contains(range1, range2):
    return range2[0] >= range1[0] and range2[1] <= range1[1]


def ranges_overlap(range1, range2):
    return (
        (range1[0] >= range2[0] and range1[0] <= range2[1])
        or
        (range1[1] >= range2[0] and range1[1] <= range2[1])
        or
        (range2[0] >= range1[0] and range2[0] <= range1[1])
        or
        (range2[1] >= range1[0] and range2[1] <= range1[1])
    )


# Task 1: how many ranges fully contain the other
result = 0
with open("4.in") as f:
    while line := f.readline().strip():
        raw_range1, raw_range2 = line.split(",")
        range1 = list(map(int, raw_range1.split("-")))
        range2 = list(map(int, raw_range2.split("-")))
        result += int(range_contains(range1, range2) or range_contains(range2, range1))
        print(f"{range1=} {range2=} {result=}")
print("Task 1 result:", result)

# Task 2
result = 0
with open("4.in") as f:
    while line := f.readline().strip():
        raw_range1, raw_range2 = line.split(",")
        range1 = list(map(int, raw_range1.split("-")))
        range2 = list(map(int, raw_range2.split("-")))
        result += int(ranges_overlap(range1, range2))
print("Task 2 result:", result)
