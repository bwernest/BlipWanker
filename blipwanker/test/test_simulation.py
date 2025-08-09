"""___Modules_______________________________________________________________"""

# BlipWanker
from blipwanker.engine.data import Data
from blipwanker.engine.simulation.simulation import JeuDeLaVie
from blipwanker.test import *

# Python
import numpy as np

"""___Classes_______________________________________________________________"""

class Test_Simulation():

    def test_empty(self) -> None:
        simu = JeuDeLaVie()
        assertEqual(simu.grid.grid, {})
        assertEqual(simu.cells, 0)
        assertEqual(simu.live_cells, 0)
        assertEqual(simu.dead_cells, 0)

    def test_fill(self) -> None:
        dico = {"1.0": False, "1.1": True}
        simu = JeuDeLaVie(dico)
        assertDictEqual(simu.grid.grid, dico)
        assertEqual(simu.cells, 2)
        assertEqual(simu.live_cells, 1)
        assertEqual(simu.dead_cells, 1)

    def test_get_coords(self) -> None:
        simu = JeuDeLaVie()
        quiz = {
            "1.1": (1, 1),
            "1.0": (1, 0),
            "-1.1": (-1, 1),
            "-1.-1": (-1, -1),
            "-1492.1515": (-1492, 1515),
        }
        for key, value in quiz.items():
            assertEqual(simu.get_coords(key), value)

    def test_get_key(self) -> None:
        simu = JeuDeLaVie()
        quiz = {
            "1.1": (1, 1),
            "1.0": (1, 0),
            "-1.1": (-1, 1),
            "-1.-1": (-1, -1),
            "-1492.1515": (-1492, 1515),
        }
        for key, value in quiz.items():
            assertEqual(simu.get_key(value), key)

    def test_around(self) -> None:
        simu = JeuDeLaVie()
        coords = (0, 0)
        around = simu.get_around(coords)
        expected = np.array(
            [
                [0, 1],
                [1, 1],
                [1, 0],
                [1, -1],
                [0, -1],
                [-1, -1],
                [-1, 0],
                [-1, 1],
            ]
        )
        assertTrue(np.array_equal(around, expected))

    def test_repr(self) -> None:
        simu = JeuDeLaVie({"0.0": False, "1.0": True})
        assertIsInstance(repr(simu), str)

    def test_update_life1(self) -> None:
        simu = JeuDeLaVie({"0.0": True, "1.0": True, "0.1": True})
        assertTrue(simu.update_life("0.0"))

    def test_update_life2(self) -> None:
        simu = JeuDeLaVie({"0.0": True})
        assertFalse(simu.update_life("0.0"))

    def test_update_dead1(self) -> None:
        simu = JeuDeLaVie({"1.0": True, "1.1": True, "0.1": True})
        assertTrue(simu.update_life("0.0"))

    def test_update_dead2(self) -> None:
        simu = JeuDeLaVie()
        assertFalse(simu.update_life("0.0"))

    def test_compact(self) -> None:
        simu = JeuDeLaVie({"0.0": True, "1.0": False})
        simu.compact()
        assertDictEqual(simu.grid.grid, {"0.0": True})

    def test_case1(self) -> None:
        simu = JeuDeLaVie(Data.BAR())
        simu.next()
        simu.compact()
        assertDictEqual(simu.grid.grid, {"0.-1": True, "0.0": True, "0.1": True})
        simu.next()
        simu.compact()
        assertDictEqual(simu.grid.grid, Data.BAR())

    def test_case2(self) -> None:
        simu1 = JeuDeLaVie(Data.BAR())
        simu2 = JeuDeLaVie(Data.BAR())
        simu1.next()
        simu1.next()
        simu2.simulate(2)
        assertEqual(simu1, simu2)
        simu1.next()
        assertNotEqual(simu1, simu2)

    def test_case3(self) -> None:
        simu = JeuDeLaVie(Data.OSCILLATOR())
        simu.simulate(3)
        assertEqual(simu.grid.grid, Data.OSCILLATOR())

    def test_get_matrix1(self) -> None:
        expected = np.array([[1]], dtype=int)
        grid = {"0.0": True}
        game = JeuDeLaVie(grid)
        result = game.get_matrix()
        assertEqual(expected, result)

    def test_get_matrix2(self) -> None:
        expected = np.array([[1, 0, 0, 1]], dtype=int)
        grid = {"0.0": True, "3.0": True}
        game = JeuDeLaVie(grid)
        result = game.get_matrix()
        assertEqual(expected, result)

    def test_get_matrix3(self) -> None:
        expected = np.array([[0, 1], [1, 0]], dtype=int)
        grid = {"0.0": True, "1.1": True}
        game = JeuDeLaVie(grid)
        result = game.get_matrix()
        assertEqual(expected, result)

    def test_get_save_dict(self) -> None:
        grid = {"0.0": True, "1.1": True}
        game = JeuDeLaVie(grid)
        result = game.get_save("dict")
        assertDictEqual(grid, result)

    def test_get_save_binary1(self) -> None:
        expected = "0110"
        grid = {"0.0": True, "1.1": True}
        game = JeuDeLaVie(grid)
        result = game.get_save("binary")
        assertEqual(expected, result)

    def test_get_save_binary2(self) -> None:
        expected = "000000111"
        game = JeuDeLaVie(Data.BAR())
        result = game.get_save("binary")
        assertEqual(expected, result)
