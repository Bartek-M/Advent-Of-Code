# Advent of code Day 4 | 2023
# https://adventofcode.com/2023/day/4
print("Advent of code Day 4 | 2023\n")
import time
from collections import deque

with open("./input/day_4.in", "r") as f:
    data = {}
    
    for line in f.readlines():
        line = line.strip().split(": ")
        card = line[1].replace("  ", " ").strip().split(" | ")
        
        winning = list(map(lambda x: int(x), card[0].split(" ")))
        selected = list(map(lambda x: int(x), card[1].split(" ")))
        
        data[int(line[0].replace("Card ", ""))] = [winning, selected]  # Game_ID: [winning, selected]
        
# Part 1
start_1 = time.time()
sum = 0

for card in data.values():
    current = 0
    
    for num in card[0]:
        if num not in card[1]:
            continue
        
        if not current:
            current = 1
        else:
            current *= 2
    
    sum += current

print(f"[PART 1]  Time: {(time.time() - start_1):.4f}s  Result: {sum}")


# Part 2
start_2 = time.time()
cards = deque(data.keys())

checked = {}
empty = set()

instances = 0

while cards:
    current = cards.popleft()
    card = data[current]
    
    n = 1
    instances += 1

    if current in empty:
        continue

    if current not in checked:
        for num in card[0]:
            if num not in card[1]:
                continue
            
            n += 1
        
        if n == 1:
            continue

        checked[current] = list(range(current + 1, current + n))

    cards.extend(checked[current])

print(f"[PART 2]  Time: {(time.time() - start_2):.4f}s  Result: {instances}")
