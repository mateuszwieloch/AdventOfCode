# NOTE: to run this file, you need to `pip install regex` first. I'm using the 3rd party regex module.

# Task 1
with open("one.in") as input_file:
    result = 0
    while line := input_file.readline().strip():
        for c in line:
            if c.isdigit():
                first_digit = int(c)
                break
        for c in reversed(line):
            if c.isdigit():
                second_digit = int(c)
                break
        result += 10 * first_digit + second_digit
    print("Task 1 result:", result)

# Task 2
import regex
pattern = regex.compile(r"\d|one|two|three|four|five|six|seven|eight|nine")

word_to_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open("one.in") as input_file:
    result = 0
    while line := input_file.readline().strip():
        matches = pattern.findall(line, overlapped=True)
        if matches[0].isdigit():
            first_digit = int(matches[0])
        else:
            first_digit = word_to_digit[matches[0]]
        if matches[-1].isdigit():
            second_digit = int(matches[-1])
        else:
            second_digit = word_to_digit[matches[-1]]
        if not any(char.isdigit() for char in line):
            print(line)
        number = 10 * first_digit + second_digit
        result += number
        # print(line, number)
    print("Task 2 result:", result)

line = "3oneight"
matches = pattern.findall(line, overlapped=True)
print(matches)
