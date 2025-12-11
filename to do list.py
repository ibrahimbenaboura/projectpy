Tasks = []


def show_menu() :
    print("=== To Do Menu ===")
    print("1) Add Task")
    print("2) Show Task")
    print("3) Delete Task")
    print("4) Exit")
def add_task():
    task = input("enter new task :")
    Tasks.append(task)
    print("Task Added.")
def show_tasks():
    if not Tasks :
        print("No Tasks Yet.")
        return
    print("Your Tasks :")
    for i, t in enumerate(Tasks, start=1) :
        print(f" {i}- {t}")

def delete_task():
    show_tasks()
    if not Tasks :
        return
    index = int(input("Enter Task Number To Delete :"))
    Tasks.pop(index - 1)
    print("Task Deleted.")

while True :
    show_menu()
    choice = input("Choose One Option :")

    if choice == "1" :
        add_task()
    elif choice == "2" :
       show_tasks()
    elif choice == "3" :
        delete_task()
    elif choice == "4" :
        print("Goodbye!")
        break
    else : 
        print("Invalid Choice")
















