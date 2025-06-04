# 50. Program to check if all numbers in a list are positive using a for-else loop

numbers = [10, 5, 20, 30, 1]

for num in numbers:
    if num < 0:
        print("List contains negative numbers.")
        break
else:
    print("All numbers are positive.")

