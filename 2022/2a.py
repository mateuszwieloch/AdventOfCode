total_score = 0
move_score = {'X': 1, 'Y': 2, 'Z': 3}
with open("2.in") as f:
    while rawline := f.readline().strip():
        opponent_move, my_move = rawline.split()
        score = move_score[my_move]
        if rawline in ['A Y', 'B Z', 'C X']:
            score += 6
        elif rawline in ['A X', 'B Y', 'C Z']:
            score += 3
        total_score += score
print(total_score)
