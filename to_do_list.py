tasks = []

def add_task():
    task=input("\nEnter your task you want to add : ")
    tasks.append(task)
    print("\nYour task has been added succesfully to your daily routin")
    

def show_tasks():
    if not tasks:
        print("\nThere is no task to show")
    elif tasks:
        for i,task in enumerate(tasks,1):
            
            print(f"{i}. {task}")

def remove_task():
    show_tasks()
    
    if tasks:
        number= int(input("\nEnter the serial number of your task you want to remove : "))
        tasks.pop(number-1)
        print("\nYour task has been removed succesfully from your daily routin")
        
        
while True :
    print("\n\n1. Show your tasks")
    print("2. Add  task")
    print("3. Remove task")
    print("4. Exit")
    
    choice= input("\nChoose what you want to do : ")

    if choice=="1":
        show_tasks()
    elif choice=="2":
        add_task()
    elif choice=="3":
        remove_task()
    elif choice=="4":
        print("Goodbye for now")
        break
    else :
        print("\nPlease choose between 1-4 ")