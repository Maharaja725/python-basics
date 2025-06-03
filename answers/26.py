# 26. Program to print only strings that start with a vowel

words = ["apple", "banana", "orange", "grape", "umbrella"]
vowels = "aeiouAEIOU"

filtered_words = [word for word in words if word[0] in vowels]

print("Words starting with a vowel:", filtered_words)