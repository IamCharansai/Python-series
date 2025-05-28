tasks = []

def show_menu():
    print("\n To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(" Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet. Add something!")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
 
def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f" Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print(" Goodbye!!")
        break
    else:
        print("Invalid option. Try again.")
