# 25. Write a function that accepts a variable number of keyword arguments and returns only those whose values are integers.
filter_integers = lambda kwargs: {k: v for k, v in kwargs.items() if isinstance(v, int)}

print(filter_integers({"a": 1, "b": "hello", "c": 3}))  # Output: {'a': 1, 'c': 3}