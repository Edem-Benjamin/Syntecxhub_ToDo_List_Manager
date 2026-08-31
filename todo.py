import json
import os

FILENAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(tasks, text):
    tasks.append({"text": text, "done": False})


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else " "
        print(f"{i}. [{status}] {task['text']}")


def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        return removed
    return None


def mark_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        return True
    return False


def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            text = input("Enter task: ")
            add_task(tasks, text)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            if tasks:
                try:
                    index = int(input("Enter task number to mark done: ")) - 1
                    if mark_done(tasks, index):
                        save_tasks(tasks)
                        print("Task marked as done!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            view_tasks(tasks)
            if tasks:
                try:
                    index = int(input("Enter task number to delete: ")) - 1
                    removed = delete_task(tasks, index)
                    if removed:
                        save_tasks(tasks)
                        print(f"Deleted: {removed['text']}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")


main()