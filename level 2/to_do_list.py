phrase ="Welcome lydia concistancy is a key pls do your list!"
print(phrase.upper())
def to_do_list():
    tasks = ["do home work"]

    while True:
         print("1. add a task")
         print("2. show a task")
         print("3. remove the task")
         print("4. exit")

         choose = input("choose an option (1-4):")
         if choose == "1":
             task = input("add your task:")
             tasks.append(task)
             print( task + " added!")

         elif choose =="2":
            print("tasks:")
            for task in tasks:
                print("-" + task)  

         elif choose == "3":
             task_to_remove = input("Enter a task to remove:")
             if task_to_remove in tasks:
                tasks.remove(task_to_remove)
                print("tasks are removed!")
             else:
                print("the task are not yet")
         elif choose == "4":
             print("thank you for ur time. Good Bye!")
             break
         else:
             print("invalid option , try again")

             
         
to_do_list()



