# Advent of code Day 5 | 2023
# https://adventofcode.com/2023/day/5
print("Advent of code Day 5 | 2023\n")
import time

with open("./input/day_5.in", "r") as f:
    data = []
    seeds = list(map(int, f.readline().replace("seeds: ", "").split(" ")))

    for line in f.readlines():
        line = line.strip()

        if not line:
            continue

        if not line[0].isdigit():
            data.append([])
            continue

        nums = list(map(int, line.split(" ")))
        data[-1].append(nums)

# Part 1
start_1 = time.time()

def find_next(num, index=0):
    if index == len(data):
        return num
    
    for nums in data[index]:
        if num not in range(nums[1], nums[1] + nums[2]):
            continue

        num = nums[0] + (num - nums[1])
        break

    return find_next(num, index + 1)

min_loc = min(map(find_next, seeds))
print(f"[PART 1]  Time: {(time.time() - start_1):.4f}s  Result: {min_loc}")
