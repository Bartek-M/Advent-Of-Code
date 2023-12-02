# Advent of code day 3 2022
# https://adventofcode.com/2022/day/3
print("Advent of code day 3 2022\n")


class Task:
    def __init__(self):
        # Set variables
        self.backpacks = []
        self.groups = []
        self.priority_lst = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.priority_sum, self.new_priority_sum = 0, 0

        self.file_open()
        self.calculate_priority()
        self.create_groups()
        self.calculate_new_priority()

        # Print out
        print("[PART I]")
        print(f"Priority sum: {self.priority_sum}\n")

        print("[PART II]")
        print(f"Priority sum: {self.new_priority_sum}")

    # Open file
    def file_open(self):
        with open("./input/day_3.in", "r") as f:
            self.backpacks = [line for line in f.read().split("\n")]

    # Calculate priority
    def calculate_priority(self):
        # Loop through every backpack
        for backpack in self.backpacks:
            compartments = [backpack[: (len(backpack) // 2)], backpack[(len(backpack) // 2) :]]

            duplic = list(set(compartments[0]) & set(compartments[1]))[0]  # Get duplicated item
            self.priority_sum += self.priority_lst.index(duplic) + 1  # Add to sum

    # Create groups
    def create_groups(self):
        # Loop through every backpack
        for i in range(0, len(self.backpacks), 3):
            duplic = list(set(self.backpacks[i]) & set(self.backpacks[i + 1]) & set(self.backpacks[i + 2]))[0]  # Get duplicated item
            self.groups.append(duplic)  # Add to group or create a new one

    # Calculate priority
    def calculate_new_priority(self):
        for group in self.groups:
            self.priority_sum += self.priority_lst.index(group) + 1


# Run
if __name__ == "__main__":
    Task()
