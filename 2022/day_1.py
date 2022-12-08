# Advent of code day 1 2022
# https://adventofcode.com/2022/day/1
print("Advent of code day 1 2022\n")

# PART I
class part1:
    def __init__(self):
        print("[PART I]")

        self.elfs = []
        self.food_cal = []

        self.file_open()
        self.create_food_lst()

        # Print out
        print(f"{len(self.elfs)} elfs are saved")
        print(f"Elf [{self.food_cal.index(max(self.food_cal))}] has {max(self.food_cal)} calories of the food")

    # Open file
    def file_open(self):
        with open("./input/day_1.txt", "r") as f:
            self.elfs = f.read().split("\n\n")

    # Create food list
    def create_food_lst(self):
        for index, elf in enumerate(self.elfs):
            for num in elf.split("\n"):
                if index >= len(self.food_cal):
                    self.food_cal.append(int(num))
                else:
                    self.food_cal[index] += int(num)


# PART II
class part2:
    def __init__(self):
        print("\n[PART II]")

        self.elfs = []
        self.food_cal = []
        self.top_elfs = ["", 0]

        self.file_open()
        self.create_food_lst()
        self.top3()

        # Print out
        print(f"{len(self.elfs)} elfs are saved")
        print(f"Elf [{self.top_elfs[0]}] have {self.top_elfs[1]} total calories of the food")

    # Open file
    def file_open(self):
        with open("./input/day_1.txt", "r") as f:
            self.elfs = f.read().split("\n\n")

    # Create food list
    def create_food_lst(self):
        for index, elf in enumerate(self.elfs):
            for num in elf.split("\n"):
                if index >= len(self.food_cal):
                    self.food_cal.append(int(num))
                else:
                    self.food_cal[index] += int(num)

    # Get top 3 elfs
    def top3(self):
        for i in range(3):
            # Top elfs
            self.top_elfs[0] += str(self.food_cal.index(max(self.food_cal)))
            if i != 2: self.top_elfs[0] += ", "

            self.top_elfs[1] += max(self.food_cal) # Total calories
            self.food_cal.pop(self.food_cal.index(max(self.food_cal))) # Remove current max


# Turn on
if __name__ == "__main__":
    part1()
    part2()