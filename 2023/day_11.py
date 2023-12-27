# Advent of code Day 11 | 2023
# https://adventofcode.com/2023/day/11
print("Advent of code Day 11 | 2023\n")
import time

with open("./input/day_11.in", "r") as f:
    data = [list(line.strip()) for line in f.readlines()]


# Part 1
def find_galaxies(space):
    return [(i, j) for i in range(len(space)) for j in range(len(space[i])) if space[i][j] == "#"]


def expanded_space(space, galaxies):
    rows_added = [i for i in range(len(space)) if len(set(space[i])) == 1]
    cols_added = sorted(list(set(range(len(space[0]))).difference(set(ind for row in space for ind, col in enumerate(row) if col == "#"))))

    expand_galaxies = []

    for galaxy in galaxies:
        y, x = galaxy

        y += sum(y > i for i in rows_added)
        x += sum(x > i for i in cols_added)

        expand_galaxies.append((y, x))

    return expand_galaxies


def get_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)


start_1 = time.time()

galaxies = expanded_space(data, find_galaxies(data))
result = sum([get_dist(galaxies[i], gal_chk) for i in range(len(galaxies)) for gal_chk in galaxies[i:]])

print(f"[PART 1]  Time: {(time.time() - start_1):.4f}s  Result: {result}")


# Part 2
def find_galaxies(space):
    return [(i, j) for i in range(len(space)) for j in range(len(space[i])) if space[i][j] == "#"]


def expanded_space(space, galaxies):
    rows_added = [i for i in range(len(space)) if len(set(space[i])) == 1]
    cols_added = sorted(list(set(range(len(space[0]))).difference(set(ind for row in space for ind, col in enumerate(row) if col == "#"))))

    expand_galaxies = []

    for galaxy in galaxies:
        y, x = galaxy

        y += sum(y > i for i in rows_added) * 999_999  # 1_000_000 - 1
        x += sum(x > i for i in cols_added) * 999_999

        expand_galaxies.append((y, x))

    return expand_galaxies


def get_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)


start_1 = time.time()

galaxies = expanded_space(data, find_galaxies(data))
result = sum([get_dist(galaxies[i], gal_chk) for i in range(len(galaxies)) for gal_chk in galaxies[i:]])

print(f"[PART 2]  Time: {(time.time() - start_1):.4f}s  Result: {result}")
