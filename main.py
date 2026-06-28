import sys
from tasks import (
    add_task,
    list_tasks, 
    update_task,
    mark_in_progress,
    mark_done,
    delete_task
)

def main():
    # Store the arguments in a variable for easy access
    args = sys.argv
    
    # If the user just typed 'python main.py' with no commands, exit gracefully
    if len(args) < 2:
        print("Usage: task-cli <command> [arguments]")
        return

    command = args[1]

    if command == "add":
        # 1. Grab the description from the args list
        description = " ".join(args[2:])
        if not description:
            print("Error: Please provide a description for the task.")
            return
        # 2. Call add_task(description) and store the returned ID
        task_id = add_task(description)
        # 3. Print "Task added successfully (ID: X)"
        print(f"Task added successfully (ID: {task_id})")
    elif command == "list":
        if len(args) > 2:
            list_tasks(args[2])
        else:
            list_tasks()
    elif command == "update":
        if len(args) > 3:
            update_task(args[2], " ".join(args[3:]))
        else:
            print("Error: Please provide a new task")
    elif command == "mark-in-progress":
        if len(args) > 2:
            mark_in_progress(args[2])
        else:
            print("Error: Please provide an index")
    elif command == "mark-done":
        if len(args) > 2:
            mark_done(args[2])
        else:
            print("Error: Please provide an index")
    elif command == "delete":
        if len(args) > 2:
            delete_task(args[2])
        else:
            print("Error: Please provide an index")
    else:
        print(f"Unknown command: {command}")

# This is the standard way to run a main function in Python
if __name__ == "__main__":
    main()