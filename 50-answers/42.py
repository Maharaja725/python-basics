# 42. Program to remove all elements greater than a given value

numbers = [10, 20, 30, 40, 50]
limit = int(input("Enter the value limit: "))

filtered_numbers = [num for num in numbers if num <= limit]

print("Filtered list:", filtered_numbers)

