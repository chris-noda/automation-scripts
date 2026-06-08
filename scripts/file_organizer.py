import os, shutil
from pathlib import Path

def organize(path):
    for f in Path(path).iterdir():
        if f.is_file():
            ext = f.suffix.lower()
            dest = Path(path) / (ext[1:] if ext else "others")
            dest.mkdir(exist_ok=True)
            shutil.move(str(f), dest / f.name)
