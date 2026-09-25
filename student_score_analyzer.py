import numpy as np

scores = np.array([78, 92, 85, 64, 90, 73, 88, 95])

# Indexing
print("\nIndexing")
print("Scores:", scores)
print("First score:", scores[0])
print("Last score:", scores[-1])
print("Fourth score:", scores[3])

# Slicing
print("\n-- Slicing --")
print("First 3 scores:", scores[0:3])
print("3rd to 6th score:", scores[2:6])

# Boolean
bool_scores = scores.astype(bool)
print(bool_scores)

# Convert score types
scores = np.array([78, 92, 85, 64, 90])
convert_scores = scores.astype(float)
print(type(convert_scores))
print(convert_scores.dtype)
