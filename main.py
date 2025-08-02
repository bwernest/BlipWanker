"""___Modules_______________________________________________________________"""

# BlipWanker
from engine.data import Data
from engine.generator.generator import Generator
from engine.simulation import *
from test.asserts import *
from toolbox import *

# Python
import numpy as np

"""___Execution_____________________________________________________________"""

gen = Generator()

print(gen.binary_list)

for k in range(1, 6) :
    gen.generate_binaries(k)

print(gen.binary_list)
