"""___Classes_______________________________________________________________"""

class BlipWankerError(Warning):
    pass

class SimulationDead(BlipWankerError):
    pass

class TooMuchIteration(BlipWankerError):
    pass
