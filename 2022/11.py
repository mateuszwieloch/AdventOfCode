# Day 11: Monkey in the Middle (https://adventofcode.com/2022/day/11)

from collections import deque

# Task 1
class Monkey:
    def __init__(self, items: deque[int], op, rhs, test, true_monkey:int, false_monkey:int):
        self.items = items
        self.op = op
        self.rhs = rhs
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey


class Test:
    def __init__(self):
        print("Test")


def compute_expression(op:str, rhs:str, old:int) -> int:
    computed_lhs = old
    if rhs == 'old':
        computed_rhs = old
    else:
        computed_rhs = int(rhs)
    if op == '*':
        return computed_lhs * computed_rhs
    else: # op == '+':
        return computed_lhs + computed_rhs



with open("11.in") as input_file:
    input_lines = input_file.read().strip().split("\n")
    i = 0
    monkeys = []
    while i < len(input_lines):
        i += 1 # skip Monkey #
        raw_starting_items = input_lines[i].split()
        starting_items = deque(map(lambda x: int(x.strip(', ')), raw_starting_items[2:]))
        print(starting_items)
        i += 1
        _, _, _, _lhs, op, rhs = input_lines[i].strip().split()
        i += 1
        test = int(input_lines[i].strip().split()[-1])
        i += 1
        true_monkey = int(input_lines[i].strip().split()[-1])
        i += 1
        false_monkey = int(input_lines[i].strip().split()[-1])
        i += 2
        monkeys.append(Monkey(starting_items, op, rhs, test, true_monkey, false_monkey))



