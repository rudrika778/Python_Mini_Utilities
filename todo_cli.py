# tools/todo_cli.py

"""
Simple CLI To-Do List
Beginner-friendly and uses only Python standard library.
"""

TODO_FILE = "todos.txt"


def load_todos():
    try:
        with open(TODO_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []


def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        for todo in todos:
            f.write(todo + "\n")


def show_todos(todos):
    if not todos:
        print("No tasks yet ✨")
        return

    print("\nYour To-Do List:")
    for i, task in enumerate(todos, start=1):
        print(f"{i}. {task}")


def main():
    todos = load_todos()

    while True:
        print("\n--- To-Do Menu ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_todos(todos)

        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                todos.append(task)
                save_todos(todos)
                print("Task added ✅")
            else:
                print("Task cannot be empty ❌")

        elif choice == "3":
            show_todos(todos)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(todos):
                    removed = todos.pop(index)
                    save_todos(todos)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number ❌")
            except ValueError:
                print("Please enter a number ❌")

        elif choice == "4":
            print("Goodbye 👋")
            break

        else:
            print("Invalid option ❌")


if __name__ == "__main__":
    main()
