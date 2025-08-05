"""___Modules_______________________________________________________________"""

# BlipWanker
from .generator.research import Researcher
from .generator.save_manager import SaveManager
from toolbox import *

"""___Classes_______________________________________________________________"""

class Engine(SaveManager):

    def __init__(self, void: bool=False) -> None:
        super().__init__()
        if void: self.void()
    
    def start(self) -> None:
        infos = self.get_next_dimension()
        self.researcher = Researcher(infos)

    def run(self) -> None:
        self.start()
        state = self.researcher.done
        dimension = self.researcher.dimension
        if state == "True":
            dimension += 1
            self.create_folder(dimension)
            self.researcher.import_infos(self.get_next_dimension())   
        print(f"Début des recherches en dimension {dimension} !")
        self.researcher.research(bar=True)
