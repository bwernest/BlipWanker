"""___Modules_______________________________________________________________"""

# BlipWanker
from engine.simulation.baerdict import BaerDict

"""___Functions_____________________________________________________________"""

def test_init() -> None:
    baer = BaerDict()
    assert baer == {}

def test_import() -> None:
    dico = {"mdr": 5}
    baer = BaerDict(dico)
    assert baer["mdr"] == 5
    assert baer["lol"] == False

def test_repr() -> None:
    dico = {"porco": "rosso"}
    baer = BaerDict(dico)
    assert repr(dico) == repr(baer)
