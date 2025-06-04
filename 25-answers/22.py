# 22. Write a function that raises a custom exception if a list contains duplicate elements.
def check_duplicates(lst):
    if len(lst) != len(set(lst)):
        raise ValueError("List contains duplicates")

try:
    check_duplicates([1,2,3,2])
except ValueError as e:
    print(e)  # Output: Raises Custom Exception