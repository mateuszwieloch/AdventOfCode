package main

import (
	"bufio"
	"fmt"
	"os"
)

type Location struct {
	x, y int
}

type DataPoint struct {
	height         byte
	reachableNines map[Location]bool
	rating         int
}

func (dp *DataPoint) mergeWith(other DataPoint) {
	for nineLocation := range other.reachableNines {
		dp.reachableNines[nineLocation] = true
	}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	topoMap := [][]DataPoint{}
	for scanner.Scan() {
		var row []DataPoint
		y := len(topoMap)
		for x, c := range scanner.Bytes() {
			height := byte(c - '0')
			reachableNines := map[Location]bool{}
			rating := 0
			if height == 9 {
				reachableNines[Location{x, y}] = true
				rating = 1
			}
			row = append(row, DataPoint{height, reachableNines, rating})
		}
		topoMap = append(topoMap, row)
	}

	for height := byte(9); height > 0; height-- {
		for y, row := range topoMap {
			for x, dp := range row {
				if dp.height == height {
					if y > 0 && topoMap[y-1][x].height == dp.height-1 {
						topoMap[y-1][x].mergeWith(dp)
						topoMap[y-1][x].rating += dp.rating
					}
					if y < len(topoMap)-1 && topoMap[y+1][x].height == dp.height-1 {
						topoMap[y+1][x].mergeWith(dp)
						topoMap[y+1][x].rating += dp.rating
					}
					if x > 0 && topoMap[y][x-1].height == dp.height-1 {
						topoMap[y][x-1].mergeWith(dp)
						topoMap[y][x-1].rating += dp.rating
					}
					if x < len(topoMap)-1 && topoMap[y][x+1].height == dp.height-1 {
						topoMap[y][x+1].mergeWith(dp)
						topoMap[y][x+1].rating += dp.rating
					}
				}
			}
		}
	}

	sumOfScores := 0
	sumOfRatings := 0
	for _, row := range topoMap {
		for _, dp := range row {
			if dp.height == 0 {
				score := len(dp.reachableNines)
				sumOfScores += score
				sumOfRatings += dp.rating
			}
		}
	}
	fmt.Println("Part 1 solution:", sumOfScores)
	fmt.Println("Part 2 solution:", sumOfRatings)
}
