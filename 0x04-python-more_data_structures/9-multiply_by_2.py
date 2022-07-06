#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for keys in new_dictionary:
        new_dictionary[keys] *= 2
    return new_dictionary
    # the shorter syntax would be:
    # return (key: value * 2 for key, value in a_dictionary.items())
