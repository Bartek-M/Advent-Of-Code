# Advent of code day 4 2023
# https://adventofcode.com/2023/day/4
print("Advent of code day 4 2023\n")

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

print("[PART 1]", sum)


# Part 2
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

print("[PART 2]", instances)

