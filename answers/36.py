# 36. Program to count the number of words using regular expressions

import re

string = input("Enter a sentence: ")
words = re.findall(r'\b\w+\b', string)

print("Word count:", len(words))