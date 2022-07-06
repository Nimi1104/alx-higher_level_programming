#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = 0
    for elm in set(my_list):
        num += elm
    return num
