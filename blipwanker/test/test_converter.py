"""___Modules_______________________________________________________________"""

# BlipWanker
from blipwanker.toolbox import *
from blipwanker.test import *

"""___Classes_______________________________________________________________"""

class Test_Converter():

    def test_binary_to_game_save(self) -> None:
        binary = "1111"
        save = binary_to_game_save(binary, 2)
        expected = {"0.0": "True", "1.0": "True",
                    "0.-1": "True", "1.-1": "True"}
        assertDictEqual(save, expected)

    def test_matrix_to_binary1(self) -> None:
        matrix = np.zeros((3, 3), dtype=int)
        expected = "0" * 9
        result, dimension = matrix_to_binary(matrix)
        assertEqual(3, dimension)
        assertEqual(expected, result)

    def test_matrix_to_binary2(self) -> None:
        matrix = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=int)
        expected = "010101010"
        result, dimension = matrix_to_binary(matrix)
        assertEqual(3, dimension)
        assertEqual(expected, result)

    def test_matrix_to_binary3(self) -> None:
        matrix = np.ones((2, 2), dtype=int)
        expected = "1111"
        result, dimension = matrix_to_binary(matrix)
        assertEqual(2, dimension)
        assertEqual(expected, result)

    def test_game_save_to_matrix1(self) -> None:
        game_save = {"0.0": True}
        expected = np.array([[1]], dtype=int)
        result = game_save_to_matrix(game_save)
        assertEqual(expected, result)

    def test_game_save_to_matrix2(self) -> None:
        game_save = {"1492.1515": True}
        expected = np.array([[1]], dtype=int)
        result = game_save_to_matrix(game_save)
        assertEqual(expected, result)

    def test_game_save_to_matrix3(self) -> None:
        game_save = {"0.0": True, "1492.1515": False}
        expected = np.array([[1]], dtype=int)
        result = game_save_to_matrix(game_save)
        assertEqual(expected, result)

    def test_game_save_to_matrix4(self) -> None:
        game_save = {"0.0": True, "2.2": True}
        expected = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=int)
        result = game_save_to_matrix(game_save)
        assertEqual(expected, result)
