"""___Modules_______________________________________________________________"""

# Python
import numpy as np
from typing import Dict, List

"""___Classes_______________________________________________________________"""

class BaerDict(dict):

    def __init__(self, grid: Dict):
        self.grid = grid
    
    def __repr__(self):
        return self.grid.__repr__()
    
    def __getitem__(self, key):
        try:
            return self.grid.__getitem__(key)
        except KeyError:
            self.grid[key] = False
            return False
