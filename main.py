"""
Game Of Life

Draws in the terminal. 
Uses a random seed to set some cells to alive.

- Uses `plotile` to draw a grid with braille characters
- Storage with simple nested lists
"""

import os
import time
import random
import plotille as plt
from typing import List

__all__ = ["size", "pixel_data", "neighs_count", "process_data"]


def flatten(t):
    return [item for sublist in t for item in sublist]


size = 100


def pixel_data(data: List[List[bool]]) -> List[int]:
    """
    Converts list in matrix format with bool values to flat list with integer values
    True -> 2
    False -> 0
    """
    return [2 if v else 0 for v in flatten(data)]


def neighs_count(data: List[List[bool]], row_i: int, col_i: int) -> int:
    """
    Amount of alive neighboors in all 8 directions
    """
    ns_count = 0
    for r in range(-1, 2):
        for c in range(-1, 2):
            new_r = row_i + r
            new_c = col_i + c
            if new_r == row_i and new_c == col_i:
                continue

            if new_r < 0 or new_c < 0 or new_r >= size or new_c >= size:
                continue

            if data[new_r][new_c]:
                ns_count += 1
    return ns_count


def process_data(data: List[List[bool]]) -> List[List[bool]]:
    """
    Applies the Game of Life game rules to the data.
    """
    newData = [[False for col in range(size)] for row in range(size)]
    for row_i, row in enumerate(data):
        for col_i, value in enumerate(row):
            ns_c = neighs_count(data, row_i, col_i)
            if value:
                if ns_c < 2:
                    newData[row_i][col_i] = False
                elif ns_c > 3:
                    newData[row_i][col_i] = False
                else:
                    newData[row_i][col_i] = True
            else:
                if ns_c == 3:
                    newData[row_i][col_i] = True
    return newData


if __name__ == "__main__":

    data = [[False for col in range(size)] for row in range(size)]
    # Seed data
    for row_i, row in enumerate(data):
        for col_i, value in enumerate(row):
            if random.random() < 0.4:
                data[row_i][col_i] = True
            else:
                data[row_i][col_i] = False

    # size x size image
    # needs a size/2 x size/4 canvas

    os.system("clear")
    os.system("tput civis")
    while True:
        cvs = plt.Canvas(int(size / 2), int(size / 4))
        cvs.braille_image(pixel_data(data), 1)

        os.system("tput cup 0 0")
        print(cvs.plot())

        # process data
        data = process_data(data)

        time.sleep(0.05)
