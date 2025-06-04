# 5. Use a lambda function to sort a list of dictionaries by a specific key's value.
sort_by_key = lambda lst, key: sorted(lst, key=lambda x: x[key])

print(sort_by_key([{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}], "age"))
# Output: [{"name": "Bob", "age": 20}, {"name": "Alice", "age": 25}]