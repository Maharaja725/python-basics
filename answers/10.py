# 10. Given two numbers, print which one is greater using comparison operators.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(num1, "is greater.")
elif num2 > num1:
    print(num2, "is greater.")
else:
    print("Both numbers are equal.")
