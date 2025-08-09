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

dimension = 400
matrix = np.random.randint(0, 2, size=(dimension, dimension), dtype=int)
binary, _ = matrix_to_binary(matrix)
game_save = binary_to_game_save(binary, dimension)

# generate_gif(game_save, 100)
generate_gif(Data.TOIT(), 200, bar=True)
