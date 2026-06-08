import os, shutil
from pathlib import Path

CATEGORIES = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "videos": [".mp4", ".mkv", ".avi"],
    "audio": [".mp3", ".wav", ".flac"],
    "archives": [".zip", ".tar", ".gz"],
}

def organize(path):
    for f in Path(path).iterdir():
        if f.is_file():
            cat = next((c for c, exts in CATEGORIES.items() if f.suffix.lower() in exts), "others")
            dest = Path(path) / cat
            dest.mkdir(exist_ok=True)
            shutil.move(str(f), dest / f.name)
            print(f"Moved: {f.name} -> {cat}/")
