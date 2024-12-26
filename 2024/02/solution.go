package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func abs(a int) int {
	if a >= 0 {
		return a
	} else {
		return -a
	}
}

// Sequence is safe if:
// 1. It's either always increasing or always decreasing
// 2. Absolute difference between subsequent numbers is 1, 2 or 3.
func isSequenceSafe(nums []int) bool {
	increasing := nums[0] < nums[1]
	for i := 0; i < len(nums)-1; i++ {
		if increasing && nums[i] > nums[i+1] {
			return false
		}
		if !increasing && nums[i] < nums[i+1] {
			return false
		}
		diff := abs(nums[i] - nums[i+1])
		if diff < 1 || diff > 3 {
			return false
		}
	}
	return true
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	lines := []string{}

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	correctCount := 0
	for _, line := range lines {
		parts := strings.Fields(line)
		numbers := []int{}
		for _, part := range parts {
			num, _ := strconv.Atoi(part)
			numbers = append(numbers, num)
		}
		if isSequenceSafe(numbers) {
			correctCount++
		}
	}
	fmt.Println("Part 1 solution:", correctCount)

	// PART 2
	correctCount = 0
outer:
	for _, line := range lines {
		parts := strings.Fields(line)
		numbers := []int{}
		for _, part := range parts {
			num, _ := strconv.Atoi(part)
			numbers = append(numbers, num)
		}

		if isSequenceSafe(numbers[1:]) {
			correctCount++
			continue
		}

		increasing := numbers[0] < numbers[1]

		for i, j := 0, 1; j < len(numbers); {
			if increasing && numbers[i] > numbers[j] {
				firstCase := slices.Delete(slices.Clone(numbers), i, i+1)
				secondCase := slices.Delete(slices.Clone(numbers), j, j+1)
				if isSequenceSafe(firstCase) || isSequenceSafe(secondCase) {
					correctCount++
				}
				continue outer
			}
			if !increasing && numbers[i] < numbers[j] {
				firstCase := slices.Delete(slices.Clone(numbers), i, i+1)
				secondCase := slices.Delete(slices.Clone(numbers), j, j+1)
				if isSequenceSafe(firstCase) || isSequenceSafe(secondCase) {
					correctCount++
				}
				continue outer
			}
			diff := abs(numbers[i] - numbers[j])
			if diff < 1 || diff > 3 {
				firstCase := slices.Delete(slices.Clone(numbers), i, i+1)
				secondCase := slices.Delete(slices.Clone(numbers), j, j+1)
				if isSequenceSafe(firstCase) || isSequenceSafe(secondCase) {
					correctCount++
				}
				continue outer
			}
			i++
			j++
		}
		correctCount++
	}
	fmt.Println("Part 2 solution:", correctCount)
}
