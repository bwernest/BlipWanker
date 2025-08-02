"""___Modules_______________________________________________________________"""

# BlipWanker
from toolbox import *

# Python
import numpy as np
import os
from tqdm import tqdm
from typing import Dict, List

"""___Classes_______________________________________________________________"""

class Generator():

    binary_path : str = "save/binary"
    models_path : str = "save/models"

    def __init__(self) -> None:
        self.binary_list = os.listdir(self.binary_path)
        self.models_list = os.listdir(self.models_path)
    
    def __repr__(self) -> str:
        return f"Generator :\nbinary = {len(self.binary_list)}\nmodels = {len(self.models_list)}"

    def generate_binaries(self, dimension: int) -> None:
        if f"{self.get_file_title(dimension)}.txt" in self.binary_list:
            return None
        self.oubliettes = []
        binaries = []
        total = to_base10("1"*dimension**2)+1
        for k in tqdm(range(total), desc=f"<Dim{dimension}>"):
            b = to_base2(k)
            if True:
            # if self.check(b, dimension):
                binaries.append(b)
        self.export_binary(binaries, dimension)

    def check(self, binary: str, dim: int) -> bool:
        if binary in self.oubliettes:
            return False
        for equivalent in self.get_equivalents(binary, dim):
            self.oubliettes.append(equivalent)
        return True
    
    def get_equivalents(self, binary: str, dim: int) -> None:
        matrix = self.to_matrix(binary, dim)

    def to_matrix(self, binary: str, dim: int) -> np.ndarray:
        matrix = np.zeros((dim, dim))
        for state in binary:
            pass

    def void(self) -> None:
        for file in self.binary_list:
            os.remove(self.binary_path+"/"+file)
        for file in self.models_list:
            os.remove(self.models_path+"/"+file)
        self.binary_list = []
        self.models_list = []

    def export_binary(self, binaries: List[str], dim: int) -> None:
        file_title = self.get_file_title(dim)
        file_path = f"{self.binary_path}/{file_title}"
        for b, binary in enumerate(binaries):
            binaries[b] = "0"*(dim**2-len(binary)) + binary
        write_txt(file_path, "\n".join(binaries))
        self.binary_list.append(f"{file_title}.txt")
    
    def get_file_title(self, dim: int) -> str:
        dim = "0"*(5-len(str(dim)))+str(dim)
        return f"Binaries{dim}"
