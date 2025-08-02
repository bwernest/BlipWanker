"""___Modules_______________________________________________________________"""

# Python
import numpy as np
from typing import Dict, List

"""___Classes_______________________________________________________________"""

class BaerDict(dict):

    def __init__(self, grid: Dict = None):
        self.grid = grid if grid is not None else {}
    
    def __repr__(self):
        return self.grid.__repr__()

    def __getitem__(self, key):
        try:
            return self.grid.__getitem__(key)
        except KeyError:
            self.grid[key] = False
            return False

    def __setitem__(self, key, value):
        self.grid.__setitem__(key, value)

    def __len__(self):
        return self.grid.__len__()

    def __eq__(self, baer: "BaerDict") -> bool:
        return self.grid == baer.grid

    def __ne__(self, baer: "BaerDict") -> bool:
        return not self.__eq__(baer)

    def keys(self):
        return self.grid.keys()

    def values(self):
        return self.grid.values()

    def items(self):
        return self.grid.items()
