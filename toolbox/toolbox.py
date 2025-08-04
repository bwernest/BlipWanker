"""___Functions_____________________________________________________________"""

def to_base2(number: int) -> str:
    if number in [0, 1]:
        return str(number)
    else :
        quotient = number // 2
        reste = number - quotient * 2
        new_number = number // 2
        return to_base2(new_number) + str(reste)

def to_base10(number: str) -> int:
    if number in ["0", "1"]:
        return eval(number)
    else :
        return eval(number[0])*2**(len(number)-1) + to_base10(number[1:])

def super_eval(number: str) -> int:
    while number.startswith("0"):
        number = number[1:]
    return eval(number)

def print_info(text: str, objet: any) -> None:
    render = f"{text} :"
    if isinstance(objet, (int, float, str)):
        render += f" {objet}"
    elif isinstance(objet, (dict)):
        for key, value in objet.items():
            render += f"\n{key} =\t{value}"
    print(render)

def write_txt(path: str, text: str, extension: str = "txt") -> None:
    with open(f"{path}.{extension}", "w") as txt:
        txt.write(text)

def read_txt(path: str, extension: str = "txt") -> list[str]:
    with open(f"{path}.{extension}", "r") as txt:
        data = txt.readlines()
    return data

def get_dict_text(dico: dict) -> str:
    text = []
    for key, value in dico.items():
        text.append(f"{key}={value}")
    return "\n".join(text)

def binary_to_game_data(binary: str, dimension: int) -> dict:
    game_save = {}
    binary = "0"*(dimension**2-len(binary))+binary
    for s, state in enumerate(binary):
        if state == "1":
            X = (s % dimension)
            Y = -(s // dimension)
            game_save[f"{X}.{Y}"] = "True"
    return game_save
