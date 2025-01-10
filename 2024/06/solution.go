package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"

	mapset "github.com/deckarep/golang-set/v2"
)

type Position struct {
	x, y int
}

func (p Position) IsOutOfBounds(floor *Floor) bool {
	return p.x < 0 || p.y < 0 || p.y >= len(*floor) || p.x >= len((*floor)[0])
}

func (p Position) Add(other Position) Position {
	return Position{p.x + other.x, p.y + other.y}
}

type Visit struct {
	pos Position
	dir Position
}

type Floor [][]byte

func (f Floor) At(pos Position) byte {
	return f[pos.y][pos.x]
}

func (f Floor) IsObstacleAt(pos Position) bool {
	return f[pos.y][pos.x] == '#'
}

func (f Floor) FindGuardsStartingPosition() Position {
	for y, row := range f {
		for x, tile := range row {
			if tile == '^' {
				return Position{x, y}
			}
		}
	}
	panic("Unable to find guard's starting position")
}

func TurnRight(dir Position) Position {
	if dir.y == -1 {
		return Position{1, 0}
	} else if dir.x == 1 {
		return Position{0, 1}
	} else if dir.y == 1 {
		return Position{-1, 0}
	} else { //if dir.x == -1
		return Position{0, -1}
	}
}

func CloneFloor(floor Floor) Floor {
	new_floor := Floor{}
	for _, row := range floor {
		new_floor = append(new_floor, slices.Clone(row))
	}
	return new_floor
}

func main() {
	floor := Floor{}
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		floor = append(floor, slices.Clone(scanner.Bytes()))
	}

	startingPos := floor.FindGuardsStartingPosition()
	visitedTiles := mapset.NewSet[Position]()

	// Part 1
	part1 := func() {
		pos := startingPos
		dir := Position{0, -1}
	outer:
		for !pos.IsOutOfBounds(&floor) {
			visitedTiles.Add(pos)

			for {
				nextPos := pos.Add(dir)
				if nextPos.IsOutOfBounds(&floor) {
					break outer
				}
				if floor.IsObstacleAt(nextPos) {
					dir = TurnRight(dir)
				} else {
					pos = nextPos
					break
				}
			}
		}

		fmt.Println("Part 1 result:", visitedTiles.Cardinality())
	}
	part1()

	// Part 2
	numLoops := 0
	for tile := range visitedTiles.Iter() {
		floor2 := CloneFloor(floor)
		floor2[tile.y][tile.x] = '#'

		pos := startingPos
		dir := Position{0, -1}
		visitedTilesAndDirs := mapset.NewSet[Visit]()

	loopSearch:
		for !pos.IsOutOfBounds(&floor2) {
			visitedTilesAndDirs.Add(Visit{pos, dir})

			for {
				nextPos := pos.Add(dir)
				if nextPos.IsOutOfBounds(&floor2) {
					break loopSearch
				}
				if floor2.IsObstacleAt(nextPos) {
					dir = TurnRight(dir)
				} else {
					if visitedTilesAndDirs.Contains(Visit{nextPos, dir}) {
						numLoops++
						break loopSearch
					}
					pos = nextPos
					break
				}
			}
		}
	}

	fmt.Println("Part 2 result:", numLoops)
}
