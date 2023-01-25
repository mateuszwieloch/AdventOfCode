# Day 1: Calorie Counting (https://adventofcode.com/2022/day/1)
import heapq

# Task 1: print sum of calories in a group with most calories
max_calories_in_group = 0
with open("1.in") as f:
    for raw_calorie_group in f.read().strip().split("\n\n"):
        calories_in_group = sum([int(x) for x in raw_calorie_group.split("\n")])
        if calories_in_group > max_calories_in_group:
            max_calories_in_group = calories_in_group
print("Task 1 result:", max_calories_in_group)


# Task 2: print sum of calories in 3 groups with most calories
calories = []
with open("1.in") as f:
    for raw_calorie_group in f.read().strip().split("\n\n"):
        calories_in_group = sum([int(x) for x in raw_calorie_group.split("\n")])
        calories.append(calories_in_group)
heapq.heapify(calories)
print("Task 2 result:", sum(heapq.nlargest(3, calories)))
