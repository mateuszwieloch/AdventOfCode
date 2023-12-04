import math
import re


# Task 1
with open("one.in") as f:
    lines = f.read().strip().split("\n")

score = 0
for line in lines:
    _, winning_numbers, numbers_you_have = re.split(r":|\|", line)
    winning_numbers = {int(num) for num in winning_numbers.split()}
    numbers_you_have = {int(num) for num in numbers_you_have.split()}
    num_of_matches = len(winning_numbers & numbers_you_have)
    if num_of_matches >= 1:
        score += math.pow(2, num_of_matches-1)
print(int(score))


# Task 2
num_of_cards = [1] * len(lines)
for idx, line in enumerate(lines):
    _, winning_numbers, numbers_you_have = re.split(r":|\|", line)
    winning_numbers = {int(num) for num in winning_numbers.split()}
    numbers_you_have = {int(num) for num in numbers_you_have.split()}
    num_of_matches = len(winning_numbers & numbers_you_have)
    for i in range(num_of_matches):
        num_of_cards[idx+i+1] += num_of_cards[idx]

print(sum(num_of_cards))

