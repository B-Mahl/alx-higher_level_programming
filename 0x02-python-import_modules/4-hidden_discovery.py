#!/usr/bin/python3

from hidden_4 import *

if __name__ == "__main__":
    names = dir()
    for name in names:
        if not name.startswith("_"):
            print(name)
