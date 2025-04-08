import datetime

class Task:
    # this class will contain all the properties and methods of a task

    def __init__(self, task_id, description):
        self.id = task_id
        self.description = description
        self.status = "todo"
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def update_status(self, status):
        #update status and updated_at
        self.status = status
        self.updated_at = datetime.datetime.now().isoformat()
        # isoformat will convert the date to a string in the format YYYY-MM-DDTHH:MM:SS.ssssss
    
    def to_dict(self):
        # convert the task to a dictionary 
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    """@classmethod is a built-in decorator in Python that transforms 
    a regular method into a class method. When you 
    use this decorator, the method receives the class 
    itself as its first parameter (conventionally named cls) 
    instead of an instance (which would be self)."""

    @classmethod
    def from_dict(cls, task_dict):
        #create task object from dictionary 
        task = cls(task_dict["id"], task_dict["description"])
        task.status = task_dict["status"]
        task.created_at = task_dict["created_at"]
        task.updated_at = task_dict["updated_at"]
        return task
    
    def __str__ (self):
        # displays the string representation of the task
        return f"[{self.id}]: {self.description} - {self.status} - {self.created_at} - {self.updated_at}"