from termcolor import colored
def start_m():
    print("1.Kirish ")
    print("2.Royxatdan ot`ish")
    print("3.Exit")
def print_status(text,condition):
    types={
        'error':'red',
        'error2':'yellow',
        'success':'green',
        'success2':'blue'
    }
    colored_text=colored(text,types[condition])
    print(colored_text)
def print_menyu():
    print("1.Task yaratish (Create task)")
    print("2.Tasklarni ko`rish")
    print("3.Belgilangan tasklarni ko`rish")
    print("4.Tasklarni bajarildi qilish")
    print("5.Bosh menyuga o`tish")