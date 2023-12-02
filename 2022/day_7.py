# Advent of code day 7 2022
# https://adventofcode.com/2022/day/7
print("Advent of code day 7 2022\n")

# NOT FINISHED

# Part I
class part_1:
    def __init__(self):
        print("[PART I]")

        # Set variables
        self.commands = []
        self.file_system = {}
        print(self.file_system)

        self.dir_sum = {}

        self.file_open()
        self.gen_file_system()
        self.visualize_fs()
        self.total_sum()

        # Print out
        print(self.file_system)

    # Open file
    def file_open(self):
        with open("./input/day_7.txt", "r") as f:
            self.commands = [line for line in f.read().split("\n")]
            self.commands.append("$ ")

    # Generate a file system
    def gen_file_system(self):
        current = []
        file_sum = 0
        ls = {}

        for cmd in self.commands:
            # Using command
            if cmd[0] == "$":
                cmd = cmd.removeprefix("$ ")

                # Generate current folder
                if ls:
                    current_dir = self.file_system

                    for dir_ in current:
                        if dir_ not in current_dir:
                            current_dir[dir_] = {}

                        current_dir = current_dir[dir_]

                    current_dir = ls
                    print(current, current_dir)
                    
                    # Reset listing
                    ls = {} 
                    file_sum = 0

                # Change directory
                if cmd.startswith("cd"):
                    current_cd = cmd.removeprefix("cd ")

                    if current_cd == "..":
                        del current[-1]
                    elif current_cd == "/":
                        current = ["/"]
                    else:
                        current.append(current_cd)

                continue
            
            # File listing
            cmd_file = cmd.split(" ")[0] if "dir" not in cmd else {}
            ls[cmd.split(" ")[1]] = cmd_file

            if cmd[0] != "d":
                file_sum += int(cmd.split(" ")[0])

    # Visualize file system
    def visualize_fs(self):
        pass

    # Calculate total sum
    def total_sum(self):
        pass

# Run
if __name__ == "__main__":
    part_1()