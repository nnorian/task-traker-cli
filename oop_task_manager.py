import json
import os
from oop_task import Task
# imports the created class

class TaskManager:
    # manages the collection of tasks
    # crud operations on the task 

    def __init__ (self, filename = "task.json"):
        self.filename = filename
        self.init_storage()

    def init_storage(self):
        # creates a file if it doesnt exist 
        if not os.path.exists(self.filename):
            with open (self.filename, "w") as file:
                json.dump([], file)
                # writes an empty list to the file 
    
    def load_tasks(self):
        # loads tasks from the file 
        with open(self.filename, "r") as file:
            task_dicts = json.load(file)
            #convert the dictionary to a task object 
            return [Task.from_dict(task_dict) for task_dict in task_dicts]
            # returns a list of task objects

    def save_tasks(self, tasks):
        # saves all the tasks to the storage file 
        task_dicts = [task.to_dict() for task in tasks]
        with open(self.filename, "w") as file:
            json.dump(task_dicts, file, indent = 4)
            # json.dump from python object to a json tring converter method 

    def add_task(self, description):
        # adds a new task with description 
        tasks = self.load_tasks()
        task_id = len(tasks) + 1
        new_task = Task(task_id, description)
        tasks.append(new_task)
        self.save_tasks(tasks)
        return new_task
        # returns the task object created 

    def list_tasks(self, status_filter = None):
        # lists all tasks and filters em by status 
        tasks = self.load_tasks()
        if status_filter:
            tasks = [task for task in tasks if task.status == status_filter]
            # list comprehension
        return tasks
    
    def get_task (self, task_id):
        # gets a task by id
        tasks = self.load_tasks()
        for task in tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id, status ):
        # updates the status of a task
        tasks = self.load_tasks()
        for task in tasks:
            if task.id == task_id:
                task.update_status(status)
                self.save_tasks(tasks)
                return task
        return None
        # returns the task object updated 

    def delete_task(self, task_id):
        # delete task by id 
        tasks = self.load_tasks()
        new_tasks = [task for task in tasks if task.id != task_id]

        if len(tasks) == len(new_tasks):
            return False
            # if no task was deleted
        
        self.save_tasks(new_tasks)
        return True
        # if task was deleted