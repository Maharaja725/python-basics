# 8. Given a list, check if a value exists in the list using membership operators.

my_list = [10, 20, 30, 40, 50]
value = int(input("Enter a value: "))

if value in my_list:
    print("The value exists in the list.")
else:
    print("The value does not exist in the list.")
