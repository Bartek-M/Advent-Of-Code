# Advent of code Day 15 | 2023
# https://adventofcode.com/2023/day/15
print("Advent of code Day 15 | 2023\n")
import time
from collections import defaultdict

with open("./input/day_15.in", "r") as f:
    data = f.readline().strip().split(",")


# Part 1
start_1 = time.time()


def hash(text):
    current_val = 0

    for char in text:
        current_val = (current_val + ord(char)) * 17 % 256

    return current_val


result = sum([hash(text) for text in data])
print(f"[PART 1]  Time: {((time.time() - start_1) * 10):.2f} ds  Result: {result}")


# Part 2
start_2 = time.time()


def hash(text):
    current_val = 0

    for char in text:
        current_val = (current_val + ord(char)) * 17 % 256

    return current_val


boxes = defaultdict(dict)

for text in data:
    if "-" in text:
        label = text[:-1]
        boxes[hash(label)].pop(label, None)
        continue

    label, num = text.split("=")
    boxes[hash(label)][label] = int(num)

result = sum(
    (i + 1) * (j + 1) * l for i in boxes for j, l in enumerate(boxes[i].values())
)
print(f"[PART 2]  Time: {((time.time() - start_2) * 10):.2f} ds  Result: {result}")
