import sys 
from oop_task_manager import TaskManager

class TaskApp:
    # cli interface 
    # for managing user interactions and command processing 

    def __init__(self, filename = "task.json"):
        self.task_manager = TaskManager(filename)

    def display_help(self):
        # displays the help message to the users 
        print("~commands for task manager app~")
        print(" add <description> - add a new task")
        print(" list - lists all tasks ")
        print(" list<status> - list tasks with a specific status ")
        print(" update <id> <status> - update task status ")
        print(" delete <id> - deletes a task")
        print(" mark-in-progress <id> - marks task as in progress")
        print(" mark-done <id> - marks task as done")
        print(" help - displays this help message ")

    def display_task(self,task):
        # display one task with all its info 
        print(f" {task.id}: {task.description} - {task.status}")
        print(f" created: {task.created_at}")
        print(f" updated: {task.updated_at}")

    def cmd_add(self, args):
        # handles add command
        if len(args) < 1:
            print("description is required")
            return
        description = args[0]
        task = self.task_manager.add_task(description)
        print(f"task added [{task.id}]: {task.description}")

    def cmd_list(self, args):
        # handles list program
        status_filter = args[0] if args else None
        tasks = self.task_manager.list_tasks(status_filter)

        if not tasks:
            print("no tasks found")
            return 

        print (f"tasks{ 'with status' + status_filter if status_filter else ''}")
        for task in tasks:
            print(f"[{task.id}]: {task.description} - {task.status}")

    def cmd_update(self, args):
        # handles update commands 
        if len(args) < 2:
            print(" error: missing id or status")
            
        try:
            task_id = int(args[0])
            status = args[1]
            task = self.task_manager.update_task(task_id, status)

            if task:
                print(f"task {task.id} updatet to {status}")
            else:
                print(f"task {task_id} not found")
        except ValueError:
            print("error: task id should be a number")
            

    def cmd_delete(self, args):
        # handles delete program
        if len(args) <1:
            print("error: missing id ")
            return
        try:
            task_id = int(args[0])
            success = self.task_manager.delete_task(task_id)

            if success:
                print(f"successefuly deleted {task_id} ")
            else:
                print(f"task {task_id} not found")
            
        except ValueError:
            print("error: task id should be a number")

            
    def cmd_mark_status(self, args, status):
        # namdles the program that marks status 
        if len(args) < 1:
            print("error: missing task id")
            return
        try:
            task_id = int(args[0])
            task = self.task_manager.update_task(task_id, status)

            if task:
                print(f" task {task.id} marked as {status}")
            else:
                print(f"task {task_id} not found")
        except ValueError:
            print("error: task id should be a number")
                
    def run(self, args):
        #main method that runs the app

        if not args or args[0] == "help":
            self.display_help()
            return
                
        cmd = args[0]
        cmd_args = args[1:]

        if cmd =="add":
            self.cmd_add(cmd_args)
        elif cmd =="list":
            self.cmd_list(cmd_args)
        elif cmd =="update":
            self.cmd_update(cmd_args)
        elif cmd =="delete":
            self.cmd_delete(cmd_args)
        elif cmd =="mark-in-progress":
            self.cmd_mark_status(cmd_args, "in-progress")
        elif cmd =="mark-done":
            self.cmd_mark_status(cmd_args, "done")
        else:
            print(f"unknown command: {cmd}")
            self.display_help()