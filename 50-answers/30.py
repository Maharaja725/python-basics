# 30. Program to print the squares of all odd numbers from a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [num ** 2 for num in numbers if num % 2 != 0]

print("Squares of odd numbers:", squares)

