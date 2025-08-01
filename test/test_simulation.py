"""___Modules_______________________________________________________________"""

# BlipWanker
from engine.simulation.simulation import JeuDeLaVie

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
