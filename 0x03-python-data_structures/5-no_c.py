#!/usr/bin/python3

def no_c(my_string):
    new_str = ''
    for letter in my_string:
        if letter == 'C' or letter == 'c':
            continue
        new_str = new_str + letter
