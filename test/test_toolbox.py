"""___Modules_______________________________________________________________"""

# BlipWanker
from toolbox import *
from test.asserts import *

"""___Functions_____________________________________________________________"""

def test_binary_usefull1() -> None:
    binary = "1001"
    dimension = 2
    assertTrue(binary_usefull(binary, dimension))

def test_binary_usefull2() -> None:
    binary = "1000"
    dimension = 2
    assertFalse(binary_usefull(binary, dimension))

def test_binary_usefull3() -> None:
    binary = "100000001"
    dimension = 3
    assertTrue(binary_usefull(binary, dimension))

def test_binary_usefull4() -> None:
    binary = "100010000"
    dimension = 3
    assertFalse(binary_usefull(binary, dimension))
