while True:
    while True:
        print("""
Please select one of the following options
    ------------------------------------------
1. Add a new task.
2. Delete a task.
3. List task.
4. Quit.
        """)

        choice = input("Please enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            break
        else:
            print("Invalid Input")
        
    if choice == 1:
        new_task = input("Please enter a new task: ")
        with open("""E:/python_project/python_project_for_beginners/To-do-List/newTask.txt""","r+") as task:
                line = len(task.readlines())
                task.write(f"#{line}: {new_task}\n")

    if choice == 2:
        delete_task = input("Do you want to delet all task or one task(D or O)? ")
        if delete_task.lower() == "d":
            with open("E:/python_project/python_project_for_beginners/To-do-List/newTask.txt","r+") as task:
                    task.seek(0)
                    task.truncate()
        if delete_task.lower() == "o":
            while True:
                line_delete = input("Which task you want to delete? ")
                if line_delete.isdigit():
                    line_delete = int(line_delete)
                    with open("E:/python_project/python_project_for_beginners/To-do-List/newTask.txt","r+") as task:
                        data = task.readline()
                    with open("E:/python_project/python_project_for_beginners/To-do-List/newTask.txt","w") as task:
                        for line in data:
                            if line.split("\n") != f"#{line_delete}":
                                task.write(line)
                    break
                else:
                    print("Invalid Input")
    if choice == 3:
        with open("E:/python_project/python_project_for_beginners/To-do-List/newTask.txt","r+") as task:
            print(task.read())

    if choice == 4:
        print("GoodBye 👋👋👋")
        break


    