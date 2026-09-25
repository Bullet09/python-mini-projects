students = {

}


def add_student():
    name = input("Enter student name: ")
    grade = int(input("Enter grade: "))

    students[name] = grade

    print(students)


def view_students():
    print(" ")
    print("======== STUDENTS ========")
    print(" ")
    for i in students:
        print(i, "-", students[i])


def calculate_average():
    average = sum(students.values()) / len(students)
    print(" ")
    print("Average grade:", average)


def find_highest_grade():

    highest_grade = max(students.values())

    for i in students:
        if students[i] == highest_grade:
            print(" ")
            print("==== HIGHEST GRADE ====")
            print(i, "-", students[i])
            print(" ")


print(" ")
print('===== STUDENT GRADE MANAGER =====')
print('1. Add Student')
print('2. View Students')
print('3. Calculate Average')
print('4. Find Highest Grade')
print('5. Exit')
print(" ")

while True:
    input_num = int(input("Choose a number: "))
    if input_num == 5:
        print("Goodbye!")
        break
    elif input_num == 1:
        add_student()
    elif input_num == 2:
        view_students()
    elif input_num == 3:
        calculate_average()
    elif input_num == 4:
        find_highest_grade()
    else:
        print("Invalid")
