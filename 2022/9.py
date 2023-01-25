# Day 9: Rope Bridge (https://adventofcode.com/2022/day/9)

# Task 1
def knots_too_far(leader, follower):
    dirV = (leader[0] - follower[0], leader[1] - follower[1])
    return (abs(dirV[0]) >= 2 or abs(dirV[1]) >= 2)


with open("9.in") as input_file:
    visited:set[tuple[int,int]] = {(0,0)} # (x,y)
    head:tuple[int,int] = (0,0)
    tail:tuple[int,int] = (0,0)

    while line := input_file.readline():
        dir, dist = line.split()
        dist = int(dist)

        if dir == 'R':
            head = (head[0] + dist, head[1])
        elif dir == 'L':
            head = (head[0] - dist, head[1])
        elif dir == 'U':
            head = (head[0], head[1] - dist)
        else:
            head = (head[0], head[1] + dist)

        while knots_too_far(head, tail):
            dirV = (head[0] - tail[0], head[1] - tail[1])
            normalizedV = (dirV[0] // abs(dirV[0]) if dirV[0] != 0 else 0,
                           dirV[1] // abs(dirV[1]) if dirV[1] != 0 else 0)
            tail = (tail[0]+normalizedV[0], tail[1]+normalizedV[1])
            visited.add(tail)
    print("Task 1 result:", len(visited))


# Task 2
with open("9.in") as input_file:
    visited:set[tuple[int,int]] = {(0,0)} # (x,y)
    knots:list[tuple[int,int]] = [(0,0) for _ in range(10)]

    while line := input_file.readline().strip():
        print(line)
        dir, dist = line.split()
        dist = int(dist)

        if dir == 'R':
            knots[0] = (knots[0][0] + dist, knots[0][1])
        elif dir == 'L':
            knots[0] = (knots[0][0] - dist, knots[0][1])
        elif dir == 'U':
            knots[0] = (knots[0][0], knots[0][1] - dist)
        else:
            knots[0] = (knots[0][0], knots[0][1] + dist)

        for f_idx in range(1, len(knots)):
            leader = knots[f_idx-1]
            follower = knots[f_idx]
            while knots_too_far(leader, follower):
                dirV = (leader[0] - follower[0], leader[1] - follower[1])
                normalizedV = (dirV[0] // abs(dirV[0]) if dirV[0] != 0 else 0,
                            dirV[1] // abs(dirV[1]) if dirV[1] != 0 else 0)
                knots[f_idx] = (follower[0]+normalizedV[0], follower[1]+normalizedV[1])
                follower = knots[f_idx]
                if f_idx == 9:
                    visited.add(follower)
        print(knots)
    print("Task 2 result:", len(visited))
