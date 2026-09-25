tasks = []


def add_task():
    input_task = input("Enter task: ")
    tasks.append(input_task)
    return


def view_tasks():
    print("===== YOUR TASKS ===== ")
    for i, task in enumerate(tasks, start=1):
        print(i, task)


def remove_task():
    task_remove = int(input("Enter task number to remove: "))

    for i, task in enumerate(tasks, start=1):
        if i == task_remove:
            tasks.pop(i-1)
            print("Task removed successfully!")


while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        add_task()
        print("Task added successfully!")

    elif choice == 2:
        view_tasks()

    elif choice == 3:
        remove_task()

    elif choice == 4:
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid option")
