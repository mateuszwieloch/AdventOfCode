# Task 1
with open("one.in") as input_file:
    result = 0
    left, right = [], []
    while line := input_file.readline().strip():
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()
    for i in range(len(left)):
        result += abs(left[i] - right[i])
    print("Task 1 result:", result)

# Task 2
from collections import defaultdict
with open("one.in") as input_file:
    result = 0
    left, right = [], defaultdict(int)
    while line := input_file.readline().strip():
        l, r = line.split()
        left.append(int(l))
        right[int(r)] += 1
    for v in left:
        result += v * right[v]
    print("Task 2 result:", result)
