# Day 6: Tuning Trouble (https://adventofcode.com/2022/day/6)


# Task 1
w ith open("6.in") as f:
    contents = f.read()
    # contents = "abcabcd"
    for idx in range(3, len(contents)):
        S = set(contents[idx-3:idx+1])
        # print(f"{S=}")
        if len(S) == 4:
            print("Task 1 result:", idx+1)
            break

# Task 2
with open("6.in") as f:
    contents = f.read()
    for idx in range(13, len(contents)):
        S = set(contents[idx-13:idx+1])
        # print(f"{S=}")
        if len(S) == 14:
            print("Task 2 result:", idx+1)
            break
