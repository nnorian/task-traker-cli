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
        print(" list<status> - list tasks with a pecific status ")
        print(" update <id> <>status - update task status ")
        print(" delete <id> - deletes a task")
        print(" mark-in-progress <id> - marks task as in progress")
        print(" mark-done <id> - marks task as done")
        print(" help - displays this help message ")

        