# 14. Given a string, print its reverse using a loop.

string = input("Enter a string: ")
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

print("Reversed string:", reversed_string)


