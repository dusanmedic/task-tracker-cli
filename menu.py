import tasks
import storage
from datetime import datetime

def show_menu():
    print("WELCOME TO TASK TRACKER APP")
    print("*** SELECT OPTIONS ****")
    print("1 - ADD TASK")
    print("2 - LIST ALL TASKS")
    print("3 - DELETE TASK")
    print("4 - UPDATE TASK")
    print("5 - MARK IN PROGRESS")
    print("6 - MARK DONE")
    print("7 - EXIT")

        

def format_tasks(data):
    taskovi = tasks.list_tasks(data)
    
    if not taskovi:
            print("Tasks not found")
    
    for task in taskovi:
        created = datetime.fromisoformat(task["created at"]) 
        created_str = created.strftime("%d.%m.%Y. %H:%M")
        
        if "updated at" in task:
            updated = datetime.fromisoformat(task["updated at"])
            updated_str = updated.strftime("%d.%m.%Y. %H:%M")
            print(
                 f"ID {task['id']}. {task['title']}\nStatus: {task['status']}\n"
                 f"Updated: {updated_str}\n")
        else:
            print(
                 f"ID {task['id']}. {task['title']}\nStatus: {task['status']}\n"
                 f"Created: {created_str}\n")



