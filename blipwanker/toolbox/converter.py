"""___Notes_________________________________________________________________"""
"""
binary      ->      game_save
game_save   ->      matrix
matrix      ->      binary

"""
"""___Modules_______________________________________________________________"""

# BlipWanker
from .toolbox import *

# Python
import numpy as np
from typing import Dict, List, Tuple

"""___Functions_____________________________________________________________"""

def binary_to_game_save(binary: str, dimension: int) -> dict:
    game_save = {}
    for s, state in enumerate(binary):
        if state == "1":
            X = (s % dimension)
            Y = -(s // dimension)
            game_save[f"{X}.{Y}"] = "True"
    return game_save

def matrix_to_binary(matrix: np.ndarray) -> Tuple[str, int]:
    """
    A partir de matrix, exporte un binary ainsi que la dimension de matrix.
    """
    matrix = get_square_matrix(matrix)
    binary_g = ""
    for line in matrix:
        for c in line:
            binary_g += str(c)
    return (binary_g, matrix.shape[0])

def game_save_to_matrix(game_save: dict) -> np.ndarray:
    bounds = get_bounds(game_save)
    grille = np.zeros(shape=(
        bounds["y+"] - bounds["y-"] + 1, bounds["x+"] - bounds["x-"] + 1), dtype=int)
    for cell, state in game_save.items():
        if state:
            coords = get_coords(cell)
            grille[bounds["y+"] - coords[1], coords[0] - bounds["x-"]] = 1
    return grille
