"""___Modules_______________________________________________________________"""

# BlipWanker
from toolbox import *

# Python
import os
from typing import Dict, List

"""___Classes_______________________________________________________________"""

class SaveManager():

    save_path : str = "save"

    folder_name : str = "Dimension"
    folder_num_len : int = 5

    file_ok : str = "PatternOK"
    file_nook : str = "PatternNOOK"
    file_infos : str = "Infos"

    def __init__(self) -> None:
        dimensions_folders = os.listdir(self.save_path)
        self.dimensions : List[int] = []
        for folder in dimensions_folders:
            self.dimensions.append(super_eval(folder[-self.folder_num_len:]))
    
    def __repr__(self) -> str:
        return f"<Generator>"
    
    def get_next_dimension(self) -> int:
        finished = True
        dimension = 1
        while finished:
            if dimension in self.dimensions:
                infos = self.get_infos(dimension)
                if infos["done"] == "True":
                    dimension += 1
                else:
                    finished = False
            else:
                finished = False
                self.create_folder(dimension)
        return self.get_infos(dimension)

    def create_folder(self, dimension) -> None:
        new_folder_name = self.save_path+"/"+self.folder_name+"0"*(self.folder_num_len-len(str(dimension)))+str(dimension)
        os.makedirs(new_folder_name)
        infos = {"done": "False", "last": "0", "ok": "0", "nook": "0", "dimension": str(dimension)}
        write_txt(new_folder_name+"/"+self.file_infos, get_dict_text(infos))
        write_txt(new_folder_name+"/"+self.file_ok, "")
        write_txt(new_folder_name+"/"+self.file_nook, "")

    def get_infos(self, dimension: int) -> Dict:
        folder_name = f"{self.folder_name}{"0"*(self.folder_num_len-len(str(dimension)))}{dimension}"
        text = read_txt(self.save_path+"/"+folder_name+"/"+self.file_infos)
        infos = {}
        for line in text:
            key, value = line.split("=")
            if "\n" in value : value = value[:-1]
            infos[key] = value
        return infos
    
    def save_infos(self, dico: dict, dimension: int) -> None:
        text = get_dict_text(dico)
        write_txt(self.save_path+"/"+self.get_folder_name(dimension)+"/"+self.file_infos, text)

    def void(self) -> None:
        for dimension in self.dimensions:
            folder_path = self.save_path+"/"+self.get_folder_name(dimension)
            for file in os.listdir(folder_path):
                os.remove(folder_path+"/"+file)
            print(f"J'ai viré {dimension}")
            os.removedirs(folder_path)
        self.dimensions = []

    def get_ok(self, dimension: int) -> List[str]:
        file_name = self.save_path+"/"+self.get_folder_name(dimension)+"/"+self.file_ok
        return read_txt(file_name)

    def save_ok(self, dimension: int, save: List[str]) -> None:
        file_name = self.save_path+"/"+self.get_folder_name(dimension)+"/"+self.file_ok
        write_txt(file_name, "\n".join(save))

    def get_nook(self, dimension: int) -> List[str]:
        pass

    def get_folder_name(self, dimension: int) -> str:
        return self.folder_name+"0"*(self.folder_num_len-len(str(dimension)))+str(dimension)
