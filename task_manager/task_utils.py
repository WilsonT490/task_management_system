"""
task_utils.py - Utility functions for the Task Management System.
"""

from task_manager.validation import validate_task_name, validate_priority, validate_task_index


def add_task(tasks, task_name, priority="medium"):
    """
    Add a new task to the tasks list.
    Each task is stored as a dictionary.
    Returns the updated tasks list.
    """
    if not validate_task_name(task_name):
        return tasks
    if not validate_priority(priority):
        return tasks

    task = {
        "task_name": task_name,
        "priority": priority.lower(),
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully.")
    return tasks


def mark_task_complete(tasks, task_index):
    """
    Mark a task as complete by its index (0-based).
    Returns the updated tasks list.
    """
    if not validate_task_index(task_index, tasks):
        return tasks

    if tasks[task_index]["completed"]:
        print("Task is already marked as complete.")
    else:
        tasks[task_index]["completed"] = True
        print("Task marked as complete.")
    return tasks


def view_pending_tasks(tasks):
    """
    Display all pending (incomplete) tasks.
    """
    pending = [task for task in tasks if not task["completed"]]

    if len(pending) == 0:
        print("No pending tasks.")
        return

    print("\n--- Pending Tasks ---")
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i + 1}. [{task['priority'].upper()}] {task['task_name']}")
    print("---------------------")


def track_progress(tasks):
    """
    Display overall progress of tasks.
    """
    total = len(tasks)

    if total == 0:
        print("No working currently.")
        return

    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed
    percentage = (completed / total) * 100

    print("\n--- Progress Report ---")
    print(f"Total Tasks   : {total}")
    print(f"Completed     : {completed}")
    print(f"Pending       : {pending}")
    print(f"Progress      : {percentage:.1f}%")
    print("-----------------------")
