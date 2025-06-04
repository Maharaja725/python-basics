# 13. Write a program to count the number of vowels in a string.

string = input("Enter a string: ")
vowels = "aeiouAEIOU"

count = sum(1 for char in string if char in vowels)

print("Number of vowels:", count)

