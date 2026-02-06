from storage import load_data,save_data
import json
from datetime import datetime

def add_data(data,title):
    # new_id = len(data["tasks"]) + 1
    task = {
        "id": get_next_id(data),
        "title": title,
        "status": "TODO",
        "created at": datetime.now().isoformat(timespec="seconds")
    }
    data["tasks"].append(task)

def get_next_id(data):
    if not data["tasks"]:
        return 1
    return max(task["id"] for task in data["tasks"]) + 1

def list_tasks(data):
    return data["tasks"]


def delete_task(data,task_id):
    for i,task in enumerate(data["tasks"]):
        if task["id"] == task_id:
            print(f"Deleting task {task["id"]} {task['title']}")
            del data["tasks"][i]
            return True
    return False

def update_task(data, task_id,new_task):
    for task in data["tasks"]:
        if task["id"] == task_id:
            print(f"\nUpdated task: ID {task['id']} {task['title']} \n")
            task["title"] = new_task
            task["updated at"] = datetime.now().isoformat(timespec="seconds")    
            return True
    return False


def mark_in_progress(data,task_id):
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["status"] = "IN PROGRESS"
            print(f"Task {task["id"]} is IN PROGRESS")
            return True
    return False

def mark_done(data,task_id):
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["status"] = "DONE"
            print(f"Task {task["id"]} is DONE")
            return True
    return False