package main

import (
	"bufio"
	"fmt"
	"os"
)

type Location struct {
	x, y int
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	antennas := map[byte][]Location{}
	antinodes := map[Location]bool{}
	antinodes2 := map[Location]bool{}

	var row, col int
	var b byte

	for row = 0; scanner.Scan(); row++ {
		for col, b = range scanner.Bytes() {
			if b != '.' {
				antennas[b] = append(antennas[b], Location{col, row})
			}
		}
	}
	rows := row
	cols := col + 1

	// part 1
	for _, locs := range antennas {
		for i := 0; i < len(locs)-1; i++ {
			for j := i + 1; j < len(locs); j++ {
				dx := locs[j].x - locs[i].x
				dy := locs[j].y - locs[i].y
				a1x := locs[i].x - dx
				a1y := locs[i].y - dy
				if a1x >= 0 && a1x < cols && a1y >= 0 && a1y < rows {
					antinodes[Location{a1x, a1y}] = true
				}
				a2x := locs[j].x + dx
				a2y := locs[j].y + dy
				if a2x >= 0 && a2x < cols && a2y >= 0 && a2y < rows {
					antinodes[Location{a2x, a2y}] = true
				}
			}
		}
	}

	// part 2
	for _, locs := range antennas {
		for i := 0; i < len(locs)-1; i++ {
			for j := i + 1; j < len(locs); j++ {
				dx := locs[j].x - locs[i].x
				dy := locs[j].y - locs[i].y
				x := locs[i].x
				y := locs[i].y
				for x >= 0 && x < cols && y >= 0 && y < rows {
					antinodes2[Location{x, y}] = true
					x += dx
					y += dy
				}
				x = locs[i].x
				y = locs[i].y
				for x >= 0 && x < cols && y >= 0 && y < rows {
					antinodes2[Location{x, y}] = true
					x -= dx
					y -= dy
				}
			}
		}
	}
	fmt.Println("Part 1 solution:", len(antinodes))
	fmt.Println("Part 2 solution:", len(antinodes2))
}
