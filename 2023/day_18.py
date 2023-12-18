# Advent of code Day 18 | 2023
# https://adventofcode.com/2023/day/18
print("Advent of code Day 18 | 2023\n")
import time

with open("./input/day_18.in", "r") as f:
    data = list(map(lambda x: (x[0], int(x[1]), x[2][2:-1]), [line.strip().split(" ") for line in f.readlines()]))


# Part 1
start_1 = time.time()


def calc_volume(corners: list, perimeter: int) -> int:
    return (
        abs(sum((corners[i - 1][1] + corners[i][1]) * (corners[i - 1][0] - corners[i][0]) for i in range(len(corners)))) // 2
        + perimeter // 2
        + 1
    )


corners = []
perimeter = 0
x, y = 0, 0

for direct, num, _ in data:
    match direct:
        case "U":
            y -= num
        case "D":
            y += num
        case "L":
            x -= num
        case "R":
            x += num

    corners.append((x, y))
    perimeter += num

result = calc_volume(corners, perimeter)
print(f"[PART 1]  Time: {((time.time() - start_1) * 10):.2f} ds  Result: {result}")


# Part 2
start_2 = time.time()


def calc_volume(corners: list, perimeter: int) -> int:
    return (
        abs(sum((corners[i - 1][1] + corners[i][1]) * (corners[i - 1][0] - corners[i][0]) for i in range(len(corners)))) // 2
        + perimeter // 2
        + 1
    )


corners = []
perimeter = 0
x, y = 0, 0

for _, _, num in data:
    direct, num = num[-1], int(num[:-1], 16)

    match direct:
        case "3":  # U
            y -= num
        case "1":  # D
            y += num
        case "2":  # L
            x -= num
        case "0":  # R
            x += num

    corners.append((x, y))
    perimeter += num

result = calc_volume(corners, perimeter)
print(f"[PART 2]  Time: {((time.time() - start_2) * 10):.2f} ds  Result: {result}")
