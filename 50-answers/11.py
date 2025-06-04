# 11. Write a program to check if a string contains only digits using a loop and logical operators.

string = input("Enter a string: ")

only_digits = True
for char in string:
    if not ('0' <= char <= '9'):
        only_digits = False
        break

print("Contains only digits:", only_digits)


