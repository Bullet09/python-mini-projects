import numpy as np

scores = np.array([85, 92, 78, 90, 88, 76, 95, 89])

print("Array:", scores)
print("\nStatistics")
print("----------")
print("Total:", np.sum(scores))
print("Mean:", np.mean(scores))
print("Minimum:", np.min(scores))
print("Maximum:", np.max(scores))
print(np.std(scores))


filter_scores = scores[scores >= 90]
print(filter_scores)
