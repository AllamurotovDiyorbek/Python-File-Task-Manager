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
        
# def laod_users():
#     with open("data/users.txt","r") as f:
#         users =[]
#         s=f.readlines()
#         username=str()
#         password=str()
#         for line in s:
#             username , password = line[:-1].split(", ")
#             users.append({
#                 "username":username,
#                 "password":password
#                 })
#         return users
def get_user(username,password):
    users=laod_users()
    for i in users:
        if i['username']==username and i['password']==make_password(password):
            return i['username']
        else:
            pass
def create_task(user):
    user,
    title=input("title "),
    description=input("description "),
    time=input("time ")
    text={"username":user,"title":title,"description":description,"time":time,"completed":"bajirlmadi"}
    if title!="" and description!="" and time!="":
        with open("data/tasks.txt","a") as f:
            f.writelines(f"{text['username']},{text['title']},{text['description']},{text['time']},{text['completed']}\n")
    else:
        print("xato")
def load_tasks(user):
    with open('data/tasks.txt' , 'r') as f:
        tasks=[]
        for line in f.readlines():
            user,title,description,time=line[:-1].split(', ')
            tasks.append({
                'user':user,
                'title':title,
                'description':description,
                'time':time,
                'completed':"bajarilmagan"                                                                                                                                                                                             
            })
    return tasks
def show_tasks(user):
    tasks=load_tasks(user=user)
    for i in tasks:
            if i['user']==user:
                print(i)

def mark_tasks(user):
    with open("data/tasks.txt","a") as f:
        w=load_tasks()
        for i in w:
            if i['completed']=="bajarilmadi":
                print(i)
            else:
                pass
def view_spefic_tasks(user):
    pass