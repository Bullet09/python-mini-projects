import numpy as np

scores = np.array([78, 92, 85, 64, 90, 73, 88, 95])

# Indexing
print("\nIndexing")
print("Scores:", scores)
print("First score:", scores[0])
print("Last score:", scores[-1])
print("Fourth score:", scores[3])
print("Sixth score:", scores[5])

# Slicing
print("\n-- Slicing --")
print("First 3 scores:", scores[0:3])
print("3rd to 6th score:", scores[2:6])

# Boolean
bool_scores = scores.astype(bool)
print("Boolean scores:", bool_scores)

# Convert score types
float_scores = scores.astype(float)
print("\n-- Data Types --")
print("Data type:", float_scores.dtype)
print("Converted array:", float_scores)

# Copy vs View
print("\n-- Copy --")
score_copy = scores.copy()
score_copy[0] = 100
print("Original scores:", scores)
print("Copied scores:", score_copy)

# View
scores[0] = 78
score_view = scores.view()
score_view[0] = 100
print("\n -- View --")
print("Original scores:", scores)
print("View scores:", score_view)

# Shape
print("\n -- Shapes --")
print("Shape:", scores.shape)
