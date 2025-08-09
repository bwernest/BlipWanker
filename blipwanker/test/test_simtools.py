"""___Modules_______________________________________________________________"""

# BlipWanker
from blipwanker.engine.data import Data
from blipwanker.engine.simulation.simtools import *
from blipwanker.test import *

"""___Classes_______________________________________________________________"""

class Test_SimTools():

    def test_get_loop(self) -> None:
        loop = get_loop(Data.BAR())
        assertEqual(loop, None)
