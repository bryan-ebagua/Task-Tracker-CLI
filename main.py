import sys
from tasks import add_task

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
        # 2. Call add_task(description) and store the returned ID
        task_id = add_task(description)
        # 3. Print "Task added successfully (ID: X)"
        print(f"Task added successfully (ID: {task_id})")

    else:
        print(f"Unknown command: {command}")

# This is the standard way to run a main function in Python
if __name__ == "__main__":
    main()