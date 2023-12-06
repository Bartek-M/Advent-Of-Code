# Advent of code Day 6 | 2023
# https://adventofcode.com/2023/day/6
print("Advent of code Day 6 | 2023\n")
import time
import math

with open("./input/day_6.in", "r") as f:
    times = list(map(int, filter(lambda x: x, f.readline().replace("Time: ", "").split(" "))))
    dist = list(map(int, filter(lambda x: x, f.readline().replace("Distance: ", "").split(" "))))

# Part 1
start_1 = time.time()

def check_times(max_tm, record_dist):
    return sum([1 for tm in range(1, max_tm) if (max_tm - tm) * tm > record_dist])

result = math.prod([check_times(tm, ds) for tm, ds in zip(times, dist)])
print(f"[PART 1]  Time: {(time.time() - start_1):.4f}s  Result: {result}")


# Part 2
start_2 = time.time()

def check_times(max_tm, record_dist):
    return sum([1 for tm in range(1, max_tm) if (max_tm - tm) * tm > record_dist])

max_time = int("".join(map(str, times)))
max_dist = int("".join(map(str, dist)))

result = check_times(max_time, max_dist)
print(f"[PART 2]  Time: {(time.time() - start_2):.4f}s  Result: {result}")
