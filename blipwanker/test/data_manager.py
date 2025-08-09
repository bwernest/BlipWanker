"""___Modules_______________________________________________________________"""

# Python
import json
import os
import shutil

"""___Functions_____________________________________________________________"""

def void(fonction):
    def clean_test_folder(*args, **kwargs):
        if os.path.isdir(save_path):
            shutil.rmtree(save_path)
        os.makedirs(save_path)
        result = fonction(*args, **kwargs)
        shutil.rmtree(save_path)
        os.makedirs(save_path)
        return result
    return clean_test_folder

def import_settings() -> dict:
    with open(f"blipwanker/engine/settings.json") as data:
        return json.load(data)

save_path = import_settings()["test"]["save_path"]
