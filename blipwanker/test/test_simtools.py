"""___Modules_______________________________________________________________"""

# BlipWanker
from blipwanker.engine.data import Data
from blipwanker.engine.simulation.simtools import *
from blipwanker.test import *

"""___Classes_______________________________________________________________"""

class Test_SimTools():

    def test_get_loop1(self) -> None:
        expected = [
            "1111",
        ]
        result = get_loop(Data.SQUARE())
        assertEqual(1, len(result))
        assertEqual(expected, result)

    def test_get_loop2(self) -> None:
        expected = [
            "000000111",
            "001001001",
        ]
        result = get_loop(Data.BAR())
        assertEqual(2, len(result))
        assertEqual(expected, result)
