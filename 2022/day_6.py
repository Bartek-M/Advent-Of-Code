# Advent of code day 6 2022
# https://adventofcode.com/2022/day/6
print("Advent of code day 6 2022\n")


# Part I
class part_1:
    def __init__(self):
        print("[PART I]")

        # Set variables
        self.subroutine = ""
        self.datastream_marker = []

        self.file_open()
        self.calculate_datastream()

        # Print out
        print(
            f"Checked: {len(self.subroutine)} subroutine\nFound datastream marker: {self.datastream_marker[0]} - {self.datastream_marker[1]}\nProcessed: {self.datastream_marker[0] - 1} characters"
        )

    # Open file
    def file_open(self):
        with open("./input/day_6.in", "r") as f:
            self.subroutine = f.read()

    # Calculate datastream
    def calculate_datastream(self):
        for i in range(len(self.subroutine) - 4):
            buffer = self.subroutine[i : i + 4]
            checked = ""

            for char in buffer:
                if char in checked:
                    break

                checked += char

            if len(checked) == 4:
                self.datastream_marker = [i + 5, self.subroutine[i + 5]]
                break


# Part II
class part_2:
    def __init__(self):
        print("\n[PART II]")

        # Set variables
        self.subroutine = ""
        self.datastream_marker = []

        self.file_open()
        self.calculate_datastream()

        # Print out
        print(
            f"Checked: {len(self.subroutine)} subroutine\nFound datastream marker: {self.datastream_marker[0]} - {self.datastream_marker[1]}\nProcessed: {self.datastream_marker[0] - 1} characters"
        )

    # Open file
    def file_open(self):
        with open("./input/day_6.in", "r") as f:
            self.subroutine = f.read()

    # Calculate datastream
    def calculate_datastream(self):
        for i in range(len(self.subroutine) - 14):
            buffer = self.subroutine[i : i + 14]
            checked = ""

            for char in buffer:
                if char in checked:
                    break

                checked += char

            if len(checked) == 14:
                self.datastream_marker = [i + 15, self.subroutine[i + 15]]
                break


# Run
if __name__ == "__main__":
    part_1()
    part_2()
