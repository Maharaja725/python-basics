# 47. Program to find all substrings of a string

string = input("Enter a string: ")
substrings = [string[i:j] for i in range(len(string)) for j in range(i+1, len(string)+1)]

print("All substrings:", substrings)