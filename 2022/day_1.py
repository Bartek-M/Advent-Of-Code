# Advent of code day 1 2022
# https://adventofcode.com/2022/day/1
print("Advent of code day 1 2022\n")


class Task:
    def __init__(self):
        # Set variables
        self.elves = []
        self.food_cal = []
        self.top_elves = ["", 0]

        self.file_open()
        self.create_food_lst()
        self.top_3()

        # Print out information
        print("[PART I]")
        print(f"Elf [{self.food_cal.index(max(self.food_cal))}] has {max(self.food_cal)} calories of the food\n")

        print("PART II")
        print(f"Elf [{self.top_elves[0]}] have {self.top_elves[1]} total calories of the food")

    # Open file
    def file_open(self):
        with open("./input/day_1.txt", "r") as f:
            self.elves = f.read().split("\n\n")

    # Create food list
    def create_food_lst(self):
        for index, elf in enumerate(self.elves):
            for num in elf.split("\n"):
                if index >= len(self.food_cal):
                    self.food_cal.append(int(num))
                else:
                    self.food_cal[index] += int(num)

    # Get top 3 elves
    def top_3(self):
        for i in range(3):
            # Top elves
            self.top_elves[0] += str(self.food_cal.index(max(self.food_cal)))

            if i != 2:
                self.top_elves[0] += ", "

            self.top_elves[1] += max(self.food_cal)  # Total calories
            self.food_cal.pop(self.food_cal.index(max(self.food_cal)))  # Remove current max


# Run
if __name__ == "__main__":
    Task()
