#!/usr/bin/python3
"""First name and last name must be strings"""

def say_myname(first_name, last_name=""):
    if type(first_name) is not str:
        raise TypeError("First name must be a string")
    elif type(last_name) is not str:
        raise TypeError("Last name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))

say_myname("Aisha", "K")
say_myname("Khalfan", 123)
