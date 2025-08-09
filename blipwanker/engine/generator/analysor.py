"""___Modules_______________________________________________________________"""

# BlipWanker
from ...toolbox import *

# Python
from copy import deepcopy
from matplotlib import pyplot as plt
import numpy as np
from typing import List

"""___Classes_______________________________________________________________"""

class Analysor():

    def analyse(self, binary_c: str, dimension: int, ok_list: List[str]) -> bool:
        """
        Analyse le binary et évalue sa pertinence :
            - Dimension justifiée
            - Unicité dans sa dimension
        """
        # if not fills_dim(binary_c): return False
