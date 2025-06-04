# 2. Write a function that accepts a variable number of string arguments and returns the longest string.
#    Input: "cat", "elephant", "dog"
#    Output: "elephant"

def longest_string(*strings):
    longest = ""
    for s in strings:
        if len(s) > len(longest):
            longest = s
    return longest

print(longest_string("cat", "elephant", "dog")) 