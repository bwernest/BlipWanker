"""___Modules_______________________________________________________________"""

# BlipWanker
from .errors import *

# Python
import numpy as np
from typing import Dict, Tuple

"""___Functions_____________________________________________________________"""

def to_base10(number: str) -> int:
    if number in ["0", "1"]:
        return eval(number)
    else:
        return eval(number[0]) * 2**(len(number) - 1) + to_base10(number[1:])

def print_info(text: str, objet: any) -> None:
    render = f"{text} {type(objet)} :"
    if isinstance(objet, (int, float, str)):
        render += f" {objet}"
    elif isinstance(objet, (list)):
        for i, item in enumerate(objet):
            render += f"\n{i} =\t{item}"
    elif isinstance(objet, (dict)):
        for key, value in objet.items():
            render += f"\n{key} =\t{value}"
    print(render)

def write_txt(path: str, text: str, extension: str = "txt", method: str = "w") -> None:
    with open(f"{path}.{extension}", method) as txt:
        txt.write(text)

def read_txt(path: str, extension: str = "txt") -> list[str]:
    with open(f"{path}.{extension}", "r") as txt:
        data = txt.readlines()
    return data

def get_dict_to_text(dico: dict) -> str:
    text = []
    for key, value in dico.items():
        text.append(f"{key}={value}")
    return "\n".join(text)

def get_square_matrix(matrix: np.ndarray) -> np.ndarray:
    """
    A partir de matrix, ajoute des lignes ou colonnes de 0 en haut
    ou à gauche pour la render carrée.
    """
    shape = matrix.shape
    if shape[0] < shape[1]:
        matrix = extend_matrix(matrix, up=shape[1] - shape[0])
    elif shape[0] > shape[1]:
        matrix = extend_matrix(matrix, left=shape[0] - shape[1])
    return matrix

def extend_matrix(matrix: np.ndarray, up: int = 0, down: int = 0, left: int = 0, right: int = 0) -> np.ndarray:
    """
    Ajoute length colonnes de 0 et height lignes de 0 à matrix.
    """
    zeros = np.zeros((matrix.shape[0], left), dtype=int)
    matrix = np.hstack((zeros, matrix))
    zeros = np.zeros((matrix.shape[0], right), dtype=int)
    matrix = np.hstack((matrix, zeros))
    zeros = np.zeros((up, matrix.shape[1]), dtype=int)
    matrix = np.vstack((zeros, matrix))
    zeros = np.zeros((down, matrix.shape[1]), dtype=int)
    matrix = np.vstack((matrix, zeros))
    return matrix

def get_coords(key: str) -> Tuple[int, int]:
    coords = key.split(".")
    return (eval(coords[0]), eval(coords[1]))

def binary_usefull(binary: str, dimension: int) -> bool:
    """
    A optimiser
    """
    matrix = np.zeros(shape=(dimension**2))
    for c, charac in enumerate(binary):
        matrix[c] = eval(charac)
    matrix = np.reshape(matrix, (dimension, dimension))
    if np.sum(matrix[0, :]) > 0 and np.sum(matrix[-1, :]) > 0 or np.sum(matrix[:, 0]) > 0 and np.sum(matrix[:, -1]):
        return True
    else:
        return False

def get_grid_binary(binary: str, dimension: int) -> str:
    return "0" * (dimension**2 - len(binary)) + binary

def get_compact_binary(binary: str) -> str:
    while binary.startswith("0"):
        binary = binary[1:]
    return binary if binary != "" else "0"

def get_bounds(game_save: dict) -> dict:
    first_cell = None
    for key, state in game_save.items():
        if state:
            first_cell = key
            break
    if first_cell is None:
        raise SimulationDead()
    X, Y = get_coords(first_cell)
    bounds = {"x+": X, "x-": X, "y+": Y, "y-": Y}
    for key, state in game_save.items():
        if state:
            X, Y = get_coords(key)
            bounds["x+"] = max(bounds["x+"], X)
            bounds["x-"] = min(bounds["x-"], X)
            bounds["y+"] = max(bounds["y+"], Y)
            bounds["y-"] = min(bounds["y-"], Y)
    return bounds
