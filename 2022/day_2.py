# Advent of code day 2 2022
# https://adventofcode.com/2022/day/2
print("Advent of code day 2 2022\n")

# PART I
class part_1:
    def __init__(self):
        print("[PART I]")

        # Set variables
        self.encr = ["A", "B", "C"]
        self.games = []
        self.score = 0

        self.file_open()
        self.calculate_score()

        # Print out result
        print(f"Played: {len(self.games)} games\nScore: {self.score}")

    # Open file
    def file_open(self):
        with open("./input/day_2.txt", "r") as f:
            self.games = [(line[0], line[-1].replace("X", "A").replace("Y", "B").replace("Z", "C")) for line in f.read().split("\n")]

    # Calculate score
    def calculate_score(self):
        for game in self.games:
            self.score += self.encr.index(game[1]) + 1 # Pick points

            if game[0] == game[1]: # Draw
                self.score += 3 
            elif (game[0] == "A" and game[1] == "B") or (game[0] == "B" and game[1] == "C") or (game[0] == "C" and game[1] == "A"): # Win
                self.score += 6 


# PART II
class part_2:
    def __init__(self):
        print("\n[PART II]")

        # Set variables
        self.encr = ["A", "B", "C"]
        self.games = []
        self.score = 0

        self.file_open()
        self.calculate_score()

        # Print out resut
        print(f"Played: {len(self.games)} games\nScore: {self.score}")

    # Open file 
    def file_open(self):
        with open("./input/day_2.txt", "r") as f:
            self.games = [(line[0], line[-1]) for line in f.read().split("\n")]

    # Calculate score
    def calculate_score(self):
        for game in self.games:
            if game[1] == "Y": # Draw
                self.score += 3 
            elif game[1] == "Z": # Win
                self.score += 6 

            # Pick points
            if game[1] == "Y": 
                self.score += self.encr.index(game[0]) + 1 
            elif (game[0] == "B" and game[1] == "X") or (game[0] == "C" and game[1] == "Z"): 
                self.score += 1
            elif (game[0] == "C" and game[1] == "X") or (game[0] == "A" and game[1] == "Z"): 
                self.score += 2
            elif (game[0] == "A" and game[1] == "X") or (game[0] == "B" and game[1] == "Z"): 
                self.score += 3


# Run
if __name__ == "__main__":
    part_1()
    part_2()