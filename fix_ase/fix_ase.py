from pathlib import Path
import ase
import shutil

# print(Path.joinpath(Path(ase.__path__[0]), 'io/espresso.py'))
shutil.copy2("espresso.py", Path.joinpath(Path(ase.__path__[0]), 'io/espresso.py'))
