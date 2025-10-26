
"""
To-Do List App
--------------------
A simple command-line Python app that lets you:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete tasks
5. Exit the app

All tasks are stored in a local text file (tasks.txt) so that data persists between sessions.
This is a beginner-friendly example of file handling, loops, and user interaction.
"""

# ---------- Import Section ----------
import os  # Used to check if the file exists before reading/writing


# ---------- Function Definitions ----------

def load_tasks():
    """Reads all tasks from the file and returns them as a list of dictionaries."""
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                # Each line has the format: task_name|completed_status
                name, status = line.strip().split("|")
                tasks.append({"name": name, "completed": status == "True"})
    return tasks


def save_tasks(tasks):
    """Saves all tasks to the file so data is persistent."""
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['name']}|{task['completed']}\n")


def show_tasks(tasks):
    """Displays all tasks with their status."""
    if not tasks:
        print("\n✅ No tasks found. Start by adding one!\n")
        return
    print("\nYour To-Do List:")
    print("-" * 30)
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. {task['name']} [{status}]")
    print("-" * 30)


def add_task(tasks):
    """Takes input from the user and adds a new task to the list."""
    name = input("Enter new task: ").strip()
    if name:
        tasks.append({"name": name, "completed": False})
        save_tasks(tasks)
        print(f"✅ Task '{name}' added successfully!")
    else:
        print("⚠️ Task name cannot be empty!")


def mark_task_completed(tasks):
    """Marks a selected task as completed."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to mark completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print(f"🎉 Task '{tasks[task_num - 1]['name']}' marked as completed!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def delete_task(tasks):
    """Deletes a selected task from the list."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{deleted['name']}' deleted successfully!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")


def main():
    """Main program loop that runs until the user exits."""
    tasks = load_tasks()

    while True:
        print("""
========= TO-DO LIST MENU =========
1. View all tasks
2. Add a new task
3. Mark a task as completed
4. Delete a task
5. Exit
===================================
""")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 5.")


# ---------- Run the App ----------
if __name__ == "__main__":
    main()
