#!/usr/bin/python3

from hidden_4 import *

names = dir(hidden_4)
for name in names:
    if not name.startswith("_"):
        print(name)
