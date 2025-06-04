# 6. Given a float, print its integer and fractional parts separately.

num = float(input("Enter a floating-point number: "))

integer_part = int(num)
fractional_part = num - integer_part

print("Integer part:", integer_part)
print("Fractional part:", fractional_part)


