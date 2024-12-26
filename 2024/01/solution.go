package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
)

func main() {
	file, _ := os.Open("one.in")
	defer file.Close()

	var leftVals, rightVals []int
	var l, r int
	result := 0

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		_, err := fmt.Sscanf(scanner.Text(), "%d %d", &l, &r)
		if err != nil {
			fmt.Println("Error parsing line of text:", err)
			return
		}
		leftVals = append(leftVals, l)
		rightVals = append(rightVals, r)
	}
	slices.Sort(leftVals)
	slices.Sort(rightVals)
	for i := 0; i < len(leftVals); i++ {
		diff := leftVals[i] - rightVals[i]
		if diff < 0 {
			diff *= -1
		}
		result += diff
	}

	fmt.Println("Part 1 result:", result)

	// PART 2
	rightFreqs := map[int]int{}
	result = 0
	for _, r := range rightVals {
		rightFreqs[r]++
	}
	fmt.Println(rightFreqs)
	for _, l := range leftVals {
		result += l * rightFreqs[l]
	}
	fmt.Println("Part 2 result:", result)
}
