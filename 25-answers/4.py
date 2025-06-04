# 4. Write a function that takes another function as a callback and applies it to the values of a dictionary, returning a new dictionary.
#    Input: {"a": 2, "b": 3}, callback: lambda x: x**2
#    Output: {"a": 4, "b": 9}

def apply_callback(data, callback):
    for key in data:
        data[key] = callback(data[key])
    return data

print(apply_callback({"a": 2, "b": 3}, lambda x: x**2))  
