# 8. Use reduce to find the greatest common divisor (GCD) of a list of numbers.
from functools import reduce
from math import gcd

gcd_reduce = lambda lst: reduce(gcd, lst)

print(gcd_reduce([24, 36, 60]))  # Output: 12