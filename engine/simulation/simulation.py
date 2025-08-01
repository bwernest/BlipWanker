"""___Modules_______________________________________________________________"""

# BlipWanker
from.baerdict import BaerDict

# Python
import numpy as np
from typing import Dict, List

"""___Classes_______________________________________________________________"""

class JeuDeLaVie():

    def __init__(self, grid: Dict):
        self.grid = BaerDict(grid)

    def simulate(self, turn: int):
        for _ in range(turn): self.next()

    def next(self):
        pass
