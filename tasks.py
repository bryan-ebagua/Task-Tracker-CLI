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
    newDict = {"id": newID, "description": description, "status": "todo", "createdAt": datetime.now().isoformat(), "updatedAt": datetime.now().isoformat()}
    tasks.append(newDict)
    save_tasks(tasks)
    return newID
# Prints out existing tasks. Allows you to filter for tasks based on their status
def list_tasks(filter = None):
    tasks = load_tasks()
    if len(tasks) == 0:
        print("No tasks found.")
        return
    for task in tasks:
        if filter != None and task["status"] != filter:
            continue
        print(f"{task["description"]} status: {task["status"]}")
    