#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copy = [0] * len(my_list)
    for i in range(0, len(my_list)):
        if i == idx:
            copy[i] = element
        else:
            copy[i] = my_list[i]
    return copy
