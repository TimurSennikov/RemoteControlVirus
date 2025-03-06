import os
import random

def canaccess(path):
    try:
        os.listdir(path)
        return True
    except Exception as e:
        return False

def only_dirs(start, l: list):
    a = []
    for dir in l:
        p = os.path.join(start, dir)
        if os.path.isdir(p) and canaccess(p):
            a.append(dir)

    return a

def random_path():
    start = os.path.abspath(os.getenv("HOMEPATH"))

    while True:
        dirs = only_dirs(start, os.listdir(start))

        if len(dirs) <= 0:
            break

        dir = dirs[random.randint(0, len(dirs)-1)]
        start = os.path.join(start, dir)

    return start