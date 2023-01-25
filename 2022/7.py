# Day 7: No Space Left On Device (https://adventofcode.com/2022/day/7)

from enum import Enum


# Task 1
class NodeType(Enum):
    DIR = 1
    FILE = 2


class Node:
    def __init__(self, type: NodeType, name: str, parent: 'Node', size: int = 0):
        self.children = []
        self.name = name
        self.parent = parent
        self.size = size
        self.type = type

    def add(self, node: 'Node'):
        self.children.append(node)


def find_subdir(parent: Node, name: str) -> Node:
    for p in parent.children:
        if p.name == name:
            return p


def calculate_size(root: Node):
    if root.type == NodeType.DIR:
        root.size = sum([calculate_size(x) for x in root.children])
    return root.size


result = 0
all_sizes = []


def find_small_dirs(root: Node):
    global result
    if root.type != NodeType.DIR:
        return
    global all_sizes
    all_sizes.append(root.size)
    if root.size <= 100000:
        result += root.size
    for child in root.children:
        find_small_dirs(child)


root = Node(NodeType.DIR, "/", None)
curNode = root
with open("7.in") as f:
    f.readline()
    while line := f.readline().strip():
        if line.startswith("$ ls"):
            continue
        elif line.startswith("$ cd"):
            _, _, dirname = line.split()
            if dirname == '..':
                curNode = curNode.parent
            else:
                curNode = find_subdir(curNode, dirname)
        else:
            size, name = line.split()
            if size == 'dir':
                curNode.add(Node(NodeType.DIR, name, parent=curNode))
            else:
                curNode.add(Node(NodeType.FILE, name, parent=curNode, size=int(size)))


calculate_size(root)
find_small_dirs(root)
print("Task 1 result:", result)


# Task 2:
def bsearch(L: list, low: int, high: int, x: int) -> int:
    mid = (low + high) // 2
    if L[mid] >= x and L[mid-1] < x:
        return mid
    if L[mid] < x:
        return bsearch(L, mid+1, high, x)
    return bsearch(L, low, mid-1, x)


space_needed = 30000000 - (70000000 - root.size)
all_sizes.sort()
print("Task 2 result:", all_sizes[bsearch(all_sizes, 0, len(all_sizes)-1, space_needed)])
