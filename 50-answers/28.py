# 28. Program to replace all vowels in a string with '*'

string = input("Enter a string: ")
vowels = "aeiouAEIOU"

modified_string = "".join('*' if char in vowels else char for char in string)

print("Modified string:", modified_string)

