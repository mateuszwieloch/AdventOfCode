total_score = 0
outcome_score = {'X': 0, 'Y': 3, 'Z': 6}
move_score = {'X': 1, 'Y': 2, 'Z': 3}
# X lose, Y draw, Z win
move_mapping = {
    'A X': 'Z', 'B X': 'X', 'C X': 'Y',
    'A Y': 'X', 'B Y': 'Y', 'C Y': 'Z',
    'A Z': 'Y', 'B Z': 'Z', 'C Z': 'X'
}


with open("2.in") as f:
    while line := f.readline().strip():
        opponent_move, outcome = line.split()
        score = outcome_score[outcome] + move_score[move_mapping[line]]
        total_score += score
print(total_score)
