# Advent of code day 5 2022
# https://adventofcode.com/2022/day/5
print("Advent of code day 5 2022\n")


# Part I
class part_1:
    def __init__(self):
        print("[PART I]")

        # Set variables
        self.cargo = {}
        self.moves = []
        self.top = ""

        self.file_open()
        self.moving_cargo()
        self.top_cargo()

        # Print out
        print(f"Cargo blocks: {len(self.cargo.keys())}   Moves: {len(self.moves)}\nTop: {self.top}")

    # Open file
    def file_open(self):
        with open("./input/day_5.in", "r") as f:
            cargo_done = False

            # Loop through lines
            for line in f.read().split("\n"):
                # Blank line
                if not line:
                    continue

                # Cargo finished
                if line[1] == "1":
                    cargo_done = True
                    continue

                if not cargo_done:  # Cargo read
                    now = True
                    num = 0

                    for i in range(len(line)):
                        # Runing lawas
                        if not line[i] or i % 2 == 0:
                            continue

                        if not now and i % 2 != 0:
                            now = True
                            continue

                        # Adding to cargo list
                        num += 1  # New block
                        now = False  # Don't turn next time

                        # Ensure char isn't a space
                        if line[i] == " ":
                            continue

                        # New block
                        if num not in self.cargo:
                            self.cargo[num] = []

                        self.cargo[num].append(line[i])
                elif line[0] == "m":  # Moves read
                    self.moves.append(
                        (int(line.split(" ")[1]), int(line.split(" ")[3]), int(line.split(" ")[5]))
                    )  # Amount, from block, to block

    # Moving cargo
    def moving_cargo(self):
        for move in self.moves:
            for _ in range(move[0]):
                moved = self.cargo[move[1]].pop(0)
                self.cargo[move[2]].insert(0, moved)

    # Get top cargo
    def top_cargo(self):
        for cargo in sorted(self.cargo):
            self.top += str(self.cargo[cargo][0])


# Part II
class part_2:
    def __init__(self):
        print("\n[PART II]")

        # Set variables
        self.cargo = {}
        self.moves = []
        self.top = ""

        self.file_open()
        self.moving_cargo()
        self.top_cargo()

        # Print out
        print(f"Cargo blocks: {len(self.cargo.keys())}   Moves: {len(self.moves)}\nTop: {self.top}")

    # Open file
    def file_open(self):
        with open("./input/day_5.in", "r") as f:
            cargo_done = False

            # Loop through lines
            for line in f.read().split("\n"):
                # Blank line
                if not line:
                    continue

                # Cargo finished
                if line[1] == "1":
                    cargo_done = True
                    continue

                if not cargo_done:  # Cargo read
                    now = True
                    num = 0

                    for i in range(len(line)):
                        # Runing lawas
                        if not line[i] or i % 2 == 0:
                            continue

                        if not now and i % 2 != 0:
                            now = True
                            continue

                        # Adding to cargo list
                        num += 1  # New block
                        now = False  # Don't turn next time

                        # Ensure char isn't a space
                        if line[i] == " ":
                            continue

                        # New block
                        if num not in self.cargo:
                            self.cargo[num] = []

                        self.cargo[num].append(line[i])
                elif line[0] == "m":  # Moves read
                    self.moves.append(
                        (int(line.split(" ")[1]), int(line.split(" ")[3]), int(line.split(" ")[5]))
                    )  # Amount, from block, to block

    # Moving cargo
    def moving_cargo(self):
        for move in self.moves:
            moved = []

            for _ in range(move[0]):
                moved += self.cargo[move[1]].pop(0)

            self.cargo[move[2]][0:0] = moved

    # Get top cargo
    def top_cargo(self):
        for cargo in sorted(self.cargo):
            self.top += str(self.cargo[cargo][0])


# Run
if __name__ == "__main__":
    part_1()
    part_2()
