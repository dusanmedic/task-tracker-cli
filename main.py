import menu
import storage
import tasks

def main():
    data = storage.load_data()
    while True:
        menu.show_menu()
        try:
            izbor = int(input("Choose an option: "))
            if izbor is None:
                print("Wrong input, choose option")
                continue
        except ValueError:
            print(f"Wrong input, please choose option \n\n")
            continue
    
        if izbor == 1:
            title = input("Enter Task title: ")
            tasks.add_data(data,title)
            storage.save_data(data)
            print("Task Added! \n\n")
            input("Press any button to continue")
        elif izbor == 2:
            print("\nListing all tasks: \n")
            menu.format_tasks(data)
            input("\nPress any button to continue")
        elif izbor ==3:
            try:
                delete = int(input("Enter task ID to delete "))
            except ValueError:
                print(f"Wrong input, please enter ID")
                delete = int(input("Enter task ID to delete "))
            tasks.delete_task(data,delete)
            storage.save_data(data)
            input("Press any button to continue")
        elif izbor == 4:
            try:
                task_id = int(input("Enter task ID to update "))
            except ValueError:
                print(f"Wrong input, please enter ID")
                task_id = int(input("Enter task ID to update "))
            new_task = input("Enter task Title: ")
            tasks.update_task(data,task_id,new_task)
            storage.save_data(data)
        elif izbor == 5:
            try:
                task_id = int(input("Enter task ID to mark in Progress "))
            except ValueError:
                print(f"Wrong input please enter task ID")
                task_id = int(input("Enter task ID to update "))
            tasks.mark_in_progress(data,task_id)
            storage.save_data(data)
        elif izbor == 6:
            try:
                task_id = int(input("Enter task ID to mark in Progress "))
            except ValueError:
                print(f"Wrong input please enter task ID")
                task_id = int(input("Enter task ID to update "))
            tasks.mark_done(data,task_id)
            storage.save_data(data)
        elif izbor == 7:
            print("Program ends")
            return


if __name__ == "__main__":
    main()




# data = {"tasks":[]}
# tasks.add_data(data,"Test task")
# print(data)