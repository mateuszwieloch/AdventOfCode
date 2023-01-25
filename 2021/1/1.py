# Day 1: Sonar Sweep (https://adventofcode.com/2021/day/1)

nums = []

with open("1.in") as input_file:
    nums = [int(x.strip()) for x in input_file.readlines()]

# Task 1
result = 0
for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        result += 1
print(result)

# Task 2
result = 0
prev_total = sum(nums[0:3])
for i in range(1, len(nums)-2):
    sliding_window_total = sum(nums[i:i+3])
    if sliding_window_total > prev_total:
        result += 1
    prev_total = sliding_window_total
print(result)
