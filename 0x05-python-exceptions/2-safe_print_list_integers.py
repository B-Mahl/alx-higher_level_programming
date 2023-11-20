#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    prnted = 0
    for int in range(x):
        try:
            print('{:d}'.format(my_list[i]), end='')
            prnted += 1
        except (TypeError, ValueError):
            continue
    print()
    return prnted
