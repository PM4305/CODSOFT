import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='root',database='todo_list')
cur=con.cursor()
#cur.execute("create database todo_list")
#cur.execute("create table tasks(Serial_No int primary key AUTO_INCREMENT,Task_Name varchar(50),Description varchar(100),Status varchar(50) Default 'Not Started')")
#con.commit()
def MainMenu():
    print("\n1. Add Task")
    print("2. Update To-Do List")
    print("3. Track or View To-Do List")
    n=int(input("\nEnter Your Choice: "))
    if n==1:
        AddTask()
    elif n==2:
        UpdateList()
    elif n==3:
        ViewList()
    else:
        print("\n!!Wrong Input!!\n")
        MainMenu()

def AddTask():
    ch='y'
    while ch=='y':
        print("\nEnter Task Details: \n")
        name=input("Enter Task Name: ")
        desc=input("Enter Task Description: ")
        cur.execute("insert into tasks(Task_Name,Description) values('{0}','{1}')".format(name,desc))
        con.commit()
        ch=input("\nDo you want to add more tasks(y/n): ")
    print("\n1. MainMenu\n2. Exit")
    m=int(input("Enter your Choice: "))
    if m==1:
        MainMenu()
    else:
        exit()

def UpdateList():
    print("\n             Update To-Do List\n")
    ch='y'
    while ch=='y':
        print("Search Task By: \n")
        print("1. Serial Number\n2. Task Name\n3. Task Description")
        n=int(input("Enter Your Choice: "))
        if n==1:
            sno=input("\nEnter Serial Number of the Task: ")
            cur.execute("select * from tasks where Serial_No='{0}'".format(sno))
        elif n==2:
            name=input("Enter Task Name: ")
            cur.execute("select * from tasks where Task_Name='{0}'".format(name))  
        elif n==3:
            desc=input("Enter Description of the Task: ")
            cur.execute("select * from tasks where Description='{0}'".format(desc))  
        else:
            print("\n!!Wrong Input!!\n")
            MainMenu()
        task=cur.fetchone()
        if len(task)!=0:
            print("\n           Task Found\n")
            stat=input("Enter the Current Status of the Task (Not Started, In Progress, Done): ")
            cur.execute("update tasks set Status='{0}' where Serial_No={1}".format(stat,task[0]))
            con.commit()
        else:
            print("\n!No Such Task Found!\n")
            MainMenu()
        ch=input("\nDo you want to update more tasks(y/n): ")
    print("\n1. MainMenu\n2. Exit")
    m=int(input("Enter your Choice: "))
    if m==1:
        MainMenu()
    else:
        exit()
    
def ViewList():
    print("\n                     To-Do List\n")
    cur.execute("select * from tasks")
    tasks=cur.fetchall()
    print("S.No.     Task Name     Description       Status\n")
    for row in tasks:
        print(row[0],"         ",row[1],"            ",row[2],"         ",row[3])
    print("\n1. MainMenu\n2. Exit")
    m=int(input("Enter your Choice: "))
    if m==1:
        MainMenu()
    else:
        exit()

print("                       To-Do List Application\n")
MainMenu()
















    
