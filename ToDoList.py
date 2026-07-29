import pandas as pd
import datetime
import os

file= "Tasks.csv"

if os.path.exists(file): # check if the csv file exists or not 
    df = pd.read_csv(file)
else: # if not creating a new one 
    df = pd.DataFrame(columns=["Task", "Done", "Date"])
    df.to_csv(file, index=False)

def addTask():
    global df
    task=input("Enter your Task: ") # taking the task as string 
    
    df_toadd = { # and added it to a dic
        "Task": [task],
        "Done": ["No"],
        "Date": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")] # added time 
    }
    df_toadd=pd.DataFrame(df_toadd) # convert the dic to dataframe and added it to the main dataframe 
    df = pd.concat([df, df_toadd], ignore_index=True)
    df.to_csv("Tasks.csv", index=False)
    print("Task added\n")

def removeTask():
    if len(df)==0: print("No tasks to remove\n")# if there is no task there is nothing to delete
    else:
        while 1:
            try: # if ID exist remove it
                ID = int(input("Enter Task ID: "))-1
                df.drop(df.index[ID], inplace=True)
                df.reset_index(drop=True, inplace=True) # reseting the IDs
                df.to_csv("Tasks.csv", index=False)
                print("Task removed\n")
                break

            except: print("Enter a valid ID\n") 

def clearTasks(): # to clear all Tasks (I added it bc I wanted to removes many task while solving some bugs so I decided to add it as feature)
    global df
    clear = input("Are you sure you want to delete all tasks? ").lower() # bc I don't want to remove all tasks by accedint 
    while 1:
        match clear:
            case "yes":
                df = pd.DataFrame(columns=["Task", "Done", "Date"])
                df.to_csv("Tasks.csv", index=False)
                print("All tasks have been deleted.\n")
                break
            case "no": break
            case _: print("Enter a valid choice")


def viewTasks(): # gro though evert task in the csv file and view it 
    if len(df)==0:
        print("No tasks to view\n")
    else:
        for i in df.index:
            print(f"{i+1}- {df.loc[i,"Task"]}, Done: {df.loc[i,"Done"]}, Date: {df.loc[i,"Date"]}")
            print("\n")

def markTaskasDone(): # convert Done to Yes
    if len(df)==0: print("No tasks to Mark\n")
    else:
        while 1:
            try: 
                ID = int(input("Enter Task ID: "))-1
                df.loc[ID,"Done"] = "Yes"
                df.to_csv("Tasks.csv", index=False)
                print("Task is Done\n")
                break
            except: print("Enter a valid ID\n")

def markTaskasNotDone(): # convert Done to No
    if len(df)==0: print("No tasks to unMark\n")
    else:
        while 1:
            try: 
                ID = int(input("Enter Task ID: "))-1
                df.loc[ID,"Done"] = "No"
                df.to_csv("Tasks.csv", index=False)
                print("Task is not Done\n")
                break
            
            except: print("Enter a valid ID\n")

def editTask(): # edit a task :D
    if len(df)==0: print("No tasks to edit\n")
    else:
        while 1:
            ID = int(input("Enter Task ID: ")) - 1 # subtracting 1 from every ID bc in pandas ID starts from 0 but in my app starts from 1 
            try:
                df.loc[ID,"Task"] = input("Enter the edit: ")
                df.to_csv("Tasks.csv", index=False)
                print("Task edited\n")
                break
            except: print("Enter a valid ID\n")

        

print("Welcome to LIGHTNING MCQUEEN'S TO-DO LIST \nWhat do u want to do Friend!")


while 1:
    print("1- Add a Task\n2- Remove a Task\n3- Edit a Task\n4- Mark Task as Done\n5- Mark Task as not Done\n6- View all Tasks\n7- clear all Tasks\n8- Quit")
    opt = input("Select your choice friend: ")
    match opt:
        case "1": addTask()
        case "2": removeTask()
        case "3": editTask()
        case "4": markTaskasDone()
        case "5": markTaskasNotDone()
        case "6": viewTasks()
        case "7": clearTasks()
        case "8": break
        case _: print("Enter a valid number dude >:(\n")