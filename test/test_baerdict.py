"""___Modules_______________________________________________________________"""

# BlipWanker
from engine.simulation.baerdict import BaerDict
from test.asserts import *

"""___Functions_____________________________________________________________"""

def test_init() -> None:
    baer = BaerDict()
    assertDictEqual(baer, {})

def test_import() -> None:
    dico = {"mdr": 5}
    baer = BaerDict(dico)
    assertEqual(baer["mdr"], 5)
    assertFalse(baer["lol"])

def test_repr() -> None:
    dico = {"porco": "rosso"}
    baer = BaerDict(dico)
    assertEqual(repr(dico), repr(baer))

def test_setitem() -> None:
    dico = {"Lewis": "Hamilton"}
    baer = BaerDict()
    baer["Lewis"] = "Hamilton"
    assertDictEqual(dico, baer.grid)

def test_call_data() -> None:
    dico = {"tomate": 1492, "patate": 26}
    baer = BaerDict(dico)
    assertListEqual(sorted(list(baer.keys())), sorted(list(dico.keys())))
    assertListEqual(sorted(list(baer.values())), sorted(list(dico.values())))
    assertListEqual(list(sorted(baer.items())), sorted(list(dico.items())))
