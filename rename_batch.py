from pathlib import Path

def rename_batch(path, prefix="file", start=1):
    files = sorted(Path(path).iterdir())
    for i, f in enumerate(files, start):
        if f.is_file():
            new_name = f"{prefix}_{i:03d}{f.suffix}"
            f.rename(f.parent / new_name)
            print(f"Renamed: {f.name} -> {new_name}")
