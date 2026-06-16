from datetime import datetime

def validate_task_title(title):
    if len(title) == 0:
        return False
    return True

def validate_task_description(description):
    if len(description) == 0:
        return False
    return True

def validate_due_date(due_date):
    if len(due_date) == 0:
        return False
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")