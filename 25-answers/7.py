# 7. Use filter to select words from a list that are palindromes.
palindromes = lambda words: list(filter(lambda w: w == w[::-1], words))

print(palindromes(["level", "world", "radar", "python"]))  # Output: ["level", "radar"]