# Day 5: Supply Stacks (https://adventofcode.com/2022/day/5)

# Task 1
stacks = [[] for i in range(9)]
raw_lines = []
with open("5.in") as f:
    for i in range(8):
        raw_lines.append(f.readline())

    for i in reversed(range(8)):
        for idx, char in enumerate(raw_lines[i]):
            if (idx % 4 == 1) and char.isalpha():
                stacks[idx//4].append(char)

    f.readline()
    f.readline()

    while line := f.readline().strip():
        _, count, _, src, _, dst = line.split()
        count, src, dst = int(count), int(src)-1, int(dst)-1
        for _ in range(count):
            stacks[dst].append(stacks[src].pop())

    print("Task 1 result:", end="")
    for stack in stacks:
        if stack:
            print(stack.pop(), end="")
    print()


# Task 2
stacks = [[] for i in range(9)]
raw_lines = []
with open("5.in") as f:
    for i in range(8):
        raw_lines.append(f.readline())

    for i in reversed(range(8)):
        for idx, char in enumerate(raw_lines[i]):
            if (idx % 4 == 1) and char.isalpha():
                stacks[idx//4].append(char)

    f.readline()
    f.readline()

    while line := f.readline().strip():
        _, count, _, src, _, dst = line.split()
        count, src, dst = int(count), int(src)-1, int(dst)-1
        stacks[dst].extend(stacks[src][-count:])
        del stacks[src][-count:]

    print("Task 2 result:", end="")
    for stack in stacks:
        if stack:
            print(stack.pop(), end="")
    print()
