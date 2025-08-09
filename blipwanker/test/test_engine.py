"""___Modules_______________________________________________________________"""

# BlipWanker
from blipwanker.engine.engine import Engine
from blipwanker.test import *

# Python
import os

"""___Classes_______________________________________________________________"""

class Test_Engine():

    def test_init(self) -> None:
        eng = Engine(settings="test")
    
    def test_init_void(self) -> None:
        eng = Engine(settings="test", void=False)
        eng.start()
        eng.run()
        eng = Engine(settings="test", void=True)
        files = os.listdir(save_path)
        expected = []
        assertListEqual(expected, files)

    def test_start(self) -> None:
        eng = Engine(settings="test")
        eng.start()

    def test_run(self) -> None:
        eng = Engine(settings="test")
        eng.start()
        eng.run()
