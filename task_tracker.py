import os
import sys
import json

# Constants
tasksFile = "tasks.json"

def loadTasks():
    """Load tasks from file"""
    if not os.path.exists(tasksFile):
        return []
    with open(tasksFile, "r") as file:
        return json.load(file)

def saveTasks(tasks):
    """Save tasks to file"""
    with open(tasksFile, "w") as file:
        json.dump(tasks, file)

def listTasks():
    """List all tasks"""
    tasks = loadTasks()
    for i, task in enumerate(tasks):
        status = "done" if task["done"] else "in progress" if task["in progress"] else "not started"
        print(f"{i+1}. {task['title']} [{status}]")

def addTasks(title):
    """Add a new task"""
    tasks = loadTasks()
    tasks.append({"title": title, "done": False, "in progress": False})
    saveTasks(tasks)

def removeTasks(index):
    """Remove a task"""
    tasks = loadTasks()
    if not tasks or index >= len(tasks):
        raise IndexError(f"Task index {index + 1} is out of range")
    del tasks[index]
    saveTasks(tasks)

def startTask(index):
    """Start a task (set it to in progress)"""
    tasks = loadTasks()
    if not tasks or index >= len(tasks):
        raise IndexError(f"Task index {index + 1} is out of range")
    tasks[index]["in progress"] = True
    tasks[index]["done"] = False
    saveTasks(tasks)

def completeTask(index):
    """Complete a task (set it to done)"""
    tasks = loadTasks()
    if not tasks or index >= len(tasks):
        raise IndexError(f"Task index {index + 1} is out of range")
    tasks[index]["done"] = True
    tasks[index]["in progress"] = False
    saveTasks(tasks)

def toggleTasks(index):
    """Toggle task status"""
    tasks = loadTasks()
    if not tasks or index >= len(tasks):
        raise IndexError(f"Task index {index + 1} is out of range")
    if tasks[index]["done"]:
        tasks[index]["done"] = False
        tasks[index]["in progress"] = False
    elif tasks[index]["in progress"]:
        tasks[index]["done"] = True
        tasks[index]["in progress"] = False
    else:
        tasks[index]["in progress"] = True
    saveTasks(tasks)

def statusTasks(index):
    """Display task status"""
    tasks = loadTasks()
    task = tasks[index]
    if task["done"]:
        print(f"Task {index + 1} ({task['title']}) is done")
    elif task["in progress"]:
        print(f"Task {index + 1} ({task['title']}) is in progress")
    else:
        print(f"Task {index + 1} ({task['title']}) is not started")

def updateTask(index, title):
    """Update a task's title"""
    tasks = loadTasks()
    if not tasks or index >= len(tasks):
        raise IndexError(f"Task index {index + 1} is out of range")
    tasks[index]["title"] = title
    saveTasks(tasks)

def listDoneTasks():
    """List all done tasks"""
    tasks = loadTasks()
    done_tasks = [task for task in enumerate(tasks) if task[1]["done"]]
    for i, task in done_tasks:
        print(f"{i+1}. {task['title']} [done]")

def listInProgressTasks():
    """List all in-progress tasks"""
    tasks = loadTasks()
    in_progress_tasks = [task for task in enumerate(tasks) if task[1]["in progress"]]
    for i, task in in_progress_tasks:
        print(f"{i+1}. {task['title']} [in progress]")

def listNotDoneTasks():
    """List all not done tasks"""
    tasks = loadTasks()
    not_done_tasks = [task for task in enumerate(tasks) if not task[1]["done"]]
    for i, task in not_done_tasks:
        print(f"{i+1}. {task['title']} [status]")

def main():
    """Main function"""
    if len(sys.argv) == 1:
        listTasks()
    elif sys.argv[1] == "add":
        if len(sys.argv) > 2:
            addTasks(sys.argv[2])
        else:
            print("Error: Task title is required.")
    elif sys.argv[1] == "update":
        if len(sys.argv) > 3:
            updateTask(int(sys.argv[2])-1, sys.argv[3])
        else:
            print("Error: Task number and new title are required.")
    elif sys.argv[1] == "remove":
        if len(sys.argv) > 2:
            removeTasks(int(sys.argv[2])-1)
        else:
            print("Error: Task number is required.")
    elif sys.argv[1] == "start":
        if len(sys.argv) > 2:
            startTask(int(sys.argv[2])-1)
        else:
            print("Error: Task number is required.")
    elif sys.argv[1] == "complete":
        if len(sys.argv) > 2:
            completeTask(int(sys.argv[2])-1)
        else:
            print("Error: Task number is required.")
    elif sys.argv[1] == "toggle":
        if len(sys.argv) > 2:
            toggleTasks(int(sys.argv[2])-1)
        else:
            print("Error: Task number is required.")
    elif sys.argv[1] == "status":
        if len(sys.argv) > 2:
            statusTasks(int(sys.argv[2])-1)
        else:
            print("Error: Task number is required.")
    elif sys.argv[1] == "list":
        if len(sys.argv) > 2:
            if sys.argv[2] == "done":
                listDoneTasks()
            elif sys.argv[2] == "progress":
                listInProgressTasks()
            elif sys.argv[2] == "pending":
                listNotDoneTasks()
            else:
                print("Error: Invalid list type. Use 'done', 'progress', or 'pending'")
        else:
            listTasks()
    else:
        print("Invalid command")
        print("Available commands: add, update, remove, start, complete, toggle, status, list")

if __name__ == "__main__":
    main()