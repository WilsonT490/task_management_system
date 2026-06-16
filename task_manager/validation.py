"""
validation.py - Input validation functions for the Task Management System.
"""


def validate_task_name(task_name):
    """
    Validate the task name input.
    Returns True if valid, False otherwise.
    """
    if len(task_name) == 0:
        print("Error: Task name cannot be empty.")
        return False
    if len(task_name) > 100:
        print("Error: Task name cannot exceed 100 characters.")
        return False
    return True


def validate_priority(priority):
    """
    Validate the priority level input.
    Accepted values: 'low', 'medium', 'high'
    Returns True if valid, False otherwise.
    """
    valid_priorities = ["low", "medium", "high"]
    if len(priority) == 0:
        print("Error: Priority cannot be empty.")
        return False
    if priority.lower() not in valid_priorities:
        print("Error: Priority must be 'low', 'medium', or 'high'.")
        return False
    return True


def validate_task_index(index, tasks):
    """
    Validate that the task index is within range.
    Returns True if valid, False otherwise.
    """
    if len(tasks) == 0:
        print("No working currently.")
        return False
    if index < 0 or index >= len(tasks):
        print(f"Error: Invalid task number. Please enter a number between 1 and {len(tasks)}.")
        return False
    return True
