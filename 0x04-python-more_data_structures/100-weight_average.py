#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return 0
    product = 0
    sum_ = 0
    for tupl in my_list:
        t_list = list(tupl)
        product += t_list[0] * t_list[1]
        sum_ += t_list[1]
    return product / sum_
