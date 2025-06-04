# 34. Program to print the second largest element in a list

numbers = [10, 20, 5, 40, 30]
unique_numbers = list(set(numbers))
unique_numbers.sort()

print("Second largest element:", unique_numbers[-2])

