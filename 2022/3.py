# Day 3: Rucksack Reorganization (https://adventofcode.com/2022/day/3)

def priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


# Task 1
sum_of_dups_priorities = 0
with open("3.in") as f:
    while line := f.readline().strip():
        middle = len(line)//2
        s1 = set(line[:middle])
        s2 = set(line[middle:])
        element = (s1 & s2).pop()
        sum_of_dups_priorities += priority(element)
print("Task 1 result:", sum_of_dups_priorities)


# Task 2
sum_of_badge_priorities = 0
with open("3.in") as f:
    while True:
        line1 = set(f.readline().strip())
        line2 = set(f.readline().strip())
        line3 = set(f.readline().strip())
        if not line1 or not line2 or not line3:
            break
        common = (line1 & line2 & line3).pop()
        sum_of_badge_priorities += priority(common)

print("Task 2 result:", sum_of_badge_priorities)
