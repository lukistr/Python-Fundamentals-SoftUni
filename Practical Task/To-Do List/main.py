def add_task(todo_list):
    task_description = input("Enter the task description: ")
    new_task = [task_description, False]
    todo_list.append(new_task)
    print(f"Task {task_description} added successfully.")

def mark_task_completed(todo_list):
    view_all_tasks(todo_list)
    task_index = int(input("Enter the index of the task to mark as completed: "))
    if 0 <= task_index < len(todo_list):
        todo_list[task_index][1] = True
        print("Task marked as completed!")

def view_all_tasks(todo_list):
    if todo_list:
        print("===== Tasks =====")
        for index, task in enumerate(todo_list):
            print(f"{index}. {'[X]' if task[1] else '[ ]'}{task[0]}")

def main():
    todo_list = []
    while True:
        print("\n===== To-Do List Menu =====\n1. Add a new task\n2. Mark a task as completed\n3. View all tasks\n4. Quit")
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            add_task(todo_list)
        elif choice == 2:
            mark_task_completed(todo_list)
        elif choice == 3:
            view_all_tasks(todo_list)
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
