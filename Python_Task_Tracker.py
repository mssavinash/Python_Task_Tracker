import argparse
import json
import os
import datetime

TASKS_FILE = "tasks.json"

# Load tasks from JSON file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

# Save tasks to JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.datetime.now().isoformat(),
        "updatedAt": datetime.datetime.now().isoformat(),
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

# Update a task
def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated successfully.")
            return
    print("Task not found.")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully.")

# Change task status
def change_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {status}.")
            return
    print("Task not found.")

# List tasks with optional filtering
def list_tasks(filter_status=None):
    tasks = load_tasks()
    filtered_tasks = tasks if not filter_status else [task for task in tasks if task["status"] == filter_status]
    for task in filtered_tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']} (Created: {task['createdAt']})")

# CLI Argument Parsing
def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Task description")

    # Update task
    parser_update = subparsers.add_parser("update", help="Update a task")
    parser_update.add_argument("task_id", type=int, help="Task ID")
    parser_update.add_argument("description", type=str, help="New task description")

    # Delete task
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("task_id", type=int, help="Task ID")

    # Mark task
    parser_mark = subparsers.add_parser("mark", help="Mark a task as in-progress or done")
    parser_mark.add_argument("task_id", type=int, help="Task ID")
    parser_mark.add_argument("status", choices=["in-progress", "done"], help="Task status")

    # List tasks
    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument("status", nargs="?", choices=["todo", "in-progress", "done"], help="Filter by status")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.task_id, args.description)
    elif args.command == "delete":
        delete_task(args.task_id)
    elif args.command == "mark":
        change_status(args.task_id, args.status)
    elif args.command == "list":
        list_tasks(args.status)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
