
mytasklist = [['human', 'life'], ['take', 'all'], ['fire', 'context']]

for i in mytasklist:  # create status for preexisiting tasks
    if len(i) != 0:
        mytasklist[mytasklist.index(i)].append('pending')

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Filter Tasks")
    print("7. Load Tasks")
    print("8. Exit")
    choice = input("Enter your choice: ")
        # Your Main Program Logic Start Here





    if choice == "1":
            add_task= input("please input the name of the task you want to complete:")
            add_description=input("Optionally, provide a short description for it:")
            new_task=[add_task, add_description,'pending']
            mytasklist.append(new_task)
    if choice == "2":
        cco=1
        for i in mytasklist:
            print(cco,")",i[0], ": ", end='')  # access the first sub item in the item indicated by i
            print(i[1])
            cco+=1


    if choice == "3":
        print(mytasklist)
        edit_choose=input("please input the name of the task you want to edit:")
        edit_new=input("what task do you want to replace it with:")
        edit_description=input("Optionally, provide a short description for it:")
        for i in mytasklist:
            if i[0]==str(edit_choose): #idk make both strings
                i[0]=edit_new
                i[1]=edit_description
                print("Task updated successfully.")
            else:
                print("Task not found in:",i)

    if choice == "4":
        print(mytasklist)
        delete_choose=input("please input the name of the task you want to delete:")
        for i in mytasklist:
            if i[0]==delete_choose:
                mytasklist.pop(mytasklist.index(i))
                print("Task deleted successfully.")

    if choice == "5":
        print(mytasklist)
        change_index = input("please input the name of the task you want to mark as completed:")
        for i in mytasklist:
            if i[0] == str(change_index):
                i[2] = "completed"
                print("Task marked successfully.")

    if choice == "6":
        print(mytasklist)
        filterChoice= input("please input the status of the task you want to filter:")
        if filterChoice == "completed":
            for i in mytasklist:
                if i[2] == "completed":
                    print(mytasklist.index(i)+1,")",i[0],": ",i[1])
        elif filterChoice == "pending":
            for i in mytasklist:
                if i[2] == "pending":
                    print(mytasklist.index(i)+1,")",i[0],": ",i[1])
        else:
            print("Invalid choice")

    if choice == "7":
        myfile = open("New Text Document.txt","r+")
        for i in mytasklist:
            print(i, file=myfile)
            print(i)
        myfile.close()

    if choice == "8":
        break