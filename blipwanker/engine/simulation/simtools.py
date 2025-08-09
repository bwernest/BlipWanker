"""___Modules_______________________________________________________________"""

# BlipWanker
from .simulation import JeuDeLaVie
from ...toolbox import *

# Python
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
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
    game_save = binary_to_game_save(binary_c, dimension)
    loop = get_loop(game_save)

def get_loop(game_save: Dict) -> List[str]:
    simulator = JeuDeLaVie(game_save)
    generations = [simulator.get_save("binary")]

    while True:
        simulator.next()
        binary = simulator.get_save("binary")
        for g, generation in enumerate(generations):
            if binary == generation:
                return generations[g:]
        generations.append(binary)
        if simulator.generation > 1000:
            raise TooMuchIteration("Impossible de déterminer une loop pour cette save.")

def screen_generations(game_save: dict, start: int = 0, end: int = None, duration: int = 10, bar: bool = False) -> List[np.ndarray]:
    """
    Simule des générations à partir de game_save. Selon les paramètres renseignés,
    sauvegarde un certain nombre de grilles.
    Le paramètre end est prioritaire sur duration.
    """
    simulator = JeuDeLaVie(game_save)
    simulator.simulate(start)
    generations = [simulator.get_matrix()]
    max_bounds = simulator.bounds
    all_bounds = [simulator.bounds]

    if end is not None:
        duration = end - start

    for _ in tqdm(range(duration - 1), desc="Simulation", disable=not bar):
        simulator.next()
        generations.append(simulator.get_matrix())
        bounds = simulator.bounds
        all_bounds.append(bounds)
        for key, value in max_bounds.items():
            max_bounds[key] = max(value, bounds[key]) if key.endswith("+") else min(value, bounds[key])

    for g, matrix in enumerate(generations):
        generations[g] = extend_matrix(
            matrix,
            up=abs(max_bounds["y+"] - all_bounds[g]["y+"]),
            down=abs(max_bounds["y-"] - all_bounds[g]["y-"]),
            right=abs(max_bounds["x+"] - all_bounds[g]["x+"]),
            left=abs(max_bounds["x-"] - all_bounds[g]["x-"]),
        )

    return generations

def generate_gif(game_save: dict, n_frames: int = 10, bar: bool = False) -> None:

    # Génération de toutes les matrices à l'avance
    matrices = screen_generations(game_save, duration=n_frames, bar=bar)
    size = matrices[0].shape[0]

    # Création de la figure
    fig, ax = plt.subplots(figsize=(6, 6), dpi=size)
    im = ax.imshow(matrices[0], cmap="inferno", animated=True)
    ax.axis("off")

    # Fonction de mise à jour pour chaque frame
    def update(frame_index):
        im.set_array(matrices[frame_index])
        return [im]

    # Animation
    anim = FuncAnimation(
        fig,
        update,
        frames=n_frames,
        blit=True,
        repeat=True,
    )

    # Sauvegarde en GIF avec PillowWriter
    writer = PillowWriter(fps=2)
    anim.save("animation.gif", writer=writer)
