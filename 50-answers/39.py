# 39. Program to validate if a string is a valid Python identifier

import keyword

identifier = input("Enter a string: ")

if identifier.isidentifier() and identifier not in keyword.kwlist:
    print("Valid Python identifier")
else:
    print("Invalid Python identifier")


    