import numpy as np

students = np.array([
    ["Adrian", 85, 92, 78],
    ["Maria", 91, 88, 95],
    ["John", 76, 84, 80],
    ["Alexa", 95, 93, 97],
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

# Reshaping and Sorting
reshape_array = numeric_scores.reshape(-1)
sorted_scores = np.sort(reshape_array)
print("\nSorted scores:", sorted_scores)

# Boolean filtering
high_performers = averages >= 90
high_performers_names = students[:, 0][high_performers]
print("High performers:", high_performers_names)
high_performer_count = np.sum(high_performers)
print("High performer count:", high_performer_count)

best_student_index = np.argmax(averages)
best_student_name = students[best_student_index, 0]
best_student_average = averages[best_student_index]
print("\nTOP 1:", best_student_name)
print("Average:", best_student_average)


highest_subject_scores = np.max(numeric_scores, axis=1)
highest_score_index = np.argmax(highest_subject_scores)
highest_score_student = students[highest_score_index, 0]
print("Highest subject scores:", highest_subject_scores)
print("TOP 1 Student:", highest_score_student)

below_average = averages < 85
below_average_names = students[:, 0][below_average]
below_average_count = np.sum(below_average)
overall_average = np.mean(numeric_scores)
print("\nBelow average:", below_average_names)
print("Below average students:", below_average_count)
print("\nOverall average:", overall_average)

subject_averages = np.mean(numeric_scores, axis=0)
strongest_subject_index = np.argmax(subject_averages)
subjects = np.array(["Math", "Science", "English"])
print("Subject averages:", subject_averages)
strongest_subject = subjects[strongest_subject_index]
strongest_subject_average = subject_averages[strongest_subject_index]
print("Average:", strongest_subject_average)

weakest_subject_index = np.argmin(subject_averages)
weakest_subject = subjects[weakest_subject_index]
weakest_subject_average = subject_averages[weakest_subject_index]
print("\nWeakest subject index:", weakest_subject_index)
print("Weakest subject average:", weakest_subject_average)

subject_average_difference = strongest_subject_average - weakest_subject_average
print("\nSubject difference:", subject_average_difference)

high_performer_percentage = high_performer_count / students.shape[0] * 100
print("\nPercentage of high performers:", high_performer_percentage)

passing_students = averages >= 75
print("\nPassing students:", passing_students)

passing_student_names = students[:, 0][passing_students]
print("Passing student names:", passing_student_names)

passing_student_count = np.sum(passing_students)
print("Passing count:", passing_student_count)

passing_student_percentage = passing_student_count / students.shape[0] * 100
print("Passing student percentage:", passing_student_percentage)
