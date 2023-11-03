#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv
    num_args = len(args) - 1

    if num_args == 0:
        print('0 Arguments.')
    elif num_args == 1:
        print('1 Argument:')
        print('1: ' + args[1])
    else:
        print('{} Arguments:'.format(num_args))
        for i in range(1, len(args)):
            print('{}: {}'.format(i, args[i]))
