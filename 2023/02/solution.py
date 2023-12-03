# Task 1
LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open("one.in") as input_file:
    sum_of_ids_of_possible_games = 0

    while line := input_file.readline():
        line_info, cube_info = line.split(":")
        _, game_id = line_info.split()
        game_id = int(game_id)

        possible = True

        for round in cube_info.split(";"):
            cube_groups = round.split(",")
            for cube_group in cube_groups:
                num, color = cube_group.split()
                num = int(num)
                if LIMITS[color] < num:
                    possible = False
        if possible:
            sum_of_ids_of_possible_games += game_id
    print(sum_of_ids_of_possible_games)


# Task 2
with open("one.in") as input_file:
    sum_of_powers = 0
    while line := input_file.readline():
        line_info, cube_info = line.split(":")
        _, game_id = line_info.split()
        game_id = int(game_id)

        maxes = {
            "red": 1,
            "green": 1,
            "blue": 1
        }

        for round in cube_info.split(";"):
            cube_groups = round.split(",")
            for cube_group in cube_groups:
                num, color = cube_group.split()
                num = int(num)
                if maxes[color] < num:
                    maxes[color] = num
        power = maxes["red"] * maxes["green"] * maxes["blue"]
        sum_of_powers += power
    print(sum_of_powers)
