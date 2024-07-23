import pygame
import sys

# SUDOKU SOLVER
# by NoePfister


def main():
    programm = Programm()
    programm.solve()

class Programm:
    def __init__(self):
        self.sudoku = [
            [0,0,1,2,0,0,0,0,0],
            [0,2,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
        ]
        self.solver = Solver(self.sudoku)


    def solve(self):
        self.solver.solve()

    def exit(self):
        sys.exit()

class Solver:
    def __init__(self, sudoku):
        self.sudoku = sudoku


    def solve(self):
        print(self.check_sudoku(self.sudoku))

    def check_sudoku(self, new_sudoku) -> bool:
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
                print("Row")
                return False
            # COLUMNS
            column = []
            for i in range(9):
                column.append(new_sudoku[j][i])

            if not self.check_group(column):
                print("COLUMN")
                return False


            # Box

        for i in range(3):
            for j in range(3):
                group = []

                x = i*3
                y = j*3

                group.append(new_sudoku[x][y])
                group.append(new_sudoku[x+1][y])
                group.append(new_sudoku[x+2][y])
                group.append(new_sudoku[x][y+1])
                group.append(new_sudoku[x][y+2])
                group.append(new_sudoku[x+1][y+1])
                group.append(new_sudoku[x+2][y+2])
                group.append(new_sudoku[x+2][y+1])
                group.append(new_sudoku[x+1][y+2])

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
                    print("BOX")
                    return False

        return True



    @staticmethod
    def check_group(group: list) -> bool:

        ints = set([1,2,3,4,5,6,7,8,9,0])
        group_set = set(group)

        if not group_set.issubset(ints):
            return False

        # Check if there are double ints
        duplicates = []
        for i in range(len(group)):
            if group[i] == 0:
                continue
            elif group[i] in duplicates:
                return False
            else:
                duplicates.append(group[i])

        return True


main()