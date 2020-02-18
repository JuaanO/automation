import os

#Como crear un directorio asi exista..
from pathlib import Path
Path("directory").mkdir(parents=True, exist_ok=True)
