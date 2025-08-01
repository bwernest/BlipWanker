"""___Modules_______________________________________________________________"""

# BlipWanker
from engine.simulation import *

"""___Execution_____________________________________________________________"""

dico = {"1.0": False, "1.1": True}
grid = BaerDict(dico)

print(list(dico.values()))
print(list(grid.values()))

print()

print(list(dico.values()).count(False))
print(list(grid.values()).count(False))
