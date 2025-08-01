"""___Modules_______________________________________________________________"""

# BlipWanker
from engine.simulation import *

"""___Execution_____________________________________________________________"""

dico = {"1.0": True, "1.1": True, "1.2": True}
game = JeuDeLaVie(dico)

game.simulate(50)
game.display()
