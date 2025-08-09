"""___Modules_______________________________________________________________"""

# BlipWanker
from engine.generator.save_manager import SaveManager
from test import *

"""___Classes_______________________________________________________________"""

class Test_SaveManager():

    def test_init(self) -> None:
        sm = SaveManager(save_path)

    def test_repr(self) -> None:
        expected = "<SaveManager>"
        sm = SaveManager(save_path)
        result = repr(sm)
        assertEqual(expected, result)
