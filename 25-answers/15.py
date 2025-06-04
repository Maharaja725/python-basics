# 15. Write a function that accepts keyword arguments and returns a dictionary with keys and their value lengths.
def value_lengths(**kwargs):
    return {k: len(v) for k, v in kwargs.items()}

print(value_lengths(a="hello", b="world"))  # Output: {'a': 5, 'b': 5}