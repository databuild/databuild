from glob import glob


def multiglob(*patterns):
    files_grabbed = []
    [files_grabbed.extend(glob(pattern)) for pattern in patterns]
    return files_grabbed