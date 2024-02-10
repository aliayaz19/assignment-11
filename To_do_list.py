#To-Do List: Develop a program that allows the user to add tasks to a to-do list. Use if statements 
#to categorize tasks as urgent, important, or less important based on their due date and priority.
todo_list = []

while True:
    task = input("Enter the task: ")
    due_date = input("Enter the due date (e.g., YYYY-MM-DD): ")
    priority = input("Enter the priority (urgent, important, less important): ")

    todo_list.append((task, due_date, priority))

    another_task = input("Do you want to add another task? (yes/no): ")
    if another_task != 'yes':
        break

print("To-Do List:")
for task, due_date, in todo_list:
    if priority == 'urgent':
        print(f"Urgent: {task} - Due: {due_date}")
    elif priority == 'important':
        print(f"Important: {task} - Due: {due_date}")
    elif priority == 'less important':
        print(f"Less Important: {task} - Due: {due_date}")
    else:
        print(f"Unknown priority: {priority}")
