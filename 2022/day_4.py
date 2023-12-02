# Advent of code day 4 2022
# https://adventofcode.com/2022/day/4
print("Advent of code day 4 2022\n")


# Part I
class part_1:
    def __init__(self):
        print("[PART I]")

        # Set variables
        self.elves = []
        self.overlaps = 0

        self.file_open()
        self.overlaps_check()

        # Print out
        print(f"Checked: {len(self.elves)} pairs\tTotal: {len(self.elves) * 2} elves\nFound: {self.overlaps} overlaping pairs")

    # Open file
    def file_open(self):
        with open("./input/day_4.in", "r") as f:
            self.elves = [(line.split(",")[0], line.split(",")[1]) for line in f.read().split("\n")]

    # Check overlaps
    def overlaps_check(self):
        for pair in self.elves:
            elf_1 = pair[0].split("-")
            elf_2 = pair[1].split("-")

            if int(elf_2[0]) in range(int(elf_1[0]), int(elf_1[1]) + 1) and int(elf_2[1]) in range(int(elf_1[0]), int(elf_1[1]) + 1):
                self.overlaps += 1
            elif int(elf_1[0]) in range(int(elf_2[0]), int(elf_2[1]) + 1) and int(elf_1[1]) in range(int(elf_2[0]), int(elf_2[1]) + 1):
                self.overlaps += 1


# Part II
class part_2:
    def __init__(self):
        print("\n[PART II]")

        # Set variables
        self.elves = []
        self.overlaps = 0

        self.file_open()
        self.overlaps_check()

        # Print out
        print(f"Checked: {len(self.elves)} pairs\tTotal: {len(self.elves) * 2} elves\nFound: {self.overlaps} overlaping pairs")

    # Open file
    def file_open(self):
        with open("./input/day_4.in", "r") as f:
            self.elves = [(line.split(",")[0], line.split(",")[1]) for line in f.read().split("\n")]

    # Check overlaps
    def overlaps_check(self):
        for pair in self.elves:
            elf_1 = pair[0].split("-")
            elf_2 = pair[1].split("-")

            if int(elf_2[0]) in range(int(elf_1[0]), int(elf_1[1]) + 1) or int(elf_2[1]) in range(int(elf_1[0]), int(elf_1[1]) + 1):
                self.overlaps += 1
            elif int(elf_1[0]) in range(int(elf_2[0]), int(elf_2[1]) + 1) or int(elf_1[1]) in range(int(elf_2[0]), int(elf_2[1]) + 1):
                self.overlaps += 1


# Run
if __name__ == "__main__":
    part_1()
    part_2()
