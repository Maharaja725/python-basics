# 10. Write a function that raises a custom exception if a string contains any digits.
def check_string(s):
    if any(c.isdigit() for c in s):
        raise ValueError("String contains digits")

try:
    check_string("hello123")
except ValueError as e:
    print(e)  # Output: Raises Custom Exception