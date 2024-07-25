# SUDOKU SOLVER
# by NoePfister
import sys
import traceback
from pprint import pprint

sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

sudoku_original = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def main():
    programm = Programm(sudoku, sudoku_original)
    programm.solve()


class Programm:
    def __init__(self, sudoku_input, sudoku_original_input):
        self.sudoku = sudoku_input
        self.sudoku_original_input = sudoku_original_input

        self.solver = Solver(self.sudoku, self.sudoku_original_input, self)

    def solve(self):
        pprint(self.solver.run())

    @staticmethod
    def exit(msg: str):
        print(msg)
        sys.exit()


class Solver:
    def __init__(self, sudoku_input: list, sudoku_original_input, program):
        self.sudoku = sudoku_input
        self.sudoku_original = sudoku_original_input
        # IMPORTANT: not working, lists are synced
        self.program = program
        self.pos = [0, 0]

    def run(self) -> list:
        if not self.check_sudoku(self.sudoku):
            self.program.exit("INVALID SUDOKU INPUT")

        else:
            self.solve()

        return self.sudoku

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
        # if the pos[0,0] is a given input, skip forward:
        if self.sudoku[0][0] != 0:
            self.forward()
        iterations = 0

        while True:
            iterations += 1
            if iterations % 10000 == 0:
                print(iterations)

            # print(self.check_sudoku(self.sudoku))
            # if self.check_sudoku(self.sudoku):
            #     self.forward()

            # if the sudoku is solved, exit the loop
            if self.check_solved(self.sudoku):
                print("SOLVED")
                break


            # if the current pos is 9, then go back and continue the next loop
            elif self.sudoku[self.pos[0]][self.pos[1]] == 10:
                self.sudoku[self.pos[0]][self.pos[1]] = 0
                print("BACK")
                self.back()

                continue

            else:

                print("FIND NEXT GOOD VALUE", self.pos)
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

    def back(self):
        if self.pos == [0, 0]:
            print("Cant go back anymore!!!")
            print(self.sudoku)
            traceback.print_stack()
            sys.exit()
        print(self.pos)

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
        # check if sudoku is finished:
        if self.check_solved(self.sudoku):
            return

        if self.pos[0] > 8:
            print("POS[0] is bigger than 8!!!!!")
        if self.pos[1] < 8:
            self.pos[1] += 1
        else:
            self.pos[0] += 1
            self.pos[1] = 0

        print(self.pos, "forward")

        # if the new pos is given from the input, go back once more
        if self.sudoku[self.pos[0]][self.pos[1]] == self.sudoku_original[self.pos[0]][self.pos[1]]:
            if self.sudoku_original[self.pos[0]][self.pos[1]] == 0:
                return
            print("given number reached")
            # check if last pos is reached:
            if self.pos == [8, 8]:
                pprint("Last pos reached!!")
                pprint(self.sudoku)
                sys.exit()
            self.forward()

    def check_solved(self, sudoku) -> bool:
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    return False

        return self.check_sudoku(sudoku)

    @staticmethod
    def check_group(group: list) -> bool:

        ints = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
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
