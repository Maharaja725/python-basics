# 20. Use reduce to concatenate a list of strings with a hyphen between them.
from functools import reduce

concat_strings = lambda lst: reduce(lambda x, y: x + "-" + y, lst)

print(concat_strings(["a", "b", "c"]))  # Output: "a-b-c"