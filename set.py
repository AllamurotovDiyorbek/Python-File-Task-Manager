from hashlib import sha224
from out import print_status


def is_password(password,confirm_password)->bool:
    return len(password) >= 8 and password==confirm_password
def make_password(password):
    hash_password=sha224(password.encode()).hexdigest()
    return hash_password

def add_user(username,password,file1):
    with open(file1,"a") as f:
        f.write(f"{username}, {make_password(password)}\n")
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
            return True
        else:
            pass
def create_task(user):
    title=input("title ")
    description=input("description ")
    time=input("time ")
    completed='bajarilmagan'
    text = f"{user}, {title}, {description}, {time}, {completed} \n"
    if title!="" and description!="" and time!="":
        print("yozilyapti")
        with open("data/tasks.txt","a") as f:
            f.write(text)
    else:
        print("xato")
def load_tasks():
    with open('data/tasks.txt' , 'r') as f:
        tasks=[]
        for line in f.readlines():
            u=line[:-1].split(", ")
            print(u)
            tasks.append({
                'user':u[0],
                'title':u[1],
                'description':u[2],
                'time':u[3],
                'completed':u[4]                                                                                                                                                                                          
            })
    return tasks
def show_tasks(user):
    tasks=load_tasks()
    for c,i in enumerate(tasks, start=0):
            if i['user']==user: 
                print(f'{c} {i}')
def mark_tasks(user):
    pass
        
mark_tasks('Ali')   
def view_spefic_tasks(user):
    with open("data/tasks.txt","a") as f:
        w=load_tasks()
        for i in w:
            if i['completed']=="bajarildi":
                print(i)
            else:
                pass    