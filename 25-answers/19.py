# 19. Use filter to select numbers from a list that are perfect squares.
is_perfect_square = lambda x: int(x**0.5)**2 == x
filter_squares = lambda lst: list(filter(is_perfect_square, lst))

print(filter_squares([1, 2, 4, 7, 9, 16]))  # Output: [1, 4, 9, 16]