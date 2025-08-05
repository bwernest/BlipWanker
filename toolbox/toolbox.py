"""___Modules_______________________________________________________________"""

# Python
import numpy as np

"""___Functions_____________________________________________________________"""

def to_base10(number: str) -> int:
    if number in ["0", "1"]:
        return eval(number)
    else :
        return eval(number[0])*2**(len(number)-1) + to_base10(number[1:])

def super_eval(number: str) -> int:
    while number.startswith("0"):
        number = number[1:]
    return 0 if number == "" else eval(number)

def print_info(text: str, objet: any) -> None:
    render = f"{text} :"
    if isinstance(objet, (int, float, str)):
        render += f" {objet}"
    elif isinstance(objet, (dict)):
        for key, value in objet.items():
            render += f"\n{key} =\t{value}"
    print(render)

def write_txt(path: str, text: str, extension: str = "txt", method: str = "w") -> None:
    with open(f"{path}.{extension}", method) as txt:
        txt.write(text)

def read_txt(path: str, extension: str = "txt") -> list[str]:
    with open(f"{path}.{extension}", "r") as txt:
        data = txt.readlines()
    return data

def get_dict_to_text(dico: dict) -> str:
    text = []
    for key, value in dico.items():
        text.append(f"{key}={value}")
    return "\n".join(text)

def binary_to_game_data(binary: str, dimension: int) -> dict:
    game_save = {}
    for s, state in enumerate(binary):
        if state == "1":
            X = (s % dimension)
            Y = -(s // dimension)
            game_save[f"{X}.{Y}"] = "True"
    return game_save

def binary_usefull(binary: str, dimension: int) -> bool:
    """
    A optimiser
    """
    matrix = np.zeros(shape=(dimension**2))
    for c, charac in enumerate(binary):
        matrix[c] = eval(charac)
    matrix = np.reshape(matrix, (dimension, dimension))
    if np.sum(matrix[0, :]) > 0 and np.sum(matrix[-1, :]) > 0 or np.sum(matrix[:, 0]) > 0 and np.sum(matrix[:, -1]):
        return True
    else:
        return False

def get_grid_binary(binary: str, dimension: int) -> str:
    return "0"*( dimension**2 - len(binary) ) + binary

def get_compact_binary(binary: str) -> str:
    while binary.startswith("0"): binary = binary[1:]
    return binary if binary != "" else "0"
