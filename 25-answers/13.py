# 13. Write a function that takes a list of numbers and returns a tuple of (sum, average, maximum, minimum).
def stats(numbers):
    return (sum(numbers), sum(numbers)/len(numbers), max(numbers), min(numbers))

print(stats([1, 2, 3, 4]))  # Output: (10, 2.5, 4, 1)