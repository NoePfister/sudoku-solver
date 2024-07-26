"""Utilitis for the program"""


def forward(pos: [int, int]) -> [int, int]:
    """Wraps the pos to a new line if necessary"""
    if pos[1] < 8:
        pos[1] += 1
    else:
        pos[0] += 1
        pos[1] = 0
    return pos