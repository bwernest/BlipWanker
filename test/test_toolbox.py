"""___Modules_______________________________________________________________"""

# BlipWanker
from toolbox import *
from test.asserts import *

"""___Classes_______________________________________________________________"""

class Test_Toolbox():

    def test_binary_usefull1(self) -> None:
        binary = "1001"
        dimension = 2
        assertTrue(binary_usefull(binary, dimension))

    def test_binary_usefull2(self) -> None:
        binary = "1000"
        dimension = 2
        assertFalse(binary_usefull(binary, dimension))

    def test_binary_usefull3(self) -> None:
        binary = "100000001"
        dimension = 3
        assertTrue(binary_usefull(binary, dimension))

    def test_binary_usefull4(self) -> None:
        binary = "100010000"
        dimension = 3
        assertFalse(binary_usefull(binary, dimension))

    def test_get_compact_binary1(self) -> None:
        binary_g = "0001"
        result = get_compact_binary(binary_g)
        expected = "1"
        assertEqual(expected, result)

    def test_get_compact_binary2(self) -> None:
        binary_g = "000100101"
        expected = "100101"
        result = get_compact_binary(binary_g)
        assertEqual(expected, result)

    def test_get_compact_binary3(self) -> None:
        binary_g = "0"
        expected = "0"
        result = get_compact_binary(binary_g)
        assertEqual(expected, result)

    def test_get_grid_binary1(self) -> None:
        dimension = 2
        binary = "111"
        expected = "0111"
        result = get_grid_binary(binary, dimension)
        assertEqual(expected, result)

    def test_get_grid_binary2(self) -> None:
        dimension = 2
        binary = "1101"
        expected = "1101"
        result = get_grid_binary(binary, dimension)
        assertEqual(expected, result)

    def test_get_grid_binary3(self) -> None:
        dimension = 4
        binary = "011000100"
        expected = "0000000011000100"
        result = get_grid_binary(binary, dimension)
        assertEqual(expected, result)

    def test_to_base10(self) -> None:
        numbers =  ["0", "1", "10", "1101"]
        expected = [ 0,   1,    2,     13 ]
        result = [to_base10(number) for number in numbers]
        assertListEqual(expected, result)

    def test_super_eval(self) -> None:
        numbers = ["0", "01", "26", "0.89", "01492.15150"]
        expected = [0, 1, 26, 0.89, 1492.1515]
        result = [super_eval(number) for number in numbers]
        assertListEqual(expected, result)    

    def test_get_dict_to_text(self) -> None:
        dico = {"mdr": 5, 26: "lol"}
        expected = "mdr=5\n26=lol"
        result = get_dict_to_text(dico)
        assertEqual(expected, result)
