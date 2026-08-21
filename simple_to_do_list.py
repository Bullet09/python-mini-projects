tasks = []


def add_task():
    input_task = input("Enter task: ")
    tasks.append(input_task)


def view_tasks():
    print("===== YOUR TASKS ===== ")
    for i, tasks in enumerate(tasks, start=1):
        print(i)


def remove_task():
    task_remove = int(input("Enter task number to remove: "))
    updated_tasks = tasks.pop(task_remove)
    print(updated_tasks)


while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        add = add_task()
        tasks = add
        print("Task added successfully!")

    elif choice == 2:
        view_tasks()

    elif choice == 3:
        tasks = remove_task()
        updated_tasks = tasks

    elif choice == 4:
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid option")
