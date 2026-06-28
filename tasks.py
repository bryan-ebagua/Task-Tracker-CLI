from storage import load_tasks
from storage import save_tasks
from datetime import datetime
# Creates a new task
def add_task(description):
    tasks = load_tasks()
    # If tasks exist, find the max id and add 1. Otherwise, start at 1.
    if tasks:
        newID = max(task["id"] for task in tasks) + 1
    else:
        newID = 1
    newDict = {"id": newID, "description": description, "status": "todo", "createdAt": datetime.now().isoformat, "updatedAt": datetime.now().isoformat}
    tasks.append(newDict)
    save_tasks(tasks)
    return newID