# 14. Write a function that accepts a variable number of lists and returns their intersection.
def intersection(*lists):
    return list(set.intersection(*map(set, lists)))

print(intersection([1,2,3], [2,3,4], [3,4,5]))  # Output: [3]