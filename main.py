# SUDOKU SOLVER
# by NoePfister


def main():
    programm = Programm()
    programm.solve()

class Programm:
    def __init__(self):
        self.sudoku = [
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

        self.solver = Solver(self.sudoku,self)


    def solve(self):
        print(self.solver.solve())

    def exit(self, msg: str):
        print(msg)
        sys.exit()

class Solver:
    def __init__(self, sudoku, program):
        self.sudoku = sudoku
        self.pos = [0,0]


    def solve(self) -> list:
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

    def solve(self):
        iterations = 0
        running = True
        while running:
            iterations += 1
            if iterations %10000 == 0:
                print(iterations)
                print(running)
            if self.check_solved(self.sudoku):
                running = False
                continue
            elif self.sudoku[self.pos[0]][self.pos[1]] == 9:
                self.back()
                continue
            else:
                while not self.check_sudoku(self.sudoku):
                    if self.sudoku[self.pos[0]][self.pos[1]] == 9:
                        break
                    self.sudoku[self.pos[0]][self.pos[1]] += 1


    def back(self):
        if self.pos[1] > 0:
            self.pos[1] -= 1
        else:
            self.pos[0] -= 1
            self.pos[1] = 8



    def check_solved(self, sudoku) -> bool:
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    return False

        return self.check_sudoku(sudoku)

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