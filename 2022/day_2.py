# Advent of code day 2 2022
# https://adventofcode.com/2022/day/2
print("Advent of code day 2 2022\n")


class Task:
    def __init__(self):
        # Set variables
        self.encr_1, self.encr_2 = ["A", "B", "C"], ["X", "Y", "Z"]
        self.games = []
        self.score, self.new_score = 0, 0

        self.file_open()
        self.calculate_score()
        self.calculate_new_score()

        # Print out result
        print("[PART I]")
        print(f"Score: {self.score}\n")

        print("[PART II]")
        print(f"Score: {self.new_score}")

    # Open file
    def file_open(self):
        with open("./input/day_2.txt", "r") as f:
            self.games = [(line[0], line[-1]) for line in f.read().split("\n")]

    # Calculate score
    def calculate_score(self):
        for game in self.games:
            self.score += self.encr_2.index(game[1]) + 1 # Pick points

            if game[0] == game[1]: # Draw
                self.score += 3 
            elif (game[0] == "A" and game[1] == "Y") or (game[0] == "B" and game[1] == "Z") or (game[0] == "C" and game[1] == "X"): # Win
                self.score += 6 

    # Calculate new score
    def calculate_new_score(self):
        for game in self.games:
            if game[1] == "Y": # Draw
                self.new_score += 3 
            elif game[1] == "Z": # Win
                self.new_score += 6 

            # Pick points
            if game[1] == "Y": 
                self.new_score += self.encr_1.index(game[0]) + 1 
            elif (game[0] == "B" and game[1] == "X") or (game[0] == "C" and game[1] == "Z"): 
                self.new_score += 1
            elif (game[0] == "C" and game[1] == "X") or (game[0] == "A" and game[1] == "Z"): 
                self.new_score += 2
            elif (game[0] == "A" and game[1] == "X") or (game[0] == "B" and game[1] == "Z"): 
                self.new_score += 3


# Run
if __name__ == "__main__":
    Task()