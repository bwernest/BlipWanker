"""___Modules_______________________________________________________________"""

# BlipWanker
from engine.simulation.baerdict import BaerDict

"""___Execution_____________________________________________________________"""

dico = {"1.1": True}
dico = BaerDict(dico)

print(dico["1.2"])
print(dico["1.1"])

print(dico)
