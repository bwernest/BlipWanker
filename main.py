"""___Modules_______________________________________________________________"""

# BlipWanker
from engine.data import Data
from engine.simulation import *
from toolbox import *

"""___Execution_____________________________________________________________"""

simu = JeuDeLaVie(Data.BAR())
simu.next()
simu.compact()
assert simu.grid.grid == {"0.-1": True, "0.0": True, "0.1": True}
simu.next()
simu.compact()
print(simu.grid.grid)
print(Data.BAR())
assert simu.grid.grid == Data.BAR()