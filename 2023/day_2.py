# Advent of code day 2 2023
# https://adventofcode.com/2023/day/2
print("Advent of code day 2 2023\n")

with open("./input/day_2.in", "r") as f:
    data = {}

    for line in f.readlines():
        line = line.strip().split(": ")
        data[int(line[0].replace("Game ", ""))] = line[1].split("; ")

# Part 1
cubes = {"red": 12, "green": 13, "blue": 14}
sum = 0

for game_id in data.keys():
    allow = True
    
    for play in data[game_id]:
        for cube in play.split(", "):
            colors = cube.split(" ")

            if int(colors[0]) > cubes[colors[1]]:
                allow = False
                break

        if not allow:
            break

    if allow:
        sum += game_id

print("[PART 1]", sum)


# Part 2
sum = 0

for game_id in data.keys():
    multi = 1
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    
    for play in data[game_id]:
        for cube in play.split(", "):
            colors = cube.split(" ")

            if int(colors[0]) > max_cubes[colors[1]]:
                max_cubes[colors[1]] = int(colors[0])

    for num in max_cubes.values():
        multi *= num

    sum += multi

print("[PART 2]", sum)
