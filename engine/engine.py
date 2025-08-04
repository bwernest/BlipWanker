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

    def __init__(self) -> None:
        super().__init__()
    
    def start(self) -> None:
        infos = self.get_next_dimension()
        self.researcher = Researcher(infos)

        print(f"Dimensions initialisées : {self.dimensions}")
        print(f"Dimension en cours de recherche : {infos["dimension"]}")

    def run(self) -> None:
        self.researcher.research()
