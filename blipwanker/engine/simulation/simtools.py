"""___Modules_______________________________________________________________"""

# BlipWanker
from .simulation import JeuDeLaVie
from ...toolbox import *

# Python
import numpy as np
from typing import Dict, List

"""___Classes_______________________________________________________________"""

def fills_dim(binary_c: str, dimension: int) -> bool:
    """
    Vérifie que le binary utilise tout l'espace
    """

def get_signature(binary_c: str, dimension: int) -> str:
    """
    Identifie la signature d'un binary. Les binaries traités ici survivent à X générations.
    Cependant 2 formes de vies n'ayant pas la même initialisation peuvent aboutir à une
    même espèce mais déphasées en générations.
    Cette fonction trouve la signature, soit une génération partiuclière permettant d'identifier
    et comparer des formes de vies mêmes déphasées.
    """
    game_save = binary_to_game_data(binary_c, dimension)
    loop = get_loop(game_save)

def get_loop(game_save : Dict) -> List[str]:
    simulator = JeuDeLaVie(game_save)
    generations = [simulator.get_save("binary")]

    found = False
    while not found:
        simulator.next()
        binary = simulator.get_save("binary")
        for g, generation in enumerate(generations):
            if binary == generation:
                generations = generations[g:]
                found = True
                break
            else:
                generations.append(binary)
        if simulator.generation > 1000:
            raise TooMuchIteration("Impossible de déterminer une loop pour cette save.")
    return generations
