# Task 1
def is_symbol(char: str) -> bool:
    return not char.isdigit() and not char == '.'


def is_adjacent_to_symbol(lines: list[str], row: int, col:int) -> bool:
    # row above
    if row > 0:
        if col > 0 and is_symbol(lines[row-1][col-1]):
            return True
        if is_symbol(lines[row-1][col]):
            return True
        if col < len(lines[0])-1 and is_symbol(lines[row-1][col+1]):
            return True
    # same row
    if col > 0 and is_symbol(lines[row][col-1]):
        return True
    if col < len(lines[0])-1 and is_symbol(lines[row][col+1]):
        return True
    # row below
    if row < len(lines)-1:
        if col > 0 and is_symbol(lines[row+1][col-1]):
            return True
        if is_symbol(lines[row+1][col]):
            return True
        if col < len(lines[0])-1 and is_symbol(lines[row+1][col+1]):
            return True
    return False


def is_num_adjecent_to_symbol(lines: list[str], row: int, col_start: int, col_end: int):
    return any([is_adjacent_to_symbol(lines, row, col) for col in range(col_start, col_end+1)])


def get_num_len_at(line: str, col:int) -> int:
    num_len = 1
    col += 1
    while col < len(line) and line[col].isdigit():
        num_len += 1
        col += 1
    return num_len


with open("one.in") as input_file:
    lines = input_file.read().strip().split("\n")

result = 0

for row, line in enumerate(lines):
    col = 0
    while col < len(line):
        if line[col].isdigit():
            num_len = get_num_len_at(line, col)
            if is_num_adjecent_to_symbol(lines, row, col, col+num_len-1):
                num = int(line[col:col+num_len])
                result += num
            col += num_len
        else:
            col += 1
print(result)


# Task 2
def find_num_slice(line: str, col: int) -> slice:
    c = col
    while c >= 0 and line[c].isdigit():
        col_start = c
        c -= 1
    c = col
    while c < len(line) and line[c].isdigit():
        col_end = c
        c += 1
    return slice(col_start, col_end+1)


def num_at(line: str, col: int) -> int:
    return int(line[find_num_slice(line, col)])



gear_ratio_sum = 0

ROWS = len(lines)
COLS = len(lines[0])

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == '*':
            gears:list[tuple] = []
            # row above
            if row > 0:
                if col > 0 and lines[row-1][col-1].isdigit():
                    gears.append((row-1, col-1))
                if lines[row-1][col].isdigit() and (col == 0 or not lines[row-1][col-1].isdigit()):
                    gears.append((row-1, col))
                if col < COLS-1 and lines[row-1][col+1].isdigit() and not lines[row-1][col].isdigit():
                    gears.append((row-1, col+1))
            # same row
            if col > 0 and lines[row][col-1].isdigit():
                gears.append((row, col-1))
            if col < COLS-1 and lines[row][col+1].isdigit():
                gears.append((row, col+1))
            # row below
            if row < ROWS-1:
                if col > 0 and lines[row+1][col-1].isdigit():
                    gears.append((row+1, col-1))
                if lines[row+1][col].isdigit() and (col == 0 or not lines[row+1][col-1].isdigit()):
                    gears.append((row+1, col))
                if col < COLS-1 and lines[row+1][col+1].isdigit() and not lines[row+1][col].isdigit():
                    gears.append((row+1, col+1))

            if len(gears) == 2:
                gear_ratio = num_at(lines[gears[0][0]], gears[0][1]) * num_at(lines[gears[1][0]], gears[1][1])
                gear_ratio_sum += gear_ratio
print(gear_ratio_sum)
