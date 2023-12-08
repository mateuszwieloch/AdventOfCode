import sys

DIR = {
    "L": 0,
    "R": 1
}


with open(sys.argv[1]) as f:
    lines = f.read().strip().split("\n")

lrs = lines[0]

nodes = {}
for line in lines[2:]:
    from_, to_ = line.split(" = ")
    to_ = to_.replace(")", "").replace("(", "").split(", ")
    nodes[from_] = to_

current_node = "AAA"
lrs_index = 0
steps = 0

while current_node != "ZZZ":
    dir = DIR[lrs[lrs_index]]
    current_node = nodes[current_node][dir]
    steps += 1
    lrs_index = (lrs_index + 1) % len(lrs)

print(steps)


# Task 2

class Cycle:
    def __init__(self, start_node: str):
        self.start_node = start_node
        self.end_node = ""
        self.steps_to_end_node = 0
        self.steps_in_cycle = 0

    def __repr__(self) -> str:
        return f"{self.start_node}->{self.end_node} Steps to end node:{self.steps_to_end_node} Steps in cycle:{self.steps_in_cycle}"


cycles = []
for start_node in filter(lambda node: node.endswith("A"), nodes):
    cycles.append(Cycle(start_node))

steps = 0

for c in cycles:
    current_node = c.start_node
    lrs_index = 0
    while not current_node.endswith("Z"):
        dir = DIR[lrs[lrs_index]]
        current_node = nodes[current_node][dir]
        c.steps_to_end_node += 1
        lrs_index = (lrs_index + 1) % len(lrs)
    c.end_node = current_node

    while c.steps_in_cycle < 1 or current_node != c.end_node:
        dir = DIR[lrs[lrs_index]]
        current_node = nodes[current_node][dir]
        lrs_index = (lrs_index + 1) % len(lrs)
        c.steps_in_cycle += 1


for c in cycles:
    print(f"Steps in cycle: {c.steps_in_cycle}")

print("Use an online tool to find the lowest common multiplier. That's the answer to Task 2.")
