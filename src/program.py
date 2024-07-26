import sys
from pprint import pprint

from solver import Solver


class Program:
    def __init__(self, sudoku_input, sudoku_input_original):
        self.sudoku = sudoku_input
        self.sudoku_input_original = sudoku_input_original

        self.solver = Solver(self.sudoku, self.sudoku_input_original, self)

    def solve(self) -> list:
        return self.solver.run()

    @staticmethod
    def exit(msg: str):
        print(msg)
        sys.exit()
