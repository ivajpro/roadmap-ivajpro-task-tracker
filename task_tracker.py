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
    del tasks[index]
    saveTasks(tasks)

def startTask(index):
    """Start a task (set it to in progress)"""
    tasks = loadTasks()
    tasks[index]["in progress"] = True
    tasks[index]["done"] = False
    saveTasks(tasks)

def completeTask(index):
    """Complete a task (set it to done)"""
    tasks = loadTasks()
    tasks[index]["done"] = True
    tasks[index]["in progress"] = False
    saveTasks(tasks)

def toggleTasks(index):
    """Toggle task status"""
    tasks = loadTasks()
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

def main():
    """Main function"""
    if len(sys.argv) == 1:
        listTasks()
    elif sys.argv[1] == "add":
        addTasks(sys.argv[2])
    elif sys.argv[1] == "remove":
        removeTasks(int(sys.argv[2])-1)
    elif sys.argv[1] == "start":
        startTask(int(sys.argv[2])-1)
    elif sys.argv[1] == "complete":
        completeTask(int(sys.argv[2])-1)
    elif sys.argv[1] == "toggle":
        toggleTasks(int(sys.argv[2])-1)
    elif sys.argv[1] == "status":
        statusTasks(int(sys.argv[2])-1)
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()