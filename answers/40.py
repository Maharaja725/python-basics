# 40. Program to filter out strings that contain digits using regex

import re

strings = ["hello", "world123", "python", "data42"]
filtered_strings = [s for s in strings if not re.search(r'\d', s)]

print("Filtered strings:", filtered_strings)