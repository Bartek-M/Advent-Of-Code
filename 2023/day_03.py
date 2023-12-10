# Advent of code Day 3 | 2023
# https://adventofcode.com/2023/day/3
print("Advent of code Day 3 | 2023\n")
import time

with open("./input/day_3.in", "r") as f:
    data = [list(line.strip()) for line in f.readlines()]


# Part 1
class Node:
    def __init__(self, grid, row, col, length):
        self.grid = grid

        self.row = row
        self.col = col
        self.length = length

        self.max_width = len(grid[row])
        self.max_height = len(grid)

        self.value = int("".join(grid[row][col : col + length]))
        self.neighbors = self.get_neighbors()

    def get_neighbors(self):
        x, y = self.col, self.row

        for dx in range(-1, self.length + 1):
            if x + dx < 0 or x + dx >= self.max_width:
                continue

            for dy in range(-1, 2):
                if y + dy < 0 or y + dy >= self.max_height:
                    continue

                if dy == 0 and dx in range(self.length):
                    continue

                char = self.grid[y + dy][x + dx]

                if not char.isdigit() and char != ".":
                    return True

        return None


start_1 = time.time()
sum_nodes = 0

for i in range(len(data)):
    current = ""
    row = data[i] + ["."]

    for ind, char in enumerate(row):
        if char.isdigit():
            current += char
            continue

        if not current:
            continue

        node = Node(data, i, ind - len(current), len(current))
        sum_nodes += node.value if node.neighbors else 0

        current = ""

print(f"[PART 1]  Time: {(time.time() - start_1):.4f}s  Result: {sum_nodes}")


# Part 2
class Node:
    def __init__(self, grid, row, col, length):
        self.grid = grid

        self.row = row
        self.col = col
        self.length = length

        self.max_width = len(grid[row])
        self.max_height = len(grid)

        self.value = int("".join(grid[row][col : col + length]))
        self.neighbors = self.get_neighbors()

    def get_neighbors(self):
        x, y = self.col, self.row

        for dx in range(-1, self.length + 1):
            if x + dx < 0 or x + dx >= self.max_width:
                continue

            for dy in range(-1, 2):
                if y + dy < 0 or y + dy >= self.max_height:
                    continue

                if dy == 0 and dx in range(self.length):
                    continue

                if self.grid[y + dy][x + dx] == "*":
                    return (y + dy, x + dx)

        return None

start_2 = time.time()
nodes = {}
sum_nodes = 0

for i in range(len(data)):
    current = ""
    row = data[i] + ["."]

    for ind, char in enumerate(row):
        if char.isdigit():
            current += char
            continue

        if not current:
            continue

        node = Node(data, i, ind - len(current), len(current))
        neighbor = node.neighbors

        if neighbor:
            if neighbor in nodes:
                nodes[neighbor].append(node)
            else:
                nodes[neighbor] = [node]

        current = ""

for key in nodes:
    node_list = nodes[key]

    if len(node_list) != 2:
        continue

    sum_nodes += node_list[0].value * node_list[1].value

print(f"[PART 2]  Time: {(time.time() - start_2):.4f}s  Result: {sum_nodes}")