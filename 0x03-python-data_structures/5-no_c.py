#!/usr/bin/python3
def no_c(my_string):
    """a function that removes all characters c and C from a string."""

    new_string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            new_string += elements

    return new_string
