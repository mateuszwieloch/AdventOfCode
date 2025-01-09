package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

	mapset "github.com/deckarep/golang-set/v2"
)

func isValid(fromRules map[int]mapset.Set[int], update []int) (bool, int, int) {
	pageToPosition := map[int]int{}
	for pos, page := range update {
		pageToPosition[page] = pos
	}

	for pageIdx := 0; pageIdx < len(update)-1; pageIdx++ {
		page := update[pageIdx]
		for afterIdx := pageIdx + 1; afterIdx < len(update); afterIdx++ {
			afterPage := update[afterIdx]

			if fromRulesForAfterPage, ok := fromRules[afterPage]; ok {
				if fromRulesForAfterPage.Contains(page) {
					return false, pageIdx, afterIdx
				}
			}
		}
	}
	return true, 0, 0
}

func readPageOrderingRules(scanner *bufio.Scanner) map[int]mapset.Set[int] {
	fromRules := map[int]mapset.Set[int]{}

	for scanner.Scan() {
		s := strings.Split(scanner.Text(), "|")
		if len(s) < 2 {
			break
		}
		from, _ := strconv.Atoi(s[0])
		to, _ := strconv.Atoi(s[1])
		if _, ok := fromRules[from]; ok {
			fromRules[from].Add(to)
		} else {
			fromRules[from] = mapset.NewSet(to)
		}
	}

	return fromRules
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	fromRules := readPageOrderingRules(scanner)

	result_valid := 0
	result_invalid := 0

	for scanner.Scan() {
		pagesStrings := strings.Split(scanner.Text(), ",")
		pages := make([]int, len(pagesStrings))
		for i, p := range pagesStrings {
			pages[i], _ = strconv.Atoi(p)
		}
		if valid, _, _ := isValid(fromRules, pages); valid {
			result_valid += pages[len(pages)/2]
		} else {
			for {
				valid, oneIdx, twoIdx := isValid(fromRules, pages)
				if valid {
					result_invalid += pages[len(pages)/2]
					break
				} else {
					tmp := pages[oneIdx]
					pages[oneIdx] = pages[twoIdx]
					pages[twoIdx] = tmp
				}
			}
		}
	}
	fmt.Println("Part 1 result:", result_valid)
	fmt.Println("Part 2 result:", result_invalid)
}
