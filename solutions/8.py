"""
1. write a program to maintain a list of daily tasks and perform operations on it
    -- add a new task (avoid repeatations)
    -- delete a given task (check if the task exists. if not print error message, if list empty, print error)
    -- delete all tasks (check if list empty)
    -- show all tasks (check if list empty)
"""

dailyTasks = []

def printList():
    if len(dailyTasks) != 0:
<<<<<<< HEAD
        print(dailyTasks)
    else:
        print("list is empty")

def addNewTask(task):
    if task in dailyTasks:
        print("this task already exists")
=======
        print (dailyTasks)
    else:
        print ("list is empty")

def addNewTask(task):
    if task in dailyTasks:
        print ("this task already exists")
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd
        return
    else:
        dailyTasks.append(task)
        return

def removeTask(task):
    if task not in dailyTasks:
<<<<<<< HEAD
        print("task unavailable")
=======
        print ("task unavailable")
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd
    else:
        dailyTasks.remove(task)


printList()
addNewTask('wake up')
printList()
addNewTask('get ready')
printList()

removeTask('wake up')

printList()
