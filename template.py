# file to create the template files for the project in windows operating
# In linux use cookiecutter
import os

dirs = [
    os.path.join("data", "raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True) # making file 
    with open(os.path.join(dir_, ".gitkeep"), "w") as f: # keeping git ignore file to just fill the folder
        pass


files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")
]

for file_ in files:
    with open(file_, "w") as f:
        pass