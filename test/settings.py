"""___Modules_______________________________________________________________"""

# Python
import os
import shutil

"""___Data__________________________________________________________________"""

test_folder: str = "test/test_data"

"""___Functions_____________________________________________________________"""

def void(fonction):
    def clean_test_folder(*args, **kwargs):
        if os.path.isdir(test_folder):
            shutil.rmtree(test_folder)
        os.makedirs(test_folder)
        result = fonction(*args, **kwargs)
        shutil.rmtree(test_folder)
        return result
    return clean_test_folder
