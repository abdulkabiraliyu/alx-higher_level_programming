#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list, in reverse order."""
    if my_list:
        new_list = reversed(my_list)

        for i in new_list:
            print("{:d}".format(i))
