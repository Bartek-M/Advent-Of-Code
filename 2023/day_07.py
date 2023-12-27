# Advent of code Day 7 | 2023
# https://adventofcode.com/2023/day/7
print("Advent of code Day 7 | 2023\n")
import time

with open("./input/day_7.in", "r") as f:
    data = list(map(lambda x: (x[0], int(x[1])), [line.split() for line in f.readlines()]))


# Part 1
def compare_hand(hand_1, hand_2):
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
    # Insertion sort
    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            if i <= 0 or current[0] == compare_hand(current, lst[i - 1])[0]:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current

    return lst


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


# Part 2
def compare_hand(hand_1, hand_2):
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
    # Insertion sort
    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            if i <= 0 or current[0] == compare_hand(current, lst[i - 1])[0]:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current

    return lst


start_2 = time.time()
CHARS = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
types = {}


for hand in data:
    current_hand = list(hand)
    char_set = set(hand[0])

    if "J" in char_set and len(char_set) != 1:
        current_hand[0] = hand[0].replace("J", max(char_set, key=lambda x: hand[0].count(x) if x != "J" else 0))
        char_set.remove("J")

    current = 0
    char_set_len = len(char_set)

    match char_set_len:
        case 1:
            current = 7
        case 4:
            current = 2
        case 5:
            current = 1
        case 2:
            current = 5 if [char for char in char_set if current_hand[0].count(char) == 3] else 6
        case 3:
            current = 4 if [char for char in char_set if current_hand[0].count(char) == 3] else 3

    if current not in types:
        types[current] = []

    types[current].append(hand)

sum = 0
current = 1

for ind in sorted(types.keys()):
    for cards, bid in sort_hands(types[ind]):
        sum += bid * current
        current += 1

print(f"[PART 2]  Time: {(time.time() - start_2):.4f}s  Result: {sum}")
