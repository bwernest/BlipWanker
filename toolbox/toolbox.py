"""___Functions_____________________________________________________________"""

def print_info(text: str, objet: any) -> None:
    render = f"{text} :"
    if isinstance(objet, (int, float, str)):
        render += f" {objet}"
    elif isinstance(objet, (dict)):
        for key, value in objet.items():
            render += f"\n{key} =\t{value}"
    print(render)
