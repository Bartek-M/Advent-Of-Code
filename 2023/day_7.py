# Advent of code Day 7 | 2023
# https://adventofcode.com/2023/day/7
print("Advent of code Day 7 | 2023\n")
import time

with open("./input/day_7.in", "r") as f:
    data = list(map(lambda x: (x[0], int(x[1])), [line.split() for line in f.readlines()]))


# Part 1
start_1 = time.time()
CHARS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

"""
Types:
1 - High card
2 - One pair
3 - Two pair
4 - Three of kind
5 - Full house
6 - Four of kind
7 - Five of kind
"""
types = {}


def min_hand(hand_1, hand_2):
    if not hand_2:
        return hand_1

    if hand_1[0] == hand_2[0]:
        return hand_1

    for char_1, char_2 in zip(hand_1[0], hand_2[0]):
        if char_1 == char_2:
            continue

        if CHARS.index(char_1) > CHARS.index(char_2):
            return hand_1

        return hand_2


def sort_hands(lst):
    # Bubble sort
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if num1[0] == min_hand(num1, num2)[0]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


for hand in data:
    char_set = set(hand[0])
    char_set_len = len(char_set)

    current = 0

    match char_set_len:
        case 1:
            current = 7
        case 4:
            current = 2
        case 5:
            current = 1
        case 2:
            current = 5 if [char for char in char_set if hand[0].count(char) == 3] else 6
        case 3:
            current = 4 if [char for char in char_set if hand[0].count(char) == 3] else 3

    if current not in types:
        types[current] = []

    types[current].append(hand)

sum = 0
current = 1

for ind in sorted(types.keys()):
    for _, bid in sort_hands(types[ind]):
        sum += bid * current
        current += 1

print(f"[PART 1]  Time: {(time.time() - start_1):.4f}s  Result: {sum}")
