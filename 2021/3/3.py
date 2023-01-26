input_file = open("3.in")
lines = [line.strip() for line in input_file.readlines()]
input_file.close()

# Task 1
gamma = "" # most common bits
epsilon = "" # least common bits
for char in range(len(lines[0])):
    zeros = 0
    ones = 0
    for line in lines:
        if line[char] == '0':
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma*epsilon)

# Task 2
remaining_lines = lines
bit = 0
while len(remaining_lines) > 1:
    zeros = 0
    ones = 0
    for line in remaining_lines:
        if line[bit] == '0':
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        remaining_lines = [x for x in remaining_lines if x[bit] == '0']
    else:
        remaining_lines = [x for x in remaining_lines if x[bit] == '1']
    bit += 1
oxygen_level = int(remaining_lines[0], 2)

remaining_lines = lines
bit = 0
while len(remaining_lines) > 1:
    zeros = 0
    ones = 0
    for line in remaining_lines:
        if line[bit] == '0':
            zeros += 1
        else:
            ones += 1
    if zeros <= ones:
        remaining_lines = [x for x in remaining_lines if x[bit] == '0']
    else:
        remaining_lines = [x for x in remaining_lines if x[bit] == '1']
    bit += 1
co2_level = int(remaining_lines[0], 2)
print(oxygen_level*co2_level)
