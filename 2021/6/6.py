from collections import Counter
fish = [int(x) for x in open("6.in").read().strip().split(",")]
fish_grouped = Counter(fish)
for day in range(256):
    new_fish = fish_grouped[0]
    for i in range(1,9):
        fish_grouped[i-1] = fish_grouped[i]
    fish_grouped[6] += new_fish
    fish_grouped[8] = new_fish
    if day == 79 or day == 255:
        print(f"Flock size after {day+1} days:", sum(fish_grouped.values()))
