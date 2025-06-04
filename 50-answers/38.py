# 38. Program to check if a string matches a valid phone number pattern using regex

import re

phone = input("Enter a phone number: ")
pattern = r'^\d{10}$'

if re.match(pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")

    