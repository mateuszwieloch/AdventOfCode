# Day 15: Beacon Exclusion Zone (https://adventofcode.com/2022/day/15)

import sys

# Task 1
with open("15.in") as input_file:
    ry = 2000000
    rangesOnX = []
    beaconsOnX = set()
    while line := input_file.readline().strip():
        _, _, sx, sy, _, _, _, _, bx, by = line.split()
        sx = int(sx.split('=')[1][:-1])
        sy = int(sy.split('=')[1][:-1])
        bx = int(bx.split('=')[1][:-1])
        by = int(by.split('=')[1])
        distToBeacon = abs(bx - sx) + abs(by - sy)
        distToRow = abs(ry - sy)
        if distToBeacon >= distToRow:
            rangesOnX.append( (sx-(distToBeacon-distToRow), sx+(distToBeacon-distToRow)) )
        if by == ry:
            beaconsOnX.add(bx)
    rangesOnX.sort()
    i = 0
    while i+1 < len(rangesOnX):
        if rangesOnX[i][1] >= rangesOnX[i+1][0]:
            maxEnd = max(rangesOnX[i][1], rangesOnX[i+1][1])
            # merge
            rangesOnX[i:i+2] = [(rangesOnX[i][0], maxEnd)]
        else:
            i += 1

    beaconsOnX = [b for b in beaconsOnX if any(r[0] <= b <= r[1] for r in rangesOnX)]
    sumOfRangeSizes = sum([r[1]-r[0]+1 for r in rangesOnX])
    print("Task 1 result", sumOfRangeSizes - len(beaconsOnX))


with open("15.in") as input_file:
    sensors = []
    beacons = {}
    while line := input_file.readline().strip():
        _, _, sx, sy, _, _, _, _, bx, by = line.split()
        sx = int(sx.split('=')[1][:-1])
        sy = int(sy.split('=')[1][:-1])
        bx = int(bx.split('=')[1][:-1])
        by = int(by.split('=')[1])
        distToBeacon = abs(bx - sx) + abs(by - sy)
        sensors.append((sx, sy, distToBeacon))
        if not by in beacons:
            beacons[by] = {bx}
        else:
            beacons[by].add(bx)

    print(sensors)
    for y in range(0, 4000001):
        rangesOnX = []

        for sx, sy, dist in sensors:
            distToRow = abs(y - sy)
            if dist >= distToRow:
                rangesOnX.append( (sx-(dist-distToRow), sx+(dist-distToRow)) )

        rangesOnX.sort()
        i = 0
        while i+1 < len(rangesOnX):
            if rangesOnX[i][1] >= rangesOnX[i+1][0]:
                maxEnd = max(rangesOnX[i][1], rangesOnX[i+1][1])
                # merge
                rangesOnX[i:i+2] = [(rangesOnX[i][0], maxEnd)]
            else:
                i += 1
        if len(rangesOnX) > 1:
            print("Task 2 result", (rangesOnX[0][1]+1)*4000000 + y)
            sys.exit(0)
        if y % 100000 == 0:
            print('.', end='')

    # beaconsOnX = [b for b in beaconsOnX if any(r[0] <= b <= r[1] for r in rangesOnX)]
    # sumOfRangeSizes = sum([r[1]-r[0]+1 for r in rangesOnX])
    # print("Task 1 result", sumOfRangeSizes - len(beaconsOnX))
