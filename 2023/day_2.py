# Advent of code Day 2 | 2023
# https://adventofcode.com/2023/day/2
print("Advent of code Day 2 | 2023\n")
import time

with open("./input/day_2.in", "r") as f:
    data = {}

    for line in f.readlines():
        line = line.strip().split(": ")
        data[int(line[0].replace("Game ", ""))] = line[1].replace(",", ";").split("; ")  # Game_ID: [list of shown cubes]

# Part 1
start_1 = time.time()
cubes = {"red": 12, "green": 13, "blue": 14}
sum = 0

for game_id in data.keys():
    allow = True

    for play in data[game_id]:
        colors = play.split(" ")

        if int(colors[0]) > cubes[colors[1]]:
            allow = False
            break

        if not allow:
            break

    if allow:
        sum += game_id

print(f"[PART 1]  Time: {(time.time() - start_1):.4f}s  Result: {sum}")


# Part 2
start_2 = time.time()
sum = 0

for game_id in data.keys():
    multi = 1
    max_cubes = {"red": 0, "green": 0, "blue": 0}

    for play in data[game_id]:
        colors = play.split(" ")

        if int(colors[0]) > max_cubes[colors[1]]:
            max_cubes[colors[1]] = int(colors[0])

    for num in max_cubes.values():
        multi *= num

    sum += multi

print(f"[PART 2]  Time: {(time.time() - start_2):.4f}s  Result: {sum}")