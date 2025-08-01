"""___Modules_______________________________________________________________"""

# BlipWanker
from engine.simulation.simulation import JeuDeLaVie

# Python
import numpy as np

"""___Functions_____________________________________________________________"""

def test_empty() -> None:
    simu = JeuDeLaVie()
    assert simu.grid == {}
    assert simu.cells == 0
    assert simu.live_cells == 0
    assert simu.dead_cells == 0

def test_fill() -> None:
    dico = {"1.0": False, "1.1": True}
    simu = JeuDeLaVie(dico)
    assert simu.grid.grid == dico
    assert simu.cells == 2
    assert simu.live_cells == 1
    assert simu.dead_cells == 1

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
        assert simu.get_coords(key) == value

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
        assert simu.get_key(value) == key

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
    assert np.array_equal(around, expected)
