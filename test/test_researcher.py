"""___Modules_______________________________________________________________"""

# BlipWanker
from engine.generator.research import Researcher
from toolbox import *
from test import *

"""___Classes_______________________________________________________________"""

class Test_Researcher():
    
    def test_to_game_save(self) -> None:
        binary = "1111"
        save = binary_to_game_data(binary, 2)
        expected = {"0.0": "True", "1.0": "True", "0.-1": "True", "1.-1": "True"}
        assertDictEqual(save, expected)
