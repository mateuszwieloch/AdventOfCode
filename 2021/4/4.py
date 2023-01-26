class Board:
    def __init__(self):
        self.rows = []
        self.cols = [set() for x in range(5)]

    def add_row(self, row: list[int]):
        self.rows.append(set(row))

        for i in range(len(row)):
            self.cols[i].add(row[i])

    def remove_guess(self, guess: int) -> bool:
        for row in self.rows:
            row.discard(guess)
            if not row:
                return True
        for col in self.cols:
            col.discard(guess)
            if not col:
                return True
        return False

    def sum_of_elements(self) -> int:
        return sum([sum(row) for row in self.rows])

    def print(self):
        for row in self.rows:
            print(row)

input_file = open("4.in")
guesses = [int(x) for x in input_file.readline().strip().split(',')]

boards = []
while input_file.readline():
    boards.append(Board())
    for i in range(5):
        row = [int(x) for x in input_file.readline().strip().split()]
        boards[-1].add_row(row)

input_file.close()

won = False
for guess in guesses:
    print(f"{guess = }")
    for board in boards:
        won = board.remove_guess(guess)
        # board.print()
        if won:
            print(board.sum_of_elements() * guess)
            break
    if won:
        break

# Task 2
input_file = open("4.in")
from collections import deque
guesses = deque([int(x) for x in input_file.readline().strip().split(',')])


boards = []
while input_file.readline():
    boards.append(Board())
    for i in range(5):
        row = [int(x) for x in input_file.readline().strip().split()]
        boards[-1].add_row(row)

input_file.close()

guess = 0
while len(boards) > 1:
    guess = guesses.popleft()
    boards = list(filter(lambda b: not b.remove_guess(guess), boards))

board = boards[0]
while True:
    guess = guesses.popleft()
    if board.remove_guess(guess):
        break

print(boards[0].sum_of_elements() * guess)
