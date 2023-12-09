# Advent of code Day 9 | 2023
# https://adventofcode.com/2023/day/9
print("Advent of code Day 9 | 2023\n")
import time

with open("./input/day_9.in", "r") as f:
    data = [list(map(int, line.strip().split(" "))) for line in f.readlines()]

# Part 1
start_1 = time.time()
sum = 0

for seq in data:
    num = 0
    lst = [seq]

    while any(current := lst[-1]):
        lst.append([current[i] - current[i - 1] for i in range(1, len(current))])

    for i in range(2, len(lst) + 1):
        num += lst[-i][-1]

    sum += num

print(f"[PART 1]  Time: {(time.time() - start_1):.4f}s  Result: {sum}")


# Part 2
start_2 = time.time()
sum = 0

for seq in data:
    num = 0
    lst = [seq]

    while any(current := lst[-1]):
        lst.append([current[i] - current[i - 1] for i in range(1, len(current))])

    for i in range(2, len(lst) + 1):
        num = lst[-i][0] - num

    sum += num

print(f"[PART 2]  Time: {(time.time() - start_2):.4f}s  Result: {sum}")
