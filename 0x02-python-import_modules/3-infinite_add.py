#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv
    num_args = len(args) - 1
    sum = 0

    if num_args == 0:
        print(sum)
    else:
        for i in range(1, len(args)):
            sum += int(args[i])
        print(sum)
