import sys
from oop_task_app import TaskApp

if __name__ == "__main__":
    app = TaskApp()
    app.run(sys.argv[1:])
    # run the app with the command line arguments