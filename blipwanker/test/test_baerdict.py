"""___Modules_______________________________________________________________"""

# BlipWanker
from blipwanker.engine.simulation.baerdict import BaerDict
from blipwanker.test import *

"""___Classes_______________________________________________________________"""

class Test_Baerdict():

    def test_init(self) -> None:
        baer = BaerDict()
        assertDictEqual(baer, {})

    def test_eq(self) -> None:
        dico = {"oui": "non"}
        baer1 = BaerDict(dico)
        baer2 = BaerDict(dico)
        assertEqual(baer1, baer2)
        baer1["lol": "mdr"]
        assertNotEqual(baer1, baer2)

    def test_import(self) -> None:
        dico = {"mdr": 5}
        baer = BaerDict(dico)
        assertEqual(baer["mdr"], 5)
        assertFalse(baer["lol"])

    def test_repr(self) -> None:
        dico = {"porco": "rosso"}
        baer = BaerDict(dico)
        assertEqual(repr(dico), repr(baer))

    def test_setitem(self) -> None:
        dico = {"Lewis": "Hamilton"}
        baer = BaerDict()
        baer["Lewis"] = "Hamilton"
        assertDictEqual(dico, baer.grid)

    def test_call_data(self) -> None:
        dico = {"tomate": 1492, "patate": 26}
        baer = BaerDict(dico)
        assertListEqual(sorted(list(baer.keys())), sorted(list(dico.keys())))
        assertListEqual(sorted(list(baer.values())),
                        sorted(list(dico.values())))
        assertListEqual(list(sorted(baer.items())), sorted(list(dico.items())))
