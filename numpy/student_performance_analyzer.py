import numpy as np

students = np.array([
    ["Adrian", 85, 92, 78],
    ["Maria", 91, 88, 95],
    ["John", 76, 84, 80],
    ["Sarah", 95, 93, 97],
    ["Mark", 68, 75, 72]
])

# Dashboard
print("\n-- Student Performance Analyzer --")
print("Students:\n", students)
print("\nData Type:", students.dtype)
print("\nStudent Scores:", students[:, 1:4])

# Converting Integers inside Array
numeric_scores = students[:, 1:4].astype(int)
print("Numeric scores:", numeric_scores)

# Calculating Average
averages = np.mean(numeric_scores, axis=1)
print("\nStudent Averages:", averages)

# Highest score
highest_score = np.max(numeric_scores)
print("\nHighest score:", highest_score)

# Lowest Score
lowest_score = np.min(numeric_scores)
print("Lowest score:", lowest_score)

# Filtering and Sorting
reshape_array = numeric_scores.reshape(-1)
sorted_scores = np.sort(reshape_array)
print("\nSorted scores:", sorted_scores)
