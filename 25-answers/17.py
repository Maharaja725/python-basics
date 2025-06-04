# 17. Use a lambda function to filter a list of tuples, keeping only those where the sum of elements is even.
filter_even_sum = lambda lst: list(filter(lambda t: sum(t) % 2 == 0, lst))

print(filter_even_sum([(1,2), (2,2), (3,3)]))  # Output: [(2,2), (3,3)]