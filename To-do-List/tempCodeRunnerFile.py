    with open("newTask.txt","r+") as task:
                    task.seek(0)
                    task.truncate()