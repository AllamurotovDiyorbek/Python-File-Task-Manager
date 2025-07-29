from out import start_m,print_status,print_menyu
from set import (
    is_password,
    add_user,
    laod_users,
    get_user,
    make_password,
    create_task,
    show_tasks,
    mark_tasks,
    view_spefic_tasks,
    load_tasks
)
def main():
    lst=[]
    users=laod_users()
    while True:
        start_m()
        menyu=input("> ")
        if menyu=='1':  
            username=input("Foydalanuvchi nomi: ")
            password=str(input("Parol: "))
            user=get_user(username,password)
            print(user)
            while user==True:
                print_menyu()
                print_status("Muvafiqiyatli kirdingiz","success2")
                choice=input("> ")
                if choice=="1":
                    create_task(username)
                elif choice=="2":
                    show_tasks(username)
                elif choice=="3":
                    view_spefic_tasks(username)
                elif choice=="4":
                    mark_tasks(user)
                elif choice=="5":
                    break
                else:
                    print_status("Faqat 1 dan 5 gacha menyu tanlang","error")
            else:
                print_status("Foydalanuvchi mavjud emas.","error")
        elif menyu=='2':
            username=input("Foydalanuvchi nomi: ")
            password=input("Parol: ")
            parolniqaytar=input("Parolni Takrorlang: ")
           
            if not is_password(password,parolniqaytar):
                print_status("Parol 8 ta belgidan iborat bo`lsin va parol to`gri takrorlanishi kerak.","error2")  
           
            elif username in list(map(lambda user: user['username'],users)):
                print_status("Bu username tanlangan","error")
           
            elif username=="":
                print_status("Usernameni kriting","error")          
            else:
                add_user(username,password,"data/users.txt")
                print_status("Ro`yxatdan o`tdingiz","success")
        elif menyu=='3':
            break
        else:
            print_status("Faqat 1,2 va 3 kiriting.","error2")
main()