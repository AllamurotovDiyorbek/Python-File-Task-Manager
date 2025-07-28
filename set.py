from hashlib import sha224
from out import print_status
def is_password(password,confirm_password)->bool:
    return len(password) >= 8 and password==confirm_password

def make_password(password:str):
    hash_password=sha224(password.encode()).hexdigest()
    return hash_password

def add_user(username,password,file1):
    with open(file1,"a") as f:
        f.write(f"{username}, {password}\n")
        
def laod_users():
    with open("data/users.txt","r") as f:
        users =[]
        for line in f.readlines():
            a = line[:-1].split(", ")
            users.append({
                "username":a[0],
                "password":a[1]
                })
        return users
def get_user(username,password):
    users=laod_users()
    for i in users:
        if i['username']==username and i['password']==make_password(password):
            return i
        else:
            pass
def load_tasks(user):
    with open('data/tasks.txt' , 'r') as f:
        tasks=[]
        for line in f.readlines():
            u=line[:-1].split()
            tasks.append({
                'user':u[0],
                'title':u[1],
                'description':u[2],
                'time':u[3],
                'completed':u[4]                                                                                                                                                                                          
            })
    return tasks
def create_task(user):  
    user,
    title=input("title "),
    description=input("description "),
    time=input("time ")
    text={"username":user,"title":title,"description":description,"time":time,"completed":"bajirlmadi"}
    if title!="" and description!="" and time!="":
        with open("data/tasks.txt","a") as f:
            f.writelines(f"{text['username']} {text['title']} {text['description']} {text['time']} {text['completed']}")
    else:
        print("xato")
def show_tasks(user):
    tasks=load_tasks(user=user)
    for i in tasks:
            if i['user']==user:
                print(i)

def mark_tasks(user):
    with open("data/tasks.txt","a") as f:
        w=load_tasks(user)
        for i in w:
            if i['completed']=="bajarildi":
                print(i)
            else:
                pass    
def view_spefic_tasks(user):
    pass