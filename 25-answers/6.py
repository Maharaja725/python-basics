# 6. Use map to convert a list of integers to their binary string representations.
to_binary = lambda lst: list(map(bin, lst))

print(to_binary([2, 5, 8]))  # Output: ['0b10', '0b101', '0b1000']