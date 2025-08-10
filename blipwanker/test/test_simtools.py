"""___Modules_______________________________________________________________"""

# BlipWanker
from blipwanker.engine.data import Data
from blipwanker.engine.simulation.simtools import *
from blipwanker.test import *

# Python
import pytest

"""___Classes_______________________________________________________________"""

class Test_SimTools():

    def test_get_loop1(self) -> None:
        expected = [
            "1111",
        ]
        loop, dimension = get_loop(Data.SQUARE())
        assertEqual(2, dimension)
        assertEqual(1, len(loop))
        assertEqual(expected, loop)

    def test_get_loop2(self) -> None:
        expected = [
            "000000111",
            "001001001",
        ]
        loop, dimension = get_loop(Data.BAR())
        assertEqual(3, dimension)
        assertEqual(2, len(loop))
        assertEqual(expected, loop)

    def test_get_loop3(self) -> None:
        expected = [
            "111001010",
            "010011101",
            "011101001",
            "110011100",
        ]
        loop, dimension = get_loop(Data.PLANEUR())
        assertEqual(3, dimension)
        assertEqual(4, len(loop))
        assertEqual(expected, loop)

    def test_get_loop4(self) -> None:
        with pytest.raises(SimulationDead):
            game_save = {"0.0": True}
            _ = get_loop(game_save)

    def test_screen_generations(self) -> None:
        expected = [
            "000111000",
            "010010010",
        ]
        matrices = screen_generations(Data.BAR(), bar=False)
        result = [matrix_to_binary(matrix)[0] for matrix in matrices]
        assertListEqual(expected, result)

    def test_gen_fills_dim1(self) -> None:
        binaries = [
            "0011",
            "0101",
            "1010",
            "1001",
        ]
        expected = [True] * len(binaries)
        result = [gen_fills_dim(binary, int(len(binaries[0])**0.5))
                  for binary in binaries]
        assertListEqual(expected, result)

    def test_gen_fills_dim2(self) -> None:
        binaries = [
            "001001010",
            "000000101",
            "111111111",
            "100000001",
            "100010100",
        ]
        expected = [True] * len(binaries)
        result = [gen_fills_dim(binary, int(len(binaries[0])**0.5))
                  for binary in binaries]
        assertListEqual(expected, result)

    def test_gen_fills_dim3(self) -> None:
        binaries = [
            "100000000",
            "010110000",
            "000010000",
            "000011011",
        ]
        expected = [False] * len(binaries)
        result = [gen_fills_dim(binary, int(len(binaries[0])**0.5))
                  for binary in binaries]
        assertListEqual(expected, result)

    def test_loop_fills_dim1(self) -> None:
        loop, dimension = get_loop(Data.BAR())
        assertEqual(3, dimension)
        assertTrue(loop_fills_dim(loop, 3))

    def test_loop_fills_dim2(self) -> None:
        loop, dimension = get_loop(Data.BAR())
        assertEqual(3, dimension)
        assertTrue(loop_fills_dim(loop, 4))
