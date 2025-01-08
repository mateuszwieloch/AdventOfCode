package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func stringsToIntegers(strings []string) []int {
	integers := make([]int, 0, len(strings))
	for _, s := range strings {
		i, _ := strconv.Atoi(s)
		integers = append(integers, i)
	}
	return integers
}

// Returns number that results from concatenating two other numbers
// e.g. 23, 45 => 2345
func concatenate(a, b int) int {
	result, _ := strconv.Atoi(strconv.Itoa(a) + strconv.Itoa(b))
	return result
}

// Returns true if testValue can be produced by placing '+' or '*' operator in-between rightSide values.
// Operations are always performed left-to-right.
// e.g. 292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20.
func canTestValueBeProduced(testValue int, rightSide Stack[int]) bool {
	if rightSide.Size() == 1 {
		return rightSide.vals[0] == testValue
	} else {
		first_new := NewStack(rightSide.vals[:len(rightSide.vals)-2])
		first_new.Push(rightSide.vals[len(rightSide.vals)-1] + rightSide.vals[len(rightSide.vals)-2])
		second_new := NewStack(rightSide.vals[:len(rightSide.vals)-2])
		second_new.Push(rightSide.vals[len(rightSide.vals)-1] * rightSide.vals[len(rightSide.vals)-2])
		return canTestValueBeProduced(testValue, first_new) || canTestValueBeProduced(testValue, second_new)
	}
}

// Returns true if testValue can be produced by placing '+', '*', '||' (concatenation) operator in-between rightSide values.
// Operations are always performed left-to-right.
// e.g. 156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
func canTestValueBeProduced2(testValue int, rightSide Stack[int]) bool {
	if rightSide.Size() == 1 {
		return rightSide.vals[0] == testValue
	} else {
		v1 := rightSide.vals[len(rightSide.vals)-1]
		v2 := rightSide.vals[len(rightSide.vals)-2]
		first_new := NewStack(rightSide.vals[:len(rightSide.vals)-2])
		first_new.Push(v1 + v2)
		second_new := NewStack(rightSide.vals[:len(rightSide.vals)-2])
		second_new.Push(v1 * v2)
		third_new := NewStack(rightSide.vals[:len(rightSide.vals)-2])
		third_new.Push(concatenate(v1, v2))
		return canTestValueBeProduced2(testValue, first_new) ||
			canTestValueBeProduced2(testValue, second_new) ||
			canTestValueBeProduced2(testValue, third_new)
	}
}

func main() {
	result := 0
	result2 := 0
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		line_parts := strings.Split(line, ":") // e.g. "7290: 6 8 6 15"
		testValue, _ := strconv.Atoi(line_parts[0])
		nums := stringsToIntegers(strings.Split(strings.TrimSpace(line_parts[1]), " "))
		slices.Reverse(nums)
		if canTestValueBeProduced(testValue, NewStack(nums)) {
			result += testValue
		}
		if canTestValueBeProduced2(testValue, NewStack(nums)) {
			result2 += testValue
		}
	}
	fmt.Println("Part 1 solution:", result)
	fmt.Println("Part 2 solution:", result2)
}
