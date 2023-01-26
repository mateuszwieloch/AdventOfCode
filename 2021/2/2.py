with open("2.in") as input_file:
    hor = 0
    depth = 0
    for line in input_file:
        dir, dist = line.strip().split()
        dist = int(dist)
        if dir == 'forward':
            hor += dist
        elif dir == 'down':
            depth += dist
        else:
            depth -= dist
    print(hor*depth)

with open("2.in") as input_file:
    aim = 0
    hor = 0
    depth = 0
    for line in input_file:
        dir, dist = line.strip().split()
        dist = int(dist)
        if dir == 'down':
            aim += dist
        elif dir == 'up':
            aim -= dist
        else:
            hor += dist
            depth += aim * dist
    print(hor*depth)
