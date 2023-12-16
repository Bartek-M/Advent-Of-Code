# Advent of code Day 16 | 2023
# https://adventofcode.com/2023/day/16
print("Advent of code Day 16 | 2023\n")
import time

with open("./input/day_16.in", "r") as f:
    data = [list(line.strip()) for line in f.readlines()]


# Part 1
start_1 = time.time()


def track_route(pos, direct, grid, added):
    x, y = pos
    dx, dy = direct

    while 0 <= x < len(grid[0]) and 0 <= y < len(grid) and (x, y, dx, dy) not in added:
        added.add((x, y, dx, dy))

        match grid[y][x]:
            case "/":
                dx, dy = -dy, -dx
            case "\\":
                dx, dy = dy, dx
            case "|" if dx:
                added.update(track_route((x, y + 1), (0, 1), grid, added))
                dx, dy = 0, -1
            case "-" if dy:
                added.update(track_route((x + 1, y), (1, 0), grid, added))
                dx, dy = -1, 0

        x, y = x + dx, y + dy

    return added


result = len(set(map(lambda x: (x[0], x[1]), track_route((0, 0), (1, 0), data, set()))))
print(f"[PART 1]  Time: {((time.time() - start_1) * 10):.2f} ds  Result: {result}")


# Part 2
start_2 = time.time()


def track_route(pos, direct, grid, added):
    x, y = pos
    dx, dy = direct

    while 0 <= x < len(grid[0]) and 0 <= y < len(grid) and (x, y, dx, dy) not in added:
        added.add((x, y, dx, dy))

        match grid[y][x]:
            case "/":
                dx, dy = -dy, -dx
            case "\\":
                dx, dy = dy, dx
            case "|" if dx:
                added.update(track_route((x, y + 1), (0, 1), grid, added))
                dx, dy = 0, -1
            case "-" if dy:
                added.update(track_route((x + 1, y), (1, 0), grid, added))
                dx, dy = -1, 0

        x, y = x + dx, y + dy

    return added


max_val = 0

for i in range(len(data[0])):  # TOP + BOTTOM
    max_val = max(max_val, len(set(map(lambda x: (x[0], x[1]), track_route((i, 0), (0, 1), data, set())))))
    max_val = max(max_val, len(set(map(lambda x: (x[0], x[1]), track_route((i, len(data) - 1), (0, -1), data, set())))))

for i in range(len(data)):  # LEFT + RIGHT
    max_val = max(max_val, len(set(map(lambda x: (x[0], x[1]), track_route((0, i), (1, 0), data, set())))))
    max_val = max(max_val, len(set(map(lambda x: (x[0], x[1]), track_route((len(data[0]) - 1, i), (-1, 0), data, set())))))

print(f"[PART 2]  Time: {((time.time() - start_2) * 10):.2f} ds  Result: {max_val}")
