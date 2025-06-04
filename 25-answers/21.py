# 21. Use collections.OrderedDict to remove duplicates from a list while preserving order.
from collections import OrderedDict

remove_duplicates = lambda lst: list(OrderedDict.fromkeys(lst))

print(remove_duplicates([1,2,2,3,1,4]))  # Output: [1,2,3,4]