"""___Modules_______________________________________________________________"""

# BlipWanker
from .baerdict import BaerDict
from toolbox import *

# Python
from copy import deepcopy
from matplotlib import pyplot as plt
import numpy as np
from tqdm import tqdm
from typing import Dict, List, Tuple

"""___Classes_______________________________________________________________"""

class JeuDeLaVie():

    def __init__(self, grid: Dict = None):
        self.grid = BaerDict(grid) if grid is not None else BaerDict()
        self.generation: int = 0

    def __eq__(self, game: "JeuDeLaVie") -> bool:
        return self.grid == game.grid and self.generation == game.generation

    def __ne__(self, game: "JeuDeLaVie") -> bool:
        return not self.__eq__(game)

    def __repr__(self) -> str:
        data = {
            "generation": self.generation,
            "cells": len(self.grid),
            "alive": self.live_cells,
            "dead": self.dead_cells,
        }
        render = "JeuDeLaVie"
        for key, value in data.items():
            render += f"\n{key} =\t{value}"
        return render

    @property
    def cells(self) -> int:
        return len(self.grid)

    @property
    def live_cells(self) -> int:
        return list(self.grid.values()).count(True)

    @property
    def dead_cells(self) -> int:
        return list(self.grid.values()).count(False)

    def simulate(self, turn: int = 1, bar: bool = False):
        self.compact()
        for _ in tqdm(range(turn), disable=not bar):
            self.next()

    def next(self):
        next_grid = deepcopy(BaerDict())
        count = [0, 0]

        # Live
        cells = list(self.grid.keys())
        states = list(self.grid.values())
        for cell, state in zip(cells, states):
            count[0] += 1
            if self.update_life(cell):
                next_grid[cell] = True

        # Dead
        cells = list(self.grid.keys())
        states = list(self.grid.values())
        for cell, state in zip(cells, states):
            count[1] += 1
            if state:
                continue
            if self.update_dead(cell):
                next_grid[cell] = True

        self.grid = deepcopy(next_grid)
        self.generation += 1

    def update_life(self, key: str) -> bool:
        coords = self.get_coords(key)
        around = self.get_around(coords)
        alives = [self.grid[self.get_key(coords)] for coords in around]
        return True if alives.count(True) in [2, 3] else False

    def update_dead(self, key: str) -> bool:
        coords = self.get_coords(key)
        around = self.get_around(coords)
        alives = [self.grid[self.get_key(coords)] for coords in around]
        return True if alives.count(True) == 3 else False

    def get_matrix(self) -> np.ndarray:
        minX, maxX, minY, maxY = 0, 0, 1, 1
        for cell, state in self.grid.items():
            if state:
                coords = self.get_coords(cell)
                minX = min(minX, coords[0])
                maxX = max(maxX, coords[0])
                minY = min(minY, coords[1])
                maxY = max(maxY, coords[1])

        grille = np.zeros(shape=(maxY - minY + 1, maxX - minX + 1))

        for cell, state in self.grid.items():
            if state:
                coords = self.get_coords(cell)
                grille[maxY - coords[1], coords[0] - minX] = 1
        return grille

    def display(self) -> None:
        grille = self.get_matrix()
        plt.imshow(grille, cmap='inferno', interpolation='nearest')
        plt.axis('off')  # Masquer les axes
        plt.show()

    def compact(self) -> None:
        compact_grid = BaerDict()
        for cell, state in self.grid.items():
            if state:
                compact_grid[cell] = True
        self.grid = deepcopy(compact_grid)

    def get_coords(self, key: str) -> Tuple[int, int]:
        coords = key.split(".")
        return (eval(coords[0]), eval(coords[1]))

    def get_key(self, coords: Tuple[int, int]) -> str:
        return f"{coords[0]}.{coords[1]}"

    def get_around(self, coords: Tuple[int, int]) -> np.ndarray:
        around = np.ndarray((8, 2), dtype=int)
        around[0] = [coords[0], coords[1] + 1]
        around[1] = [coords[0] + 1, coords[1] + 1]
        around[2] = [coords[0] + 1, coords[1]]
        around[3] = [coords[0] + 1, coords[1] - 1]
        around[4] = [coords[0], coords[1] - 1]
        around[5] = [coords[0] - 1, coords[1] - 1]
        around[6] = [coords[0] - 1, coords[1]]
        around[7] = [coords[0] - 1, coords[1] + 1]
        return around
