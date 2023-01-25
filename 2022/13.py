import ast
import functools
from typing import cast

# -1 = right order

def tricompare(first:list|int, second:list|int) -> int:
    if type(first) == int and type(second) == int:
        first = cast(int, first)
        second = cast(int, second)
        if first < second:
            return -1
        elif first == second:
            return 0
        else:
            return 1

    if type(first) != list: # list comparison
        first = [first]
    elif type(second) != list:
        second = [second]
    first = cast(list, first)
    second = cast(list, second)

    for i in range(len(first)):
        if i == len(second):
            break
        result = tricompare(first[i], second[i])
        if abs(result) == 1:
            return result

    # Run out of elements, but did not find conclusive result
    if len(first) == len(second):
        return 0
    if len(first) < len(second):
        return -1
    return 1



result = 0
with open("13.in") as input_file:
    raw_pairs = input_file.read().split("\n\n")
    for pair_idx, raw_pair in enumerate(raw_pairs):
        first, second = raw_pair.strip().split("\n")
        first = ast.literal_eval(first)
        second = ast.literal_eval(second)
        result += pair_idx+1 if tricompare(first, second) == -1 else 0
    print("Task 1 result:", result)


with open("13.in") as input_file:
    raw_pairs = input_file.read().split("\n\n")
    all_signals = [[[2]], [[6]]]
    for raw_pair in raw_pairs:
        first, second = raw_pair.strip().split("\n")
        all_signals.append(ast.literal_eval(first))
        all_signals.append(ast.literal_eval(second))

    all_signals.sort(key=functools.cmp_to_key(tricompare))
    one = all_signals.index([[2]])
    two = all_signals.index([[6]])
    print("Task 2 result:", (one+1)*(two+1))
