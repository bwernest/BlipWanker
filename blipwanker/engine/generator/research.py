"""___Modules_______________________________________________________________"""

# BlipWanker
from .analysor import Analysor
from .save_manager import SaveManager
from ..simulation.simulation import JeuDeLaVie
from ...toolbox import *

# Python
import numpy as np
from tqdm import tqdm

"""___Classes_______________________________________________________________"""

class Researcher(SaveManager, Analysor):

    done: str
    dimension: int
    last: int
    n_ok: int
    n_nook: int

    def __init__(self, save_path: str, infos: dict) -> None:
        super().__init__(save_path)
        self.import_infos(infos)

    def import_infos(self, infos: dict) -> None:
        for element in ["dimension", "last", "ok", "nook"]:
            self.__setattr__(element, eval(infos[element]))
        self.done = infos["done"]
        self.ok_list = self.get_ok(self.dimension)
        self.nook_list = self.get_nook(self.dimension)

    def export_infos(self) -> None:
        infos = {element: str(self.__getattribute__(element))
                 for element in ["done", "dimension", "last", "ok", "nook"]}
        self.save_infos(infos, self.dimension)

    def research(self, bar: bool = False) -> None:

        final = 2**(self.dimension**2)
        print(f"Démarrage recherche de {self.last} à {final}")
        for k in tqdm(range(self.last, final), disable=not bar):
            self.last += 1
            binary_c = np.binary_repr(k)

            # ___Entry_filters___
            # Known nook binary
            if binary_c in self.nook_list:
                continue
            # Unfilled dimension
            binary_g = get_grid_binary(binary_c, self.dimension)
            if not gen_fills_dim(binary_g, self.dimension):
                self.nook += 1
                continue

            # Simulation
            game_grid = binary_to_game_save(binary_g, self.dimension)
            if self.simulation(game_grid):
                self.simulation_succeed(binary_g)
            else:
                self.simulation_failed(binary_g)

        self.done = True
        self.export_infos()

    def simulation_succeed(self, binary_g: str) -> None:
        binary_c = get_compact_binary(binary_g)
        self.ok_list.append(binary_c)
        equivalents += get_equivalents(binary_g)
        self.nook_list += equivalents
        self.nook += len(equivalents)

    def simulation_failed(self, binary_g: str) -> None:
        self.nook_list += get_equivalents(binary_g)
        self.nook += 1

    def simulation(self, game_grid: dict) -> bool:
        game = JeuDeLaVie(game_grid)
        game.simulate(100, bar=False)
        return game.live_cells > 0
