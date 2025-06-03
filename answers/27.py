# 27. Program to remove all whitespace from a string

string = input("Enter a string: ")
cleaned_string = "".join(string.split())

print("String without whitespace:", cleaned_string)