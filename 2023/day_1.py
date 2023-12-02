# Advent of code day 1 2023
# https://adventofcode.com/2023/day/1
print("Advent of code day 1 2023\n")

with open("./input/day_1.in", "r") as f:
    data = [line.strip() for line in f.readlines()]

# Part 1
sum = 0

for text in data:
    num = []

    for char in text:
        if not char.isdigit():
            continue

        if len(num) < 2:
            num.append(char)
        else:
            num[-1] = char

    if 0 < len(num) < 2:
        num.append(num[0])

    if num:
        sum += int("".join(num))

print("[PART 1]", sum)


# Part 2
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0

def verify_num(text):
    for num, digit in enumerate(digits):
        if len(text) < len(digit):
            continue

        if text[:len(digit)] != digit:
            continue
        
        return str(num+1)
    
    return None

for text in data:
    num = []

    for ind, char in enumerate(text):
        if not char.isdigit():
            if not (char := verify_num(text[ind:])):
                continue

        if len(num) < 2:
            num.append(char)
        else:
            num[-1] = char

    if 0 < len(num) < 2:
        num.append(num[0])

    sum += int("".join(num))

print("[PART 2]", sum)
