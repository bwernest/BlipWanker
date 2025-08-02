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
