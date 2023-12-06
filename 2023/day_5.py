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


# Part 2
start_2 = time.time()


def find_range(ranges, maps):
    results = []
    
    while ranges:
        range_st, range_end = ranges.pop()

        for dest, map_st, map_range in maps:
            map_end = map_st + map_range
            offset = dest - map_st

            if range_end <= map_st or map_end <= range_st:  # No intersections
                continue

            if range_st < map_st:  # Add range from before map
                ranges.append([range_st, map_st])
                range_st = map_st
            if range_end > map_end:
                ranges.append([map_end, range_end])  # Add range from after end
                range_end = map_end

            results.append([range_st + offset, range_end + offset]) # Add range with offset
            break
        else:
            results.append([range_st, range_end])

    return results


seeds = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
min_loc = None

for seed in seeds:
    ranges = [seed]
    
    for maps in data:
        ranges = find_range(ranges, maps)

    current_min = min(ranges)[0]
    min_loc = current_min if min_loc is None or current_min < min_loc else min_loc

print(f"[PART 2]  Time: {(time.time() - start_2):.4f}s  Result: {min_loc}")
