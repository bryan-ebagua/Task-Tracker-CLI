from pathlib import Path
import json
#Checks if tasks.json exists. Returns a parsed json list if it does, or an empty list if not
def load_tasks():
    file_path = Path("tasks.json")
    if file_path.exists():
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            return tasks
    else:
        return[]
# Takes a list of tasks and writes them to the json file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    return