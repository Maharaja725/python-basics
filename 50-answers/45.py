# 45. Program to group words by their first letter using a dictionary

words = ["apple", "banana", "cherry", "apricot", "blueberry"]
groups = {}

for word in words:
    first_letter = word[0]
    groups.setdefault(first_letter, []).append(word)

print("Grouped words:", groups)

