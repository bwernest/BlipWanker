"""___Modules_______________________________________________________________"""

# BlipWanker
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
    SQUARE = square

    def __call__(self) -> dict:
        return deepcopy(self.value)
