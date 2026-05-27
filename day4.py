def todolist():
    listoftask = {}
    while True:
        choice = int(input("1. add task, 2. view all task ,3. delete , 4.exit: "))
        if choice == 1:
            task = input("enter the task :")
            status = input("WHATS THE STATUS - done , pending:")
            listoftask[task]=status
        elif choice == 2:
            for key, value in listoftask.items():
                print(f"{key}:{value}")
        elif choice == 3:
            delete = input("enter the task to be deleted :")
            if delete in listoftask:
                del listoftask[delete]
            else:
                print("task not found")
        elif choice == 4:
            break
todolist()
