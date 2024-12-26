package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
)

func main() {
	lines := []string{}
	result := 0

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	rows := len(lines)
	cols := len(lines[0])
	xmas_regexp, _ := regexp.Compile("XMAS")
	samx_regexp, _ := regexp.Compile("SAMX")

	// horizontal
	for _, line := range lines {
		result += len(xmas_regexp.FindAllString(line, -1)) + len(samx_regexp.FindAllString(line, -1))
	}
	fmt.Println("Horizontal:", result)

	// vertical down
	for x := 0; x < len(lines[0]); x++ {
		line := []byte{}
		for y := 0; y < len(lines); y++ {
			line = append(line, lines[y][x])
		}
		result += len(xmas_regexp.FindAll(line, -1)) + len(samx_regexp.FindAll(line, -1))
	}
	fmt.Println("Horizontal+V:", result)

	// diagonal right down
	for startX := 0; startX < cols; startX++ {
		line := []byte{}
		for x, y := startX, 0; x < cols && y < rows; {
			line = append(line, lines[y][x])
			x++
			y++
		}
		result += len(xmas_regexp.FindAll(line, -1)) + len(samx_regexp.FindAll(line, -1))
	}
	for startY := 1; startY < rows; startY++ {
		line := []byte{}
		for x, y := 0, startY; x < cols && y < rows; {
			line = append(line, lines[y][x])
			x++
			y++
		}
		result += len(xmas_regexp.FindAll(line, -1)) + len(samx_regexp.FindAll(line, -1))
	}
	// diagonal left down
	for startX := cols - 1; startX >= 0; startX-- {
		line := []byte{}
		for x, y := startX, 0; x >= 0 && y < rows; {
			line = append(line, lines[y][x])
			x--
			y++
		}
		result += len(xmas_regexp.FindAll(line, -1)) + len(samx_regexp.FindAll(line, -1))
	}
	for startY := 1; startY < rows; startY++ {
		line := []byte{}
		for x, y := cols-1, startY; x >= 0 && y < rows; {
			line = append(line, lines[y][x])
			x--
			y++
		}
		result += len(xmas_regexp.FindAll(line, -1)) + len(samx_regexp.FindAll(line, -1))
	}

	fmt.Println("Part 1 result:", result)

	// PART 2
	result = 0
	for x := range cols {
		for y := range rows {
			if lines[y][x] == 'A' {
				if y > 0 && x > 0 && y < rows-1 && x < cols-1 &&
					((lines[y-1][x-1] == 'M' && lines[y+1][x+1] == 'S') || (lines[y-1][x-1] == 'S' && lines[y+1][x+1] == 'M')) &&
					((lines[y-1][x+1] == 'M' && lines[y+1][x-1] == 'S') || (lines[y-1][x+1] == 'S' && lines[y+1][x-1] == 'M')) {
					result += 1
				}
			}
		}
	}
	fmt.Println("Part 2 results:", result)
}
