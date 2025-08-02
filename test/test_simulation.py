"""___Modules_______________________________________________________________"""

# BlipWanker
from engine.data import Data
from engine.simulation.simulation import JeuDeLaVie
from test.asserts import *

# Python
import numpy as np

"""___Functions_____________________________________________________________"""

def test_empty() -> None:
    simu = JeuDeLaVie()
    assertEqual(simu.grid.grid, {})
    assertEqual(simu.cells, 0)
    assertEqual(simu.live_cells, 0)
    assertEqual(simu.dead_cells, 0)

def test_fill() -> None:
    dico = {"1.0": False, "1.1": True}
    simu = JeuDeLaVie(dico)
    assertDictEqual(simu.grid.grid, dico)
    assertEqual(simu.cells, 2)
    assertEqual(simu.live_cells, 1)
    assertEqual(simu.dead_cells, 1)

def test_get_coords() -> None:
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

def test_get_key() -> None:
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

def test_around() -> None:
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

def test_repr() -> None:
    simu = JeuDeLaVie({"0.0": False, "1.0": True})
    assertIsInstance(repr(simu), str)

def test_update_life1() -> None:
    simu = JeuDeLaVie({"0.0": True, "1.0": True, "0.1": True})
    assertTrue(simu.update_life("0.0"))

def test_update_life2() -> None:
    simu = JeuDeLaVie({"0.0": True})
    assertFalse(simu.update_life("0.0"))

def test_update_dead1() -> None:
    simu = JeuDeLaVie({"1.0": True, "1.1": True, "0.1": True})
    assertTrue(simu.update_life("0.0"))

def test_update_dead2() -> None:
    simu = JeuDeLaVie()
    assertFalse(simu.update_life("0.0"))

def test_compact() -> None:
    simu = JeuDeLaVie({"0.0": True, "1.0": False})
    simu.compact()
    assertDictEqual(simu.grid.grid, {"0.0": True})

def test_case1() -> None:
    simu = JeuDeLaVie(Data.BAR())
    simu.next()
    simu.compact()
    assertDictEqual(simu.grid.grid, {"0.-1": True, "0.0": True, "0.1": True})
    simu.next()
    simu.compact()
    assertDictEqual(simu.grid.grid, Data.BAR())

def test_case2() -> None:
    simu1 = JeuDeLaVie(Data.BAR())
    simu2 = JeuDeLaVie(Data.BAR())
    simu1.next()
    simu1.next()
    simu2.simulate(2)
    assertEqual(simu1, simu2)
    simu1.next()
    assertNotEqual(simu1, simu2)

def test_case3() -> None:
    simu = JeuDeLaVie(Data.OSCILLATOR())
    simu.simulate(3)
    assertEqual(simu.grid.grid, Data.OSCILLATOR())
