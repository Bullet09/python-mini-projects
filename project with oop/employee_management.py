class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(
            f"\nName: {self.name} \nPosition: {self.position} \nSalary: {self.salary}")

    def salary_raise(self):
        pass

    def salary_update(self):
        pass

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("\n1. Display Employee Information")
    print("2. Salary Raise")
    print("3. Salary Update")

    try:
        choice = int(input("\nChoose an option: "))
    except ValueError:
        print("Invalid input. Enter a number only")

    if choice == 1:
        display_info()
    elif choice == 2:
        salary_raise()
    elif choice == 3():
        salary_update()
    else:
        print("Invalid input. Choose only from 1-3!")
        pass
