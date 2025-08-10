"""___Modules_______________________________________________________________"""

# BlipWanker
from blipwanker.test import *
from blipwanker.toolbox import *

# Python
import os

"""___Classes_______________________________________________________________"""

class Test_Equivalents():

    def test_get_Hequi1(self) -> None:
        binary_g = "0011"
        expected = "1100"
        result = get_Hequi(binary_g, 2)
        assertEqual(expected, result)

    def test_get_Hequi2(self) -> None:
        binary_g = "111001000"
        expected = "000001111"
        result = get_Hequi(binary_g, 3)
        assertEqual(expected, result)

    def test_get_Hequi3(self) -> None:
        binary_g = "1"
        expected = "1"
        result = get_Hequi(binary_g, 1)
        assertEqual(expected, result)

    def test_get_Vequi1(self) -> None:
        binary_g = "1010"
        expected = "0101"
        result = get_Vequi(binary_g, 2)
        assertEqual(expected, result)
