# 24. Write a function that takes a list of functions and a value, and applies each function to the value, returning the results as a list.
def apply_functions(functions, value):
    return [f(value) for f in functions]

print(apply_functions([lambda x: x+1, lambda x: x*2], 3))  # Output: [4, 6]