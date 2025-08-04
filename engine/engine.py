"""___Modules_______________________________________________________________"""

# BlipWanker
from .generator.research import Researcher
from .generator.save_manager import SaveManager
from toolbox import *

# Python
import numpy as np
import os
from tqdm import tqdm
from typing import Dict, List

"""___Classes_______________________________________________________________"""

class Engine(SaveManager):

    def __init__(self, void: bool=False) -> None:
        super().__init__()
        if void: self.void()
    
    def start(self) -> None:
        infos = self.get_next_dimension()
        self.researcher = Researcher(infos)

        print(f"Dimensions initialisées : {self.dimensions}")

    def run(self) -> None:
        state = self.researcher.infos["done"]
        dimension = eval(self.researcher.infos["dimension"])
        if state == "True":
            dimension += 1
            self.create_folder(dimension)
            self.researcher.infos = self.get_next_dimension()    
        print(f"Début des recherches en dimension {dimension} !")
        self.researcher.research(bar=True)
