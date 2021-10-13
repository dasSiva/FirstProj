
import os

# Getting username
name = input("Welcome to Apps2U. Please enter your name: ")

# Verifying if file exists for the user
if os.path.exists(name+".txt"):
    print("Welcome back")


# Creating new file if new user
else:
    f = open(name+".txt", "a")
    f.write("Username\t|Password\t|url \n")
    f.close()

print("Enter your selection from the menu")
print("Enter A for adding details")
print("Enter V for viewing the details")
print("Enter Q for exiting the applciation")
choice = ""
while choice != 'Q':
    choice = input("Enter your choice: ")

    if choice == 'A':
        username = input("Enter username: ")
        password = input("Enter password: ")
        url = input("Enter url: ")

        # Encrypting password
        encrpt = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@\'#,\"$!&\\"
        secret = "".join([encrpt[(encrpt.find(character)+3) % 71]
                          for character in password])
        f = open(name+".txt", "a")

        # Saving to file
        f.write(""+username+"\t|" + ""+secret+"\t|"+url+"\n")
        f.close()

    elif choice == 'V':
        f = open(name+".txt", "r")

     # Printing file content
        print(f.read())
