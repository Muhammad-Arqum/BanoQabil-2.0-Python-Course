# NAME: MUHAMMAD ARQUM, ROLL NO: 21725, EMAIL: marqum2003@gmail.com 
tasks = []

def add_task():
    task_name = input("Enter task name: ")
    priority = input("Enter priority (low, medium, high): ")
    task = {"name": task_name, "priority": priority, "done": False}
    tasks.append(task)
    print("Task added successfully!\n")

def view_tasks():
    print("\nTask List:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. {task['name']} - Priority: {task['priority']} - Status: {status}")
    print()

def mark_done():
    view_tasks()
    task_number = int(input("Enter task number to mark as done: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        print("Task marked as done!\n")
    else:
        print("Invalid task number. Please try again.\n")

def remove_completed():
    global tasks
    tasks = [task for task in tasks if not task["done"]]
    print("Completed tasks removed!\n")

# Sample usage
while True:
    print("1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Remove Completed Tasks\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        remove_completed()
    elif choice == "5":
        print("Exiting Task Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
