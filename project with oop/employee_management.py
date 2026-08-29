class Employee:
    # Employee Method
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(
            f"\nName: {self.name} \nPosition: {self.position} \nSalary: {self.salary}")

    # Salary Raise Method
    def salary_raise(self):
        try:
            raise_input = int(input("Enter raise amount: "))
        except ValueError:
            print("Invalid input. Raise should only be numbers")
            return
        if raise_input <= 0:
            print("Invalid input. Negative amount is not allowed.")
            return
        added_salary = raise_input + self.salary
        self.salary = added_salary
        print("Current salary: ", added_salary)

    # Salary Update Method
    def salary_update(self):
        current_salary = self.salary
        print("Current salary: ", current_salary)
        try:
            updated_salary = int(input("Enter new salary: "))
            self.salary = updated_salary
        except ValueError:
            print("Invalid input. Salary amount should only be numbers")


employee1 = Employee("Adrian", "Software Developer", 125000)

# MENU
print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
print("\n1. Display Employee Information")
print("2. Salary Raise")
print("3. Salary Update")

try:
    choice = int(input("\nChoose an option: "))
except ValueError:
    print("Invalid input. Choose a number only")

if choice == 1:
    employee1.display_info()
elif choice == 2:
    employee1.salary_raise()
elif choice == 3:
    employee1.salary_update()
else:
    print("Invalid input. Choose only from 1-3!")
    pass
