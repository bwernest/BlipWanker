"""___Modules_______________________________________________________________"""

# BlipWanker
from engine.data import Data
from engine.simulation import *
from test.asserts import *
from toolbox import *

"""___Execution_____________________________________________________________"""

simu1 = JeuDeLaVie(Data.BAR())
simu2 = JeuDeLaVie(Data.BAR())
simu1.next()
simu1.next()
simu2.simulate(2)
assertEqual(simu1, simu2)
simu1.next()
assertNotEqual(simu1, simu2)
