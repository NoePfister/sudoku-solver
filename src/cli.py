"""
The Command Line Interface (CLI) of the Sudoku Solver.
It manages the main loop of the application.
"""
import ast
import copy
import dataclasses
import msvcrt
import os
import sys

import utils
from program import Program


@dataclasses.dataclass
class Colors:
    """
    The Colors to print in the terminal
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


TITLE_ASCII = r""" __   _     ___   ___   _     _         __   ___   _     _      ____  ___
( (` | | | | | \ / / \ | |_/ | | |     ( (` / / \ | |   \ \  / | |_  | |_) 
_)_) \_\_/ |_|_/ \_\_/ |_| \ \_\_/     _)_) \_\_/ |_|__  \_\/  |_|__ |_| \\"""


def color_red(text):
    """Returns the text with the colors,so it can be printed in the terminal."""
    return Colors.FAIL + text + Colors.ENDC


def visualize(sudoku_input, pos=None):
    """Visualize the Sudoku in a fancy grid."""
    list_sudoku = []
    for i in range(9):
        for j in range(9):
            list_sudoku.append(sudoku_input[i][j])

    def q(x, y):
        return x + y + x + y + x

    def r(a, b, c, d, e):
        return a + q(q(b * 3, c), d) + e + "\n"

    grid = (((r(*"╔═╤╦╗") + q(q("║ %s │ %s │ %s " * 3 + "║\n", r(*"╟─┼╫╢")), r(*"╠═╪╬╣")) +
              r(*"╚═╧╩╝")) % ast.literal_eval(str(tuple(list_sudoku)))))

    grid_array = grid.split("\n")

    if pos is not None:
        i = pos[0] * 2 + 1
        j = pos[1] * 4 + 2

        grid_array[i] = grid_array[i][:j] + color_red("_") + grid_array[i][j + 1:]

    grid = ""
    for i, line in enumerate(grid_array):
        grid += line + "\n"

    print(grid)


class CLI:
    """
    The main CLI class. This class executes the main Loop of the application.
    """

    def __init__(self):
        """Initialize the variables."""
        self.sudoku_input: list = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.solved_sudoku: list = copy.deepcopy(self.sudoku_input)
        self.pos = [0, 0]
        self.program: Program = Program(self.sudoku_input, self.sudoku_input)

    def start_cli(self):
        """Start the CLI"""

        # LOOP:
        # 1. START MENU
        #   TITLE (Ascii art)
        #   OPTIONS:
        #       - (1) Solve sudoku -> 2. INPUT SUDOKU
        #       - (2) Quit -> EXIT PROGRAM
        #   CREDITS:
        #   Made by Noe
        # 2. INPUT SUDOKU
        #   TITLE (Input Sudoku)
        #   INFO: "Input number one by one, replace empty cells with "0"
        #   GRID: Auto refresh
        #   OPTIONS:
        #       - (s) Done -> 3. SOLVE SUDOKU
        #       - (q) Cancel -> 1. START MENU
        #   CREDITS:
        #   Made by Noe
        # 3. SOLVE SUDOKU
        #   TITLE (Sudoku Solved)
        #   GRID (Solved)
        #   OPTIONS
        #       - (1) Main Menu -> 1. START MENU
        #       - (2) Quit -> EXIT PROGRAM

        self.start_menu_loop()

    def quit(self):
        """Exit the CLI"""
        print(Colors.ENDC)
        self.clear()
        sys.exit()

    def start_menu_loop(self):
        """Start the main menu loop."""

        self.sudoku_input: list = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.solved_sudoku: list = copy.deepcopy(self.sudoku_input)
        self.pos = [0, 0]
        self.program: Program = Program(self.sudoku_input, self.sudoku_input)

        while True:
            self.clear()

            self.print_start_menu()

            input_key = self.wait_for_input()

            match input_key:
                case b'1':
                    self.input_sudoku_loop()
                case b'2':
                    self.quit()
                case _:
                    continue

    def solve_sudoku_loop(self):
        """Start the solve sudoku loop."""
        while True:
            self.clear()
            self.print_solve_sudoku()

            input_key = self.wait_for_input()

            match input_key:
                case b'1':
                    self.start_menu_loop()
                case b'2':
                    self.quit()
                case _:
                    continue

    def input_sudoku_loop(self):
        """Start the input sudoku loop."""
        while True:
            self.clear()

            self.print_input_sudoku()

            input_key = self.wait_for_input()

            match input_key:
                case b's':
                    self.solve_sudoku_loop()
                case b'q':
                    self.quit()
                case b'0':
                    self.add_value(0)
                case b'1':
                    self.add_value(1)
                case b'2':
                    self.add_value(2)
                case b'3':
                    self.add_value(3)
                case b'4':
                    self.add_value(4)
                case b'5':
                    self.add_value(5)
                case b'6':
                    self.add_value(6)
                case b'7':
                    self.add_value(7)
                case b'8':
                    self.add_value(8)
                case b'9':
                    self.add_value(9)
                case _:
                    continue

    def add_value(self, value: int) -> None:
        """Add a value to the input_sudoku"""
        self.sudoku_input[self.pos[0]][self.pos[1]] = value
        self.forward()

    def forward(self, pos=None) -> list:
        """Make the pos go forward"""
        if pos is None:

            if self.pos == [8, 8]:
                self.solve_sudoku_loop()

            self.pos = utils.forward(self.pos)
        else:
            if pos == [8, 8]:
                return pos
            pos = utils.forward(pos)

        return pos

    def print_solve_sudoku(self):
        """Print the solve sudoku loop CLI."""

        #   OPTIONS
        #       - (m) Main Menu -> 1. START MENU
        #       - (q) Quit -> EXIT PROGRAM

        # SOLVE SUDOKU HERE
        if not self.program:
            self.program = Program(self.sudoku_input, copy.deepcopy(self.sudoku_input))

            self.clear()

            self.solved_sudoku = self.program.solve()

        visualize(self.solved_sudoku)

        print("\n\n\n")
        print("OPTIONS:")
        print("    - (1) Main Menu")
        print("    - (2) Quit")

    def print_input_sudoku(self):
        """Print the input sudoku loop CLI."""
        print("Input values one by one!")
        print('VALUES:')
        visualize(self.sudoku_input, self.pos)
        print("OPTIONS:")
        print("    - (s) Solve Sudoku")
        print("    - (q) Quit")

    @staticmethod
    def print_start_menu():
        """Print the start menu loop CLI."""
        print(TITLE_ASCII)
        print("\n\n\n\n")
        print("OPTIONS:")
        print("    - (1) Solve Sudoku")
        print("    - (2) Quit")
        print("\n\n\n\n")
        print("Made by Noé")

    @staticmethod
    def wait_for_input() -> bytes:
        """Wait for key input and return it."""
        return msvcrt.getch()

    @staticmethod
    def clear():
        """Clear the CLI."""
        os.system("cls")
