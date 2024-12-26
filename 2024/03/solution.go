package main

import (
	"fmt"
	"io"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	input, _ := io.ReadAll(os.Stdin)
	inputString := string(input)

	r, _ := regexp.Compile(`mul\((\d{1,3}),(\d{1,3})\)`)
	matches := r.FindAllStringSubmatch(inputString, -1)
	result := 0
	for _, match := range matches {
		firstNum, _ := strconv.Atoi(match[1])
		secondNum, _ := strconv.Atoi(match[2])
		result += firstNum * secondNum
	}
	fmt.Println("Part 1 solution:", result)

	// PART 2
	r, _ = regexp.Compile(`mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)`)
	matches = r.FindAllStringSubmatch(inputString, -1)
	enabled := true
	result = 0
	for _, match := range matches {
		if enabled && strings.HasPrefix(match[0], "mul") {
			firstNum, _ := strconv.Atoi(match[1])
			secondNum, _ := strconv.Atoi(match[2])
			result += firstNum * secondNum
		} else if strings.HasPrefix(match[0], "don") {
			enabled = false
		} else if strings.HasPrefix(match[0], "do") {
			enabled = true
		}
	}
	fmt.Println("Part 2 solution:", result)
}
