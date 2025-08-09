"""___Modules_______________________________________________________________"""

# BlipWanker
from blipwanker.engine.data import Data
from blipwanker.engine.engine import Engine
from blipwanker.engine.simulation import *
from blipwanker.test.asserts import *
from blipwanker.toolbox import *

# Python
import numpy as np

"""___Execution_____________________________________________________________"""

loop = get_loop(Data.BAR())

print_info("Loop", loop)
print(f"Loop de taille {len(loop)}")
