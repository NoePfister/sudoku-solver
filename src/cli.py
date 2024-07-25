import copy
import msvcrt
import os
import sys
import traceback
from pprint import pprint

from program import Programm

title_ascii = """ __   _     ___   ___   _     _         __   ___   _     _      ____  ___  
( (` | | | | | \ / / \ | |_/ | | |     ( (` / / \ | |   \ \  / | |_  | |_) 
_)_) \_\_/ |_|_/ \_\_/ |_| \ \_\_/     _)_) \_\_/ |_|__  \_\/  |_|__ |_| \\"""


def visualize(sudoku_input):
    # convert to one list
    list_sudoku = []
    for i in range(9):
        for j in range(9):
            list_sudoku.append(sudoku_input[i][j])

    q = lambda x, y: x + y + x + y + x
    r = lambda a, b, c, d, e: a + q(q(b * 3, c), d) + e + "\n"
    print(((r(*"╔═╤╦╗") + q(q("║ %d │ %d │ %d " * 3 + "║\n", r(*"╟─┼╫╢")), r(*"╠═╪╬╣")) + r(*"╚═╧╩╝")) % eval(
        str(tuple(list_sudoku)))).replace(*"0 "))


class CLI:
    def __init__(self):
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
        self.pos = [0, 0]

    def start_cli(self):

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
        self.clear()
        sys.exit()

    def start_menu_loop(self):
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
        self.sudoku_input[self.pos[0]][self.pos[1]] = value
        self.forward()

    def forward(self):

        if self.pos == [8, 8]:
            self.solve_sudoku_loop()

        if self.pos[1] < 8:
            self.pos[1] += 1
        else:
            self.pos[0] += 1
            self.pos[1] = 0

    def print_solve_sudoku(self):

        #   OPTIONS
        #       - (m) Main Menu -> 1. START MENU
        #       - (q) Quit -> EXIT PROGRAM

        # SOLVE SUDOKU HERE
        programm = Programm(self.sudoku_input, copy.deepcopy(self.sudoku_input))

        self.clear()

        visualize(programm.solve())

        print("\n\n\n")
        print("OPTIONS:")
        print("    - (m) Main Menu")
        print("    - (q) Quit")

    def print_input_sudoku(self):
        print("Input values one by one!")
        print('VALUES:')
        pprint(self.sudoku_input)
        print("OPTIONS:")
        print("    - (s) Solve Sudoku")
        print("    - (q) Quit")

    @staticmethod
    def print_start_menu():
        print(title_ascii)
        print("\n\n\n\n")
        print("OPTIONS:")
        print("    - (1) Solve Sudoku")
        print("    - (2) Quit")
        print("\n\n\n\n")
        print("Made by Noé")

    @staticmethod
    def wait_for_input() -> bytes:
        return msvcrt.getch()

    @staticmethod
    def clear():
        os.system("cls")


def test_cli():
    cli = CLI()
    cli.start_cli()


test_cli()
