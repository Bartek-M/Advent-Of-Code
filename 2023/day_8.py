# Advent of code Day 8 | 2023
# https://adventofcode.com/2023/day/8
print("Advent of code Day 8 | 2023\n")
import time
from math import lcm

with open("./input/day_8.in", "r") as f:
    moves = list(map(lambda x: 0 if x == "L" else 1, f.readline().strip()))
    data = {}

    for line in f.readlines()[1:]:
        line = line.strip().replace("(", "").replace(")", "").split(" = ")
        data[line[0]] = line[1].split(", ")


# Part 1
start_1 = time.time()
move, n = 0, 0
current = "AAA"

while current != "ZZZ":
    current = data[current][moves[move]]

    move = (move + 1) if move < len(moves) - 1 else 0
    n += 1

print(f"[PART 1]  Time: {(time.time() - start_1):.4f}s  Result: {n}")


# Part 2
start_2 = time.time()
nodes = [node for node in data.keys() if node[-1] == "A"]
results = []

for node in nodes:
    move, n = 0, 0
    current = node

    while current[-1] != "Z":
        current = data[current][moves[move]]

        move = (move + 1) if move < len(moves) - 1 else 0
        n += 1

    results.append(n)

result = lcm(*results)
print(f"[PART 2]  Time: {(time.time() - start_2):.4f}s  Result: {result}")
