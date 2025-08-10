"""___Modules_______________________________________________________________"""

# Python
from typing import List

"""___Functions_____________________________________________________________"""

def get_equivalents(binary_g: str) -> List[str]:
    equivalents = []
    equivalents += get_Hequi(binary_g)
    equivalents += get_Vequi(binary_g)
    equivalents += get_Oequi(binary_g)
    return equivalents

def get_Hequi(binary_g: str) -> List[str]:
    Hequi = []
    return Hequi

def get_Vequi(binary_g: str) -> List[str]:
    Vequi = []
    return Vequi

def get_Oequi(binary_g: str) -> List[str]:
    Oequi = []
    return Oequi
