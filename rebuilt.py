
import os

print("Welcome to the APP")
name = input("Enter username:")

if os.path.exists(name+".txt"):
    print("welcome back")

else:
    print("File doesn't exist. Creating a new file")
    user_file = open(name+".txt", "x")


def menulist():
    print("Enter choice A for adding details:")
    print("Enter choice V for viewing detais:")
    print("Enter Q for exit:")
    choice = input("Enter choice:")
    return choice


choice = menulist()
while choice == "A":
    username = input("Enter username:")
    password = input("Enter password:")
    url = input("URL")
    encrptKey = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@\'#,\"$!&\\"
    secret = "".join([encrptKey[(encrptKey.find(character)+3) % 71]
                      for character in password])
    f = open(name+".txt", "a")
    f.write(username + "|" + password+"|" + url)
    choice = menulist()

while choice == "V":
    f = open(name+".txt", "r")
    for everyrow in f:
        encpass = everyrow[1]
    encrptKey = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@\'#,\"$!&\\"
    decrpted_pswd = "".join([encrptKey[(encrptKey.find(character)-3) % 71]
                             for character in encpass])
    print("username| password| url")
    print(everyrow[0] + "|" + decrpted_pswd + "|" + everyrow[2])
    choice = menulist()

if choice == "Q":
    print("Exiting application")

else:
    print("invalid choice")
