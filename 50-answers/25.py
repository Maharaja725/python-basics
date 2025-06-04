# 25. Program to find maximum and minimum values in a list without using built-in functions

numbers = [10, 20, 5, 30, 2, 40]

max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("Maximum:", max_value)
print("Minimum:", min_value)


