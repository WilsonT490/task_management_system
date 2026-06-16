from validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Invalid title.")
        return
    if not validate_task_description(description):
        print("Invalid description.")
        return
    if not validate_due_date(due_date):
        print("Invalid due date.")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    tasks[index]["completed"] = True
    print("Task marked as complete!")

def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks if not task["completed"]]
    if len(pending) == 0:
        print("No pending tasks.")
    else:
        for i, task in enumerate(pending):
            print(f"{i}. {task['title']} Due: {task['due_date']}")

def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0
    else:
        completed = len([task for task in tasks if task["completed"]])
        progress = (completed / len(tasks)) * 100
        return progress