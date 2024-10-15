"""
The main Program, that starts the Solver sits here.
"""
import sys

from solver import Solver


class Program:
    def __init__(self, sudoku_input, sudoku_input_original):
        """Initialise variables"""
        self.sudoku = sudoku_input
        self.sudoku_input_original = sudoku_input_original

        self.solver = Solver(self.sudoku, self.sudoku_input_original, self)

    def solve(self) -> list:
        """Solve the sudoku and return it."""
        return self.solver.run()

    @staticmethod
    def exit(msg: str):
        """exit the programm -> only in emergencys."""
        print(msg)
        sys.exit()
