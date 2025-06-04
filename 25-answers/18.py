# 18. Use map to add corresponding elements of two lists.
add_lists = lambda lst1, lst2: list(map(lambda x, y: x + y, lst1, lst2))

print(add_lists([1,2,3], [4,5,6]))  # Output: [5,7,9]