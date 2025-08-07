"""___Modules_______________________________________________________________"""

# BlipWanker
from toolbox import *
from test import *

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
        numbers = ["0", "1", "10", "1101"]
        expected = [0, 1, 2, 13]
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

    @void
    def test_write_txt1(self) -> None:
        text = "Bonsoir"
        write_txt(save_path+"/"+"lol", text)
    
    @void
    def test_write_txt2(self) -> None:
        text = "Bonsoir"
        write_txt(save_path+"/"+"lol", text)
        write_txt(save_path+"/"+"lol", text, "a")
    
    @void
    def test_write_txt3(self) -> None:
        text = "Bonsoir"
        write_txt(save_path+"/"+"lol", text, "a")
    
    @void
    def test_read_txt(self) -> None:
        text = "Bonsoir"
        write_txt(save_path+"/"+"lol", text)
        data = read_txt(save_path+"/"+"lol")
        assertEqual(text, data[0])

    def test_to_game_save(self) -> None:
        binary = "1111"
        save = binary_to_game_data(binary, 2)
        expected = {"0.0": "True", "1.0": "True", "0.-1": "True", "1.-1": "True"}
        assertDictEqual(save, expected)

    def test_print_info1(self, capsys) -> None:
        print_info("5", 5)
        result = capsys.readouterr()
        expected = "5 : 5\n"
        assertIn(expected, result)

    def test_print_info2(self, capsys) -> None:
        print_info("Mois", {"Janvier": 1, "Février": "Quoicoubeh"})
        result = capsys.readouterr()
        expected = "Mois :\nJanvier =\t1\nFévrier =\tQuoicoubeh\n"
        assertIn(expected, result)
