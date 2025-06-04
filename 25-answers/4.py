# 4. Write a function that takes another function as a callback and applies it to the values of a dictionary, returning a new dictionary.
def apply_callback(data, callback):
    return {k: callback(v) for k, v in data.items()}

print(apply_callback({"a": 2, "b": 3}, lambda x: x**2))  # Output: {"a": 4, "b": 9}