#!/usr/bin/python3

def max_integer(my_list=[]):
    """a function that finds the biggest integer of a list"""

    if my_list:
        my_list.sort(reverse=True)
        return (my_list[0])
    return (None)
