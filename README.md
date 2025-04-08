#  Task Tracker 

command-line Task Tracker written in Python using OOP principles  
it allows you to execute CRUD operations on your tasks which are saved in a local json file

---

## Features

- add, update and delete tasks
- mark a tesk as in progress or done 
- List all tasks
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress

---

## Project structure

```
oop_task.py          # defines task class
oop_task_manager.py  # CRUD operations on task 
oop_task_app.py      # CLI interface and command interpreter
oop_main.py          # ontry point 
task.json            # JSON file to store tasks (auto created)
task.py              # same program whitout OOP principles

```

---

### Prerequisites
- Python 3 installed

### Running the app

through terminal run:

```bash
python oop_main.py <command> [arguments]
```

---

## Commands examples

```bash
python oop_main.py add "Finish homework"
python oop_main.py list
python oop_main.py list done
python oop_main.py update 1 in-progress
python oop_main.py mark-done 1
python oop_main.py delete 1
```

---

## Dependencies

only Python built in libraries:
- `json`
- `os`
- `datetime`
- `sys`

---

##  What i learned while working on this project 

- implementation of Object-Oriented Programming (classes, methods, classmethods)
- Working with files in Python and JSON
- CLI tools with argument 

---

## 📄 License

This project is licensed under the MIT License.
