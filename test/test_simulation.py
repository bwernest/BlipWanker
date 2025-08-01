"""___Modules_______________________________________________________________"""

# BlipWanker
from engine.simulation.simulation import JeuDeLaVie

"""___Functions_____________________________________________________________"""

def test_init() -> None:
    simu = JeuDeLaVie()
    assert simu.grid == {}
