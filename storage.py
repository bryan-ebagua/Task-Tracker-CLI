from pathlib import Path
import json
file_name = "tasks.json"
#Checks if tasks.json exists. Returns a parsed json list if it does, or an empty list if not
def load_tasks():
    file_path = Path(file_name)
    if file_path.exists():
        with open(file_path, "r") as file:
            tasks = json.load(file)
            return tasks
    else:
        return []
# Takes a list of tasks and writes them to the json file
def save_tasks(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent=4)
    return