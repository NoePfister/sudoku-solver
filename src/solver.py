"""
The real Solver. It gets the Sudoku as an Input,
and returns the solved sudoku.
"""

import sys
import traceback

import utils


class Solver:
    """The main class which houses the Solver."""

    def __init__(self, sudoku_input: list, sudoku_original_input, program):
        """Initialise the variables"""
        self.sudoku = sudoku_input
        self.sudoku_original = sudoku_original_input
        # IMPORTANT: not working, lists are synced
        self.program = program
        self.pos = [0, 0]

    def run(self) -> list:
        """Run the Solver and return the solution"""
        if not self.check_sudoku(self.sudoku):

            self.program.exit("INVALID SUDOKU INPUT")

        else:
            # print("START SOLVING")
            self.solve()

        return self.sudoku

    def check_sudoku(self, new_sudoku) -> bool:
        """Check if the inputted sudoku is valid."""
        # Check sudoku

        # POSSIBLE CASES:
        # 1. One Row isn't correct
        # 2. One Column isn't correct
        # 3. One Box isn't correct
        # 4. Everything is correct

        for j in range(9):
            # ROWS
            row = []
            for i in range(9):
                row.append(new_sudoku[i][j])

            if not self.check_group(row):
                # print("Row")
                return False
            # COLUMNS
            column = []
            for i in range(9):
                column.append(new_sudoku[j][i])

            if not self.check_group(column):
                # print("COLUMN")
                return False

            # Box

        for i in range(3):
            for j in range(3):
                group = []

                x = i * 3
                y = j * 3

                group.append(new_sudoku[x][y])
                group.append(new_sudoku[x + 1][y])
                group.append(new_sudoku[x + 2][y])
                group.append(new_sudoku[x][y + 1])
                group.append(new_sudoku[x][y + 2])
                group.append(new_sudoku[x + 1][y + 1])
                group.append(new_sudoku[x + 2][y + 2])
                group.append(new_sudoku[x + 2][y + 1])
                group.append(new_sudoku[x + 1][y + 2])

                # print(x,y)
                # print(x+1,y)
                # print(x+2,y)
                # print(x,y+1)
                # print(x,y+2)
                # print(x+1,y+1)
                # print(x+2,y+2)
                # print(x+2,y+1)
                # print(x+1,y+2)

                if not self.check_group(group):
                    # print("BOX")
                    return False

        return True

    def solve(self):
        """Start the solving loop."""
        # if the pos[0,0] is a given input, skip forward:
        if self.sudoku[0][0] != 0:
            self.forward()
        iterations = 0

        while True:
            iterations += 1
            # if iterations % 10000 == 0:
            #     print(iterations)

            # print(self.check_sudoku(self.sudoku))
            # if self.check_sudoku(self.sudoku):
            #     self.forward()

            # if the sudoku is solved, exit the loop
            if self.check_solved(self.sudoku):
                print("SOLVED")
                break

            # if the current pos is 9, then go back and continue the next loop
            if self.sudoku[self.pos[0]][self.pos[1]] == 10:
                self.sudoku[self.pos[0]][self.pos[1]] = 0
                # print("BACK")
                self.back()

                continue

            # print("FIND NEXT GOOD VALUE", self.pos)
            searching = True
            # increase the value until it is a valid sudoku or skip,
            # if the value is 9, which will be picked up in the next loop
            # and the back function will be called
            while searching:

                if self.sudoku[self.pos[0]][self.pos[1]] == 10:
                    break
                self.sudoku[self.pos[0]][self.pos[1]] += 1
                if self.check_sudoku(self.sudoku):
                    searching = False
                    self.forward()

        print(f'ITERATIONS: {iterations}')

    def back(self):
        """Bring the position back."""
        if self.pos == [0, 0]:
            # print("Cant go back anymore!!!")
            # print(self.sudoku)
            traceback.print_stack()
            sys.exit()
        # print(self.pos)

        if self.pos[1] > 0:
            self.pos[1] -= 1
        else:
            self.pos[0] -= 1
            self.pos[1] = 8
        # if the new pos is given from the input, go back once more
        if self.sudoku[self.pos[0]][self.pos[1]] == self.sudoku_original[self.pos[0]][self.pos[1]]:
            if not self.sudoku[self.pos[0]][self.pos[1]] == 0:
                self.back()

    def forward(self):
        """Bring the position forward"""
        # check if sudoku is finished:
        if self.check_solved(self.sudoku):
            return

        self.pos = utils.forward(self.pos)

        # print(self.pos, "forward")

        # if the new pos is given from the input, go back once more
        if self.sudoku[self.pos[0]][self.pos[1]] == self.sudoku_original[self.pos[0]][self.pos[1]]:
            if self.sudoku_original[self.pos[0]][self.pos[1]] == 0:
                return
            # print("given number reached")
            # check if last pos is reached:
            if self.pos == [8, 8]:
                # pprint("Last pos reached!!")
                # pprint(self.sudoku)
                return
            self.forward()

    def check_solved(self, _) -> bool:
        """Check if the Sudoku is solved."""
        for i in range(9):
            for j in range(9):
                if self.sudoku[i][j] == 0:
                    return False

        return self.check_sudoku(self.sudoku)

    @staticmethod
    def check_group(group: list) -> bool:
        """Check if the group violates any rules."""

        ints = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
        group_set = set(group)

        if not group_set.issubset(ints):
            return False

        # Check if there are double ints
        duplicates = []
        for _, num in enumerate(group):
            if num == 0:
                continue
            if num in duplicates:
                return False

            duplicates.append(num)

        return True
