# Advent of code day 8 2022
# https://adventofcode.com/2022/day/8
print("Advent of code day 8 2022\n")


# Part I
class part_1:
    def __init__(self):
        print("[PART I]")

        # Set variables
        self.forest = []
        self.visible_trees = 0

        self.file_open()
        self.calc_trees()

        # Print out
        print(f"Checked: {len(self.forest) * len(self.forest[0])} trees\nVisible: {self.visible_trees} trees")

    # Open file
    def file_open(self):
        with open("./input/day_8.in", "r") as f:
            self.forest = [list(line) for line in f.read().split("\n")]

    # Check visibility
    def check_vis(self, pos, tree):
        x, y = pos

        current_x, current_y = 0, 0
        x_match, y_match = [0, 0], [0, 0]

        # Check x
        for i in range(len(self.forest[0])):
            if int(self.forest[y][i]) >= tree and i != x:
                x_match[current_x] += 1

            if i == x:
                current_x = 1

        # Check y
        for i in range(len(self.forest)):
            if int(self.forest[i][x]) >= tree and i != y:
                y_match[current_y] += 1

            if i == y:
                current_y = 1

        # Check matches and return
        if (x_match[0] >= 1 and x_match[1] >= 1) and (y_match[0] >= 1 and y_match[1] >= 1):
            return 0
        else:
            return 1

    # Calculate visible trees
    def calc_trees(self):
        edge = len(self.forest[0]) * 2 + (len(self.forest) - 2) * 2  # Top + bottom, left + right

        for ind, row in enumerate(self.forest):
            if ind == 0 or ind == len(self.forest) - 1:
                continue

            for pos, tree in enumerate(row[1:-1]):
                self.visible_trees += self.check_vis((pos + 1, ind), int(tree))

        self.visible_trees += edge


# Part II
class part_2:
    def __init__(self):
        print("\n[PART II]")

        # Set variables
        self.forest = []
        self.highest_scenic = 0

        self.file_open()
        self.calc_trees()

        # Print out
        print(f"Checked: {len(self.forest) * len(self.forest[0])} trees\nHighest scenic score: {self.highest_scenic}")

    # Open file
    def file_open(self):
        with open("./input/day_8.in", "r") as f:
            self.forest = [list(line) for line in f.read().split("\n")]

    # Check visibility
    def check_vis(self, pos, tree):
        x, y = pos

        current_x, current_y = 0, 0
        x_match, y_match = [0, 0], [0, 0]
        x_trees, y_trees = [-1, -1], [-1, -1]

        # Check x
        for i in range(len(self.forest[0])):
            if i == x:
                current_x = 1
                continue

            if int(self.forest[y][i]) > tree:  # x_trees[current_x]:
                x_trees[current_x] = int(self.forest[y][i])
                x_match[current_x] += 1

        # Check y
        for i in range(len(self.forest)):
            if i == y:
                current_y = 1
                continue

            if int(self.forest[i][x]) > tree:  # y_trees[current_y]:
                y_trees[current_y] = int(self.forest[i][x])
                y_match[current_y] += 1

        # Check scenic_score
        scenic_score = x_match[0] * x_match[1] * y_match[0] * y_match[1]

        if scenic_score > self.highest_scenic:
            self.highest_scenic = scenic_score

    # Calculate visible trees
    def calc_trees(self):
        for ind, row in enumerate(self.forest):
            for pos, tree in enumerate(row):
                self.check_vis((pos, ind), int(tree))


# Run
if __name__ == "__main__":
    part_1()
    part_2()
