# Day 8: Treetop Tree House (https://adventofcode.com/2022/day/8)

# Task 1
with open("8.in") as input_file:
    trees = input_file.read().strip().split("\n")
    trees = [[int(col) for col in [*row]] for row in trees]
    rows = len(trees)
    cols = len(trees[0])
    results = [[False for _ in range(cols)] for _ in range(rows)]

    # Calculate trees visible from the left
    for r in range(rows):
        tallest_tree = -1
        for c in range(cols):
            if trees[r][c] > tallest_tree:
                tallest_tree = trees[r][c]
                results[r][c] = True

    # Calculate trees visible from the right
    for r in range(rows):
        tallest_tree = -1
        for c in reversed(range(cols)):
            if trees[r][c] > tallest_tree:
                tallest_tree = trees[r][c]
                results[r][c] = True

    # Calculate trees visible from the right
    for c in range(cols):
        tallest_tree = -1
        for r in range(rows):
            if trees[r][c] > tallest_tree:
                tallest_tree = trees[r][c]
                results[r][c] = True

    # Calculate trees visible from the right
    for c in range(cols):
        tallest_tree = -1
        for r in reversed(range(rows)):
            if trees[r][c] > tallest_tree:
                tallest_tree = trees[r][c]
                results[r][c] = True

    total_visible_trees = 0
    for row in results:
        for cell in row:
            if cell:
                total_visible_trees += 1

    print("Task 1 result:", total_visible_trees)


# Task 2
def calculate_scenic_score(trees, r, c):
    tree_height = trees[r][c]

    dist_left = 0
    for cr in reversed(range(r)):
        dist_left += 1
        if trees[cr][c] >= tree_height:
            break

    dist_right = 0
    for cr in range(r+1, len(trees)):
        dist_right += 1
        if trees[cr][c] >= tree_height:
            break

    dist_up = 0
    for cc in reversed(range(c)):
        dist_up += 1
        if trees[r][cc] >= tree_height:
            break

    dist_down = 0
    for cc in range(c+1, len(trees[0])):
        dist_down += 1
        if trees[r][cc] >= tree_height:
            break

    return dist_left * dist_right * dist_up * dist_down

with open("8.in") as input_file:
    trees = input_file.read().strip().split("\n")
    trees = [[int(col) for col in [*row]] for row in trees]
    # trees = [
    #             [3, 3, 3, 3],
    #             [3, 4, 3, 3],
    #             [3, 3, 3, 3]
    #         ]
    rows = len(trees)
    cols = len(trees[0])
    results = [[False for _ in range(cols)] for _ in range(rows)]
    max_score = 0
    for r in range(rows):
        for c in range(cols):
            max_score = max(max_score, calculate_scenic_score(trees, r, c))
    print("Task 2 result", max_score)
