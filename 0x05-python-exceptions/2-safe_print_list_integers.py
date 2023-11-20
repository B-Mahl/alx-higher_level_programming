#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    prnted = 0
    for int in range(x):
        try:
            print('{:d}'.format(my_list[int]), end='')
            prnted += 1
        except (ValueError, TypeError):
            continue
    print()
    return prnted
