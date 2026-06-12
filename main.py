import os
import sys
import importlib.util
from pathlib import Path

root_dir = Path(__file__).resolve().parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

task_utils_path = root_dir / "task_manager" / "task_utils.py"
if task_utils_path.exists():
    spec = importlib.util.spec_from_file_location("task_utils", task_utils_path)
    task_utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(task_utils)
    add_task = task_utils.add_task
    mark_task_as_complete = task_utils.mark_task_as_complete
    view_pending_tasks = task_utils.view_pending_tasks
    calculate_progress = task_utils.calculate_progress
else:
    raise ImportError(f"Cannot find task_utils module at {task_utils_path}")

def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)
        elif choice == "2":
            view_pending_tasks()
            index = int(input("Enter task number to mark complete: ")) - 1
            mark_task_as_complete(index)
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            calculate_progress()
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()