# 7. Use filter to select words from a list that are palindromes.
#    Input: ["level", "world", "radar", "python"]
#    Output: ["level", "radar"]

def find_palindromes(words):
    return list(filter(lambda w: w == w[::-1], words))

print(find_palindromes(["level", "world", "radar", "python"]))