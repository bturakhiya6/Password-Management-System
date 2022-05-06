#store and manage passwords
from cryptography.fernet import Fernet

def load_key():
    file = open ("key.key","rb") 
    key = file.read()
    file.close()
    return key


key = load_key() 
fer = Fernet(key)
'''
def write_key():
    key = Fernet.generate_key()
    with open ("key.key","wb") as key_file:
        key_file.write(key)
write_key()'''
         
def view():
    with open('paassword.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user, passw = data
            print("user:", user,"| password:",
                 fer.decrypt(passw.encode()).decode())


def add():
    name=input('account name:    ')
    pwd=input("password:   ")
    with open('paassword.txt','a') as f:
        f.write(name+ "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode=input("would you like to add a new password or view existing ones(view,add) press q to quit? ").lower()
    if mode=="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("invalid.")
        continue 