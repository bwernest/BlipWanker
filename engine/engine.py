"""___Modules_______________________________________________________________"""

# BlipWanker
from .generator.research import Researcher
from .generator.save_manager import SaveManager
from toolbox import *

# Python
import json

"""___Classes_______________________________________________________________"""

class Engine(SaveManager):

    def __init__(self, settings: str = "prod", void: bool = False) -> None:
        with open(f"engine/settings.json") as data:
            self.settings = json.load(data)
        self.save_path = self.settings[settings]["save_path"]
        super().__init__(save_path = self.save_path)
        if void:
            self.void(self.save_path)

    def start(self) -> None:
        infos = self.get_next_dimension()
        self.researcher = Researcher(self.save_path, infos)

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
