import random

tasks = []

def show_menu():
    print("\n📝 To-Do List")
    print("------------")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Clear all tasks")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks yet. 🎉")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("✅ Task added.")
    else:
        print("Task cannot be empty.")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks()
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"🗑 Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def clear_tasks():
    confirm = input("Are you sure you want to delete all tasks? (y/n): ")
    if confirm.lower() == "y":
        tasks.clear()
        print("All tasks cleared.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1–5): ").strip()
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            clear_tasks()
        elif choice == "5":
            print("Goodbye! ✅")
            break
        else:
            print("Please choose a valid option (1–5).")

if __name__ == "__main__":
    main()
