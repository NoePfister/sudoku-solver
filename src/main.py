# SUDOKU SOLVER
# by NoePfister
import copy

from src.program import Programm

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


def main():
    visualize(sudoku)
    programm = Programm(sudoku, copy.deepcopy(sudoku))
    
    visualize(programm.solve())


# https://codegolf.stackexchange.com/a/126934
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


main()
