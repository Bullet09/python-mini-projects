import numpy as np


# =========================
# Student Dataset
# =========================

students = np.array([
    ["Adrian", 85, 92, 78],
    ["Maria", 91, 88, 95],
    ["John", 76, 84, 80],
    ["Alexa", 95, 93, 97],
    ["Mark", 68, 75, 72]
])


# =========================
# Dashboard
# =========================

print("\n-- Student Performance Analyzer --")

print("Students:\n", students)
print("\nData Type:", students.dtype)
print("\nStudent Scores:", students[:, 1:4])


# =========================
# Convert Scores to Integers
# =========================

numeric_scores = students[:, 1:4].astype(int)

print("\nNumeric Scores:", numeric_scores)


# =========================
# Student Statistics
# =========================

averages = np.mean(numeric_scores, axis=1)

highest_score = np.max(numeric_scores)
lowest_score = np.min(numeric_scores)

print("\nStudent Averages:", averages)
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)


# =========================
# Sorting Scores
# =========================

reshape_array = numeric_scores.reshape(-1)
sorted_scores = np.sort(reshape_array)

print("\nSorted Scores:", sorted_scores)


# =========================
# High Performers
# =========================

high_performers = averages >= 90
high_performers_names = students[:, 0][high_performers]
high_performer_count = np.sum(high_performers)

print("\nHigh Performers:", high_performers_names)
print("High Performer Count:", high_performer_count)


# =========================
# Highest Individual Subject Score
# =========================

highest_subject_scores = np.max(numeric_scores, axis=1)
highest_score_index = np.argmax(highest_subject_scores)
highest_score_student = students[highest_score_index, 0]

print("\nHighest Subject Score Per Student:", highest_subject_scores)
print("Highest Individual Subject Scorer:", highest_score_student)


# =========================
# Below-Average Students
# =========================

below_average = averages < 85
below_average_names = students[:, 0][below_average]
below_average_count = np.sum(below_average)

overall_average = np.mean(numeric_scores)

print("\nBelow-Average Students:", below_average_names)
print("Below-Average Student Count:", below_average_count)
print("Overall Average:", overall_average)


# =========================
# Subject Analysis
# =========================

subjects = np.array(["Math", "Science", "English"])

subject_averages = np.mean(numeric_scores, axis=0)

strongest_subject_index = np.argmax(subject_averages)
strongest_subject = subjects[strongest_subject_index]
strongest_subject_average = subject_averages[strongest_subject_index]

weakest_subject_index = np.argmin(subject_averages)
weakest_subject = subjects[weakest_subject_index]
weakest_subject_average = subject_averages[weakest_subject_index]

subject_average_difference = (
    strongest_subject_average - weakest_subject_average
)

print("\nSubject Averages:", subject_averages)
print("Strongest Subject:", strongest_subject)
print("Strongest Subject Average:", strongest_subject_average)
print("Weakest Subject:", weakest_subject)
print("Weakest Subject Average:", weakest_subject_average)
print("Subject Average Difference:", subject_average_difference)


# =========================
# High Performer Percentage
# =========================

high_performer_percentage = (
    high_performer_count / students.shape[0] * 100
)

print("\nHigh Performer Percentage:", high_performer_percentage)


# =========================
# Passing Students
# =========================

passing_students = averages >= 75
passing_student_names = students[:, 0][passing_students]
passing_student_count = np.sum(passing_students)
passing_student_percentage = (
    passing_student_count / students.shape[0] * 100
)
passing_student_average = np.mean(averages[passing_students])

print("\nPassing Students:", passing_students)
print("Passing Student Names:", passing_student_names)
print("Passing Student Count:", passing_student_count)
print("Passing Student Percentage:", passing_student_percentage)
print("Passing Student Average:", passing_student_average)


# =========================
# Failing Students
# =========================

failing_students = averages < 75
failing_student_average = np.mean(averages[failing_students])

print("\nFailing Student Average:", failing_student_average)


# =========================
# Highest & Lowest Student Average
# =========================

highest_student_average = np.max(averages)
lowest_student_average = np.min(averages)

highest_student_index = np.argmax(averages)
lowest_student_index = np.argmin(averages)

highest_student_name = students[highest_student_index, 0]
lowest_student_name = students[lowest_student_index, 0]

print("\nHighest Student:", highest_student_name)
print("Highest Student Average:", highest_student_average)

print("\nLowest Student:", lowest_student_name)
print("Lowest Student Average:", lowest_student_average)


# =========================
# Final Summary
# =========================

print("\n========== FINAL SUMMARY ==========")

print("Overall Student Average:", overall_average)

print("Highest Student:", highest_student_name)
print("Highest Student Average:", highest_student_average)

print("Lowest Student:", lowest_student_name)
print("Lowest Student Average:", lowest_student_average)

print("Strongest Subject:", strongest_subject)
print("Strongest Subject Average:", strongest_subject_average)

print("Weakest Subject:", weakest_subject)
print("Weakest Subject Average:", weakest_subject_average)

print("Passing Students:", passing_student_count)
print("Passing Students Percentage:", passing_student_percentage)

print("High-Performing Students:", high_performer_count)
print("High-Performer Percentage:", high_performer_percentage)
