import datetime

to_do_list = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

def view_tasks():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}. [{task['priority']}] {task['task']} (Category: {task['category']}, Due: {task['due_date']})")

def add_task():
    task_name = input("Enter the task: ")
    category = input("Enter the category (e.g., Work, Personal, etc.): ")
    priority = input("Enter the priority (High, Medium, Low): ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    
    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
        task = {
            "task": task_name,
            "category": category,
            "priority": priority.capitalize(),
            "due_date": due_date
        }
        to_do_list.append(task)
        print(f'"{task_name}" has been added to your to-do list.')
    except ValueError:
        print("Invalid date format. Please enter the date as YYYY-MM-DD.")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(to_do_list):
            removed_task = to_do_list.pop(task_num - 1)
            print(f'"{removed_task["task"]}" has been removed from your to-do list.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
