import json
import os
import sys
working_file = "task.json"
from datetime import datetime


def init_storage():
    if not os.path.exists(working_file):
        with open(working_file, "w") as file:
            json.dump([], file)
            #writes an empty list to the file 

# load the tasks that are already in the json file 
def load_tasks():
    with open(working_file, "r") as file:
        return json.load(file)

# save the tasks to the json file
def save_tasks(tasks):
    with open(working_file, "w") as file:
        json.dump(tasks, file, indent = 4)
        # ident is added for the specing of the json file so it will be more fuman readable 


def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks)+ 1
    # not sure if thats the correct way but the other one is too complex and unreadable 
    task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "created_at": now,
        "updated_at": now    
    }

    tasks.append(task)
    save_tasks(tasks)
    #saves the task done and adds it to the bulk that is to be updated to the file 
    print(f"task added{task_id}: {description}")
    
    # list all the tasks as no filter by status is applied
def list__tasks(status_filter = None):
    tasks = load_tasks()
    if status_filter:
        tasks= [ task for task in tasks if task["status"] == status_filter]
        # list comprehension that filters the tasks with the needed status
    for task in tasks:
        print(f"{task["id"]}: {task["description"]} - {task[status]} - {tas["created_at"]} - {task["updated_at"]}")

def update_task(task_id, status ):
    tasks = load_tasks()
    for task in tasks:
        if task["id" ] == task_id:
            task["status"] = status
            task ["updated_at"] = now
            save_tasks(tasks)
            print(f"task {task_id} updated to {status}")
            return
    print(f"task {task_id} not found")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    #will create another list whrere the id of tasks are not the one that should be excluded 
    if len (tasks) == len(new_tasks):
        print(f"task{task_id}not found")
        return
    save_tasks(new_tasks)
    print("soccessefully delated task {task_id}")

def mark_status(task_id, status):
    tasks = load_tasks()
    for task in rasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updated_at"] = datatime.now().isoformat()
            save_tasks(tasks)
            print(f"task {task_is} marked as {status}")
            return
    print("this task was not found ")

if __name__ == "__main__":
    init_storage()
    args = sys.argv[1:]
    #args for unprevisible number of arguments while writing the cli promp
    #reads what is in the commmand line
    if not args:
        print("no command provided")
        sys.exit(1) 
    # means error
    #sys.exit(0) means success

    cmd = args[0]

    if cmd == "add":
        add_task(args[1])
    elif cmd == "update":
        update_task(int(args[1], args[2]))
    elif cmd == "delete":
        delete_task(int(args[1]))
    elif cmd == "mark-in-progress":
        mark_status(int(args[1]), "in-progress")
    elif cmd == "mark-done":
        mark_status(int(args[1]), "done")
    #no to-do status because it it givem by default when introducing a task in the traker 
    elif cmd == "list":
        if len(args) ==2:
            list_tasks(args[1])
            #the status of the tasks that are asked to be listed are passed as an argument
        else:
            list_tasks()
            #if no status is mentioned it prints everything 
    else:
        print("error in interpreting your command")

