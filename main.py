"""___Modules_______________________________________________________________"""

# BlipWanker
from engine import data
from engine.simulation import *
from toolbox import *

"""___Execution_____________________________________________________________"""

dico = data.planeur
game = JeuDeLaVie(dico)

game.simulate(500, debug=False, display=False)
game.display()

# print_info("Grille finale", game.grid.grid)
