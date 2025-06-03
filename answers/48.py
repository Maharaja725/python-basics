# 48. Program to print all characters that appear more than once in a string

string = input("Enter a string: ")
char_count = {}

for char in string:
    char_count[char] = char_count.get(char, 0) + 1

duplicates = [char for char, count in char_count.items() if count > 1]

print("Repeated characters:", duplicates)