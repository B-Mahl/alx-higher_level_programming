#!/usr/bin/python3

for i in range(122, 96, -2):
    j = i - 1
    print('{}{}'.format(chr(i), chr(j).upper()), end='')
