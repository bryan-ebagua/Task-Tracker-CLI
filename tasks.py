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
        print(f"{task["id"]} {task["description"]} status: {task["status"]}")

# Changes the description of an existing task
def update_task(index, newTask):
    tasks = load_tasks()
    for task in tasks:
        if(task["id"] == int(index)):
            task["description"] = newTask
            task["updatedAt"] = datetime.now().isoformat()
            print(f"Task {index} updated successfully")
            break
    save_tasks(tasks)

# Changes task status to in progress
def mark_in_progress(index):
    tasks = load_tasks()
    for task in tasks:
        if(task["id"] == int(index)):
            task["status"] = "In progress"
            task["updatedAt"] = datetime.now().isoformat()
            print(f"Task {index} marked as in progress")
            break
    save_tasks(tasks)

#Changes task status to done
def mark_done(index):
    tasks = load_tasks()
    for task in tasks:
        if(task["id"] == int(index)):
            task["status"] = "Done"
            task["updatedAt"] = datetime.now().isoformat()
            print(f"Task {index} marked as done")
            break
    save_tasks(tasks)

#Deletes a task
def delete_task(index):
    tasks = load_tasks()    
    for task in tasks:
        if task["id"] == int(index):
            tasks.remove(task) 
            print(f"Task {index} deleted successfully.")
            break        
    save_tasks(tasks)