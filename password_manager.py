master_pwd = input("Enter the master password: ")

def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("username:", user, ", password", passw)

def add():
    username = input("username: ")
    password = input("password: ")

    with open("passwords.txt", 'a') as f:
        f.write(username + "|" + password + "\n")

while True:
    mode = input("Would you like to add a new password or view all passwords? or press q to quit (view/add/q): ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Enter a valid input")
        continue