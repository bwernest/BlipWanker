"""___Modules_______________________________________________________________"""

# BlipWanker
from ..simulation.simulation import JeuDeLaVie
from .save_manager import SaveManager
from toolbox import *

# Python
import numpy as np
import os
from tqdm import tqdm
from typing import Dict, List

"""___Classes_______________________________________________________________"""

class Researcher(SaveManager):

    def __init__(self, infos: dict) -> None:
        self.infos = infos
    
    def research(self) -> None:
        dimension = eval(self.infos["dimension"])
        current = eval(self.infos["last"]) + 1
        last = 2**(dimension**2)
        n_ok = eval(self.infos["ok"])
        n_nook = eval(self.infos["nook"])

        ok_list = self.get_ok(dimension)

        for k in tqdm(range(current, last+1)):
            binary = np.binary_repr(k)
            game_save = binary_to_game_data(binary, dimension)

            game = JeuDeLaVie(game_save)
            game.simulate(100)
            if game.live_cells > 0:
                ok_list.append(binary)
                n_ok += 1
            else:
                n_nook += 1
            
            self.infos["ok"] = str(n_ok)
            self.infos["nook"] = str(n_nook)
            self.infos["last"] = str(k)
        
        self.infos["done"] = "True"
        self.save_ok(dimension, ok_list)
        self.save_infos(self.infos, dimension)
