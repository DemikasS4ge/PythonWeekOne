from cryptography.fernet import Fernet
'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''

master_pass_key = "1234"

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key



def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user,"| Password:",fer.decrypt(passw.encode()).decode())
            
def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



if __name__ == '__main__':
    master_pwd = input("what is the master password? ")
    if master_pwd != master_pass_key:
        print("INVALID")
    else:
        key = load_key() + master_pwd.encode()
        fer = Fernet(key)

        while True:
            mode = input("would you like to add a new password or view existing ones (view/add) or quit (Q)? ").lower()
            if mode == "q":
                break
            
            if mode == "view":
                view()
            elif mode == "add":
                add()
            else:
                print("invalid mode. ")
                continue