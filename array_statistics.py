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


high_scores = scores[scores >= 90]
print(high_scores)
print("\nNumber of high scores:", high_scores.size)
print(np.median(scores))


below_mean = scores[scores < np.mean(scores)]
print("\nBelow Mean:", below_mean)
print("Average below mean:", np.mean(below_mean))
print("Number of low grades:", np.size(below_mean))

percentage = high_scores.size/np.size(scores) * 100
print("\nPercentage of high scores:", percentage)

max_score = np.max(high_scores)
print("\nMax score:", max_score)

lowest_high_score = np.min(high_scores)
print("\nLowest High Score:", lowest_high_score)

sorted_scores = []

sorted_scores = np.sort(scores)
print(sorted_scores)

mid_score = sorted_scores[3:5]
print(mid_score)
