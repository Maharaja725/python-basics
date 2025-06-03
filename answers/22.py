# 22. Program to add a new key-value pair only if the key does not exist

my_dict = {"a": 10, "b": 20, "c": 30}
key = "d"
value = 40

if key not in my_dict:
    my_dict[key] = value

print(my_dict)