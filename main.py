"""___Modules_______________________________________________________________"""

# BlipWanker
from engine import data
from engine.simulation import *

"""___Execution_____________________________________________________________"""

dico = data.pentadecathlon
game = JeuDeLaVie(dico)

game.simulate(20, debug=False, display=True)
game.display()
