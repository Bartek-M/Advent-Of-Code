# Advent of code Day 10 | 2023
# https://adventofcode.com/2023/day/10
print("Advent of code Day 10 | 2023\n")
import time

with open("./input/day_10.in", "r") as f:
    data = [list(line.strip()) for line in f.readlines()]


# Part 1
start_1 = time.time()


def find(item, matrix):
    for i in range(len(matrix)):
        if item not in matrix[i]:
            continue

        return (i, matrix[i].index(item))

    return None


def get_next(pos, matrix, last=None):
    row, col = pos
    current = matrix[row][col]

    top, bottom = (row - 1, col), (row + 1, col)
    left, right = (row, col - 1), (row, col + 1)

    if current in ["|", "L", "J", "S"] and row > 0:  # TOP
        if top != last and matrix[top[0]][top[1]] != ".":
            return top, pos

    if current in ["|", "F", "7", "S"] and row < len(matrix):  # BOTTOM
        if bottom != last and matrix[bottom[0]][bottom[1]] != ".":
            return bottom, pos

    if current in ["-", "7", "J", "S"] and col > 0:  # LEFT
        if left != last and matrix[left[0]][left[1]] != ".":
            return left, pos

    if current in ["-", "F", "L", "S"] and col < len(matrix[0]):  # RIGHT
        if right != last and matrix[right[0]][right[1]] != ".":
            return right, pos

    return None, None


length = 1
current, last = get_next(find("S", data), data)

while data[current[0]][current[1]] != "S":
    current, last = get_next(current, data, last)
    length += 1

length //= 2
print(f"[PART 1]  Time: {(time.time() - start_1):.4f}s  Result: {length}")
