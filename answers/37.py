# 37. Program to extract email addresses from a given text using regex

import re

text = input("Enter text: ")
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

print("Extracted emails:", emails)