import os
from pprint import pprint
from pathlib import Path
from os import error

# pprint(dir(os))
print("getcwd, Path.resolve")
pprint(curdir := os.getcwd())
p = Path(curdir)
pprint(p.resolve())
normalized_path = p.resolve().as_posix()
pprint(normalized_path)
os.chdir(normalized_path)

print("\nmkdir, rmdir")
try:
    os.makedirs("./test/dir")
except FileExistsError as exc:
    pprint(exc)
pprint(os.listdir())
print("\nrmdir")
try:
    os.rmdir("./test/dir")
    os.rmdir("./test")
except FileNotFoundError as exc:
    pprint(exc)
pprint(os.listdir())

print(os.listdir(os.getcwd()))

