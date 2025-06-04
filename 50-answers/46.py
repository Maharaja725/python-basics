# 46. Program to find names with the highest score from a list of tuples

scores = [("Alice", 90), ("Bob", 85), ("Charlie", 90)]
max_score = max(score for _, score in scores)

highest_scorers = [name for name, score in scores if score == max_score]

print("Highest scorers:", highest_scorers)


