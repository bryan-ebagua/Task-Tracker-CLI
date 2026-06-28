# Task Tracker CLI

A simple command-line interface (CLI) application to track and manage your tasks. Built entirely with Python's standard library, this tool lets you add, update, delete, and track the status of your daily tasks directly from your terminal.


## Prerequisites

* Python 3.x installed on your system.

## Installation

1. Clone or download this repository.
2. Open your terminal and navigate to the project directory.

This application is entirely driven via the command line. Below are all the available commands, what they do, and examples of how to use them. All commands are executed by running the main.py file followed by your desired command and arguments.

### 1. Adding a Task
Use the `add` command followed by the task description. The default status is always `todo`.
```bash
python main.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
```
### 2. Updating a Task Description
Use the update command followed by the task's ID and the new description.
```bash
python main.py update 1 "Buy groceries and cook dinner"
# Output: Task 1 updated successfully.
```
### 3. Deleting a Task
Use the delete command followed by the ID of the task you want to remove.
```bash
python main.py delete 1
# Output: Task 1 deleted successfully.
```
### 4. Changing Task Status
You can move tasks through different stages of completion using the mark-in-progress and mark-done commands, followed by the task ID.
```bash
python main.py mark-in-progress 1
# Output: Task 1 marked as in-progress.

python main.py mark-done 1
# Output: Task 1 marked as done.
```
### 5. Listing Tasks
Use the list command to view your tasks. You can view all of them, or filter them by passing a specific status.
```bash
# View every task in your tracker
python main.py list

# View only tasks that still need to be started
python main.py list todo

# View only tasks you are currently working on
python main.py list "In progress"

# View only completed tasks
python main.py list Done
```
Inspired by https://roadmap.sh/projects/task-tracker
