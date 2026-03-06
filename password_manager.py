from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

write_key() # Generates the key file 
'''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close
    return key


master_pwd = input("Enter the master password: ")
encrypt_key = load_key() + master_pwd.encode()
fer = Fernet(encrypt_key)


def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("username:", user, ", password", fer.decrypt(passw.encode()).decode())

def add():
    username = input("username: ")
    password = input("password: ")

    with open("passwords.txt", 'a') as f:
        f.write(username + "|" + fer.encrypt(password.encode()).decode() + "\n")

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