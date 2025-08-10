"""___Modules_______________________________________________________________"""

# BlipWanker
from .toolbox import *

# Python
from typing import List

"""___Functions_____________________________________________________________"""

def get_equivalents(binary_g: str, dimension: int) -> List[str]:
    """
    From a grid binary, finds the equivalents binaries and return them compacted.
    """
    binary_c = get_compact_binary(binary_g)
    equivalents = []
    equivalents += get_Hequi(binary_g, dimension)
    equivalents += get_Vequi(binary_g, dimension)
    equivalents += get_HVequi(binary_g)
    equivalents += get_Oequi(binary_g)
    equivalents = [equivalent for equivalent in equivalents if int(equivalent, 10) > int(binary_c, 10)]
    equivalents = [get_compact_binary(equivalent) for equivalent in equivalents]
    return equivalents

def get_Hequi(binary_g: str, dimension: int) -> str:
    lines = [binary_g[dim:dim+dimension] for dim in range(0, len(binary_g), dimension)]
    symH = "".join(lines[::-1])
    Hequi = [symH] + get_Oequi(symH)
    return symH

def get_Vequi(binary_g: str, dimension: int) -> str:
    columns = [binary_g[dim:dim+1:dimension] for dim in range(0, dimension)]
    symV = "".join(columns[::-1])
    Vequi = [symV] + get_Oequi(symV)
    return symV

def get_HVequi(binary_g: str) -> List[str]:
    symHV = binary_g[::-1]
    HVequi = [symHV] + get_Oequi(symHV)
    return HVequi

def get_Oequi(binary_g: str) -> List[str]:
    Oequi = []
    return Oequi
