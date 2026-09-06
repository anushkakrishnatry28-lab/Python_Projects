#To Do App:-
def task():
    tasks=[]
    total_tasks=int(input("Total tasks you want to enter:- "))
    for i in range(0,total_tasks):
        a=input(f"Enter task {i}:- ")
        tasks.append(a) 
    
    while True:
        operation=int(input("Enter 1-Add\nEnter 2- Update\nEnter 3- Delete\nEnter 4- View\nEnter 5- Exit/Stop"))
        if operation==1:
            add=input("Enter new data:- ")
            tasks.append(add)
            print("Data added successfully")
        elif operation==2:
            update=input("Enter the data you want to update:- ")
            new=input("Enter the new data:- ") 
            if update in tasks:
                ind=tasks.index(update)
                tasks[ind]=new
                print("Data updated successfully")
        elif operation==3:
            delete=input("Enter the data you want to delete:- ") 
            if delete in tasks:
                ind=tasks.index(delete)
                del tasks[ind]
                print("Data deleted successfully")
        elif operation==4:
            print(tasks)
        else:
            print("Invalid input")
            break
task()                              
                
            
