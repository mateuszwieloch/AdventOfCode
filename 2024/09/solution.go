package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
)

func calculateChecksum(disk []int) int {
	checksum := 0
	for i, v := range disk {
		if v == -1 {
			continue
		}
		checksum += i * disk[i]
	}
	return checksum
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	diskmap := scanner.Bytes()
	var disk []int
	for i, b := range diskmap {
		blockSize := int(b - '0')
		if i%2 == 0 { // file block
			id := i / 2
			for j := 0; j < blockSize; j++ {
				disk = append(disk, id)
			}
		} else { // free space block
			for j := 0; j < blockSize; j++ {
				disk = append(disk, -1)
			}
		}
	}
	disk2 := slices.Clone(disk)

	// part 1
	var i, j int = 0, len(disk) - 1
	for i < j {
		if disk[j] == -1 {
			j--
			continue
		}
		if disk[i] != -1 {
			i++
			continue
		}
		disk[i] = disk[j]
		disk[j] = -1
		i++
		j--
	}
	fmt.Println("Part 1 solution:", calculateChecksum(disk))

	// part 2
	var min_space_idx, space_size int
	var min_block_idx int
	max_space_idx := 0
	max_block_idx := len(disk2) - 1
	var block_id, block_size int

	for max_block_idx > 0 {
		for max_block_idx > 0 && disk2[max_block_idx] == -1 {
			max_block_idx--
		}
		block_id = disk2[max_block_idx]
		min_block_idx = max_block_idx
		for min_block_idx > 0 && disk2[min_block_idx-1] == block_id {
			min_block_idx--
		}
		block_size = max_block_idx - min_block_idx + 1

		min_space_idx = 0
	space_search:
		for min_space_idx < min_block_idx {
			for disk2[min_space_idx] != -1 {
				min_space_idx++
				if min_space_idx >= min_block_idx {
					break space_search
				}
			}
			max_space_idx = min_space_idx
			for disk2[max_space_idx+1] == -1 {
				max_space_idx++
			}
			space_size = max_space_idx - min_space_idx + 1
			if space_size >= block_size {
				for i := 0; i < block_size; i++ {
					disk2[min_space_idx+i] = disk2[min_block_idx+i]
					disk2[min_block_idx+i] = -1
				}
				break
			} else {
				min_space_idx = max_space_idx + 1
			}
		}
		max_block_idx = min_block_idx - 1
	}
	fmt.Println("Part 2 solution:", calculateChecksum(disk2))
}
