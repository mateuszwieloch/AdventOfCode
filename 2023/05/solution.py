class Map:
    def __init__(self):
        self.ranges = []

    def add_range(self, dest, src, length):
        self.ranges.append((src, src+length-1, dest, dest+length-1))

    def map(self, number: int) -> int:
        for dest, src, length in self.ranges:
            if src <= number <= src+length-1:
                return dest + (number-src)
        return number


maps:list[Map] = []
seed_locations:list[int] = []

with open("input") as f:
    seeds_to_plant = [int(seed) for seed in f.readline().split()[1:]]
    f.readline()

    while line := f.readline():
        if line[0].isalpha():
            maps.append(Map())
        elif line[0].isdigit():
            src, dest, length = (int(x) for x in line.split())
            maps[-1].add_range(src, dest, length)
        

# Task 1
# for s in seeds_to_plant:
#     for m in maps:
#         s = m.map(s)
#     seed_locations.append(s)
#
# print(min(seed_locations))

def find_overlap(b, e, B, E):
    if B <= b <= E:
        return b, min(e, E)
    elif B <= e <= E:
        return max(b, B), e
    elif b <= B <= e:
        return B, E

# Task 2
seed_ranges:list[int] = []
i = 0
while i < len(seeds_to_plant):
    seed_ranges.append( (seeds_to_plant[i], seeds_to_plant[i]+seeds_to_plant[i+1]) )
    i += 2


for m in maps:
    new_ranges = []
    for beg, end in seed_ranges:
        # print(f"({beg}, {end})")
        found_overlap = False
        for src_beg, src_end, dest_beg, dest_end in m.ranges:
            overlap = find_overlap(beg, end, src_beg, src_end)
            # print(f"    ({src_beg}, {src_end}) -> ({dest_beg}, {dest_end})")
            if overlap is not None:
                overlap_beg, overlap_end = overlap
                shift = dest_beg - src_beg
                text = f"Found overlap ({overlap_beg, overlap_end})!"
                if overlap_beg > beg:
                    seed_ranges.append( (beg, overlap_beg-1) )
                    text += f" adding ({beg}, {overlap_beg-1})"
                new_ranges.append( (overlap_beg+shift, overlap_end+shift) )
                text += f" adding ({overlap_beg+shift}, {overlap_end+shift})"
                if overlap_end < end:
                    seed_ranges.append( (overlap_end+1, end))
                    text += f" adding ({overlap_end+1}, {end})"
                found_overlap = True
                # print(text)
                continue
        if not found_overlap:
            new_ranges.append( (beg, end) )
    # print(f"NEW RANGES = {new_ranges}")
    seed_ranges = new_ranges
    # print()

print(min(r[0] for r in seed_ranges))
