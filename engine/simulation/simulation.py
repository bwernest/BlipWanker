"""___Modules_______________________________________________________________"""

# BlipWanker
from.baerdict import BaerDict

# Python
from copy import deepcopy
import numpy as np
from typing import Dict, List, Tuple

"""___Classes_______________________________________________________________"""

class JeuDeLaVie():

    def __init__(self, grid: Dict = {}):
        self.grid = BaerDict(grid)
        self.generation: int = 0
    
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

    def simulate(self, turn: int = 1):
        for _ in range(turn): self.next()

    def next(self):
        next_grid = BaerDict()

        for key, cell in self.grid.items():
            if not cell: continue
            self.update_life(key)

        self.grid = deepcopy(next_grid)
        self.generation += 1
    
    def update_life(self, key: str) -> None:
        coords = self.get_coords(key)
        around = self.get_around(coords)

    def get_coords(self, key: str) -> Tuple[int, int]:
        coords = key.split(".")
        return (eval[coords[0]], eval[coords[1]])

    def get_around(self, coords: Tuple[int, int]) -> np.ndarray:
        around = np.ndarray((8, 2))
        around[0] = [coords[0],   coords[1]+1]
        around[1] = [coords[0]+1, coords[1]+1]
        around[2] = [coords[0]+1, coords[1]]
        around[3] = [coords[0]+1, coords[1]-1]
        around[4] = [coords[0],   coords[1]-1]
        around[5] = [coords[0]-1, coords[1]-1]
        around[6] = [coords[0]-1, coords[1]]
        around[7] = [coords[0]-1, coords[1]+1]
        return around
