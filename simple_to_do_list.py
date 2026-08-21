tasks = []


def add_task():
    print("")


def view_tasks():
    print("")


def remove_task():
    print("")


while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        add_task()

    elif choice == 2:
        view_tasks()

    elif choice == 3:
        remove_task()

    elif choice == 4:
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid option")
