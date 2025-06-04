def longest_string(*strings):
    longest = ""
    for s in strings:
        if len(s) > len(longest):
            longest = s
    return longest

print(longest_string("cat", "elephant", "dog"))  # Output: "elephant" 