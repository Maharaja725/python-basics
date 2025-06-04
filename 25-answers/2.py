# 2. Write a function that accepts a variable number of string arguments and returns the longest string.
def longest_string(*strings):
    return max(strings, key=len)

print(longest_string("cat", "elephant", "dog"))  # Output: "elephant"