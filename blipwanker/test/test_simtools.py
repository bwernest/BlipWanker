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

    def test_get_loop3(self) -> None:
        expected = [
            "111001010",
            "010011101",
            "011101001",
            "110011100",
        ]
        result = get_loop(Data.PLANEUR())
        assertEqual(4, len(result))
        assertEqual(expected, result)

    def test_screen_generations(self) -> None:
        expected = [
            "000111000",
            "010010010",
        ]
        matrices = screen_generations(Data.BAR(), bar=False)
        result = [matrix_to_binary(matrix)[0] for matrix in matrices]
        assertListEqual(expected, result)
