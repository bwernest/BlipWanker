"""___Modules_______________________________________________________________"""

# BlipWanker
from .bac_de_tri import *
from .periodic import *
from .ship import *
from .stable import *

# Python
from copy import deepcopy
from enum import Enum

"""___Classes_______________________________________________________________"""

class Data(Enum):

    BAR = bar
    OSCILLATOR = oscillator
    PENTADECATHLON = pentadecathlon
    PLANEUR = planeur
    SQUARE = square
    TOIT = toit

    def __call__(self) -> dict:
        return deepcopy(self.value)
