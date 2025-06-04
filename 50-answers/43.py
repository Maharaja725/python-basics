# 43. Program to count the number of unique words in a sentence

sentence = input("Enter a sentence: ")
words = sentence.lower().split()

unique_words_count = len(set(words))

print("Number of unique words:", unique_words_count)

