# 📝 Task Tracker CLI

A simple command-line interface (CLI) application to track and manage your tasks. This tool allows you to add, update, delete, and mark the status of tasks — all stored in a local JSON file.

## 🚀 Features

- ✅ Add new tasks
- ✏️ Update task descriptions
- ❌ Delete tasks
- 🔁 Mark tasks as `todo`, `in-progress`, or `done`
- 📋 List all tasks or filter them by status
- 🗃️ Tasks are saved in a local `tasks.json` file (auto-created if missing)

## 📦 Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/task-tracker-cli.git
   cd task-tracker-cli

## List of Commands
Add a new task
```
python task_tracker.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
```
Update a task
```
python task_tracker.py update 1 "Buy groceries and cook dinner"
```
Delete a task
```
python task_tracker.py delete 1
```
Mark a task as in-progress or done
```
python task_tracker.py mark 1 in-progress
python task_tracker.py mark 1 done
```
List all tasks
```
python task_tracker.py list
```
List tasks by status
```
python task_tracker.py list done
python task_tracker.py list todo
python task_tracker.py list in-progress
```

## Execution
```
python Python_Task_Tracker.py add "Complete project documentation"
python Python_Task_Tracker.py list
python Python_Task_Tracker.py mark 1 done
```

Project will generate a json file after you run the command.

## Result
![image](https://github.com/user-attachments/assets/2804da6f-6054-4c00-9b2f-6b1e0ebe093d)

## Project
[https://roadmap.sh/projects/task-tracker]
