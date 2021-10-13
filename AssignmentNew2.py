# importing os library
import os

# Getting username
name = input("Welcome to Apps2U. Please enter your name: ")

# Verifying if file exists for the user
if os.path.exists(name+".txt"):
    print("Welcome back")


# Creating new file if new user
else:
    f = open(name+".txt", "a")

    # Adding the heading separated by tab and |
    f.write("Username\t|Password\t|url \n")
    f.close()

# Displaying the options menu
print("Enter your selection from the menu")
print("Enter A for adding details")
print("Enter V for viewing the details")
print("Enter Q for exiting the applciation")

# Assigning choice to empty string
choice = ""
while choice != 'Q':
    # Requesting inout from user
    choice = input("Enter your choice: ")

# Checking if choice is A
    if choice == 'A':

        # Requesting user for username,password and url
        username = input("Enter username: ")
        password = input("Enter password: ")
        url = input("Enter url: ")

        # Encrypting password
        encrpt = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@\'#,\"$!&\\"
        secret = "".join([encrpt[(encrpt.find(character)+3) % 71]
                          for character in password])
        # Opening file to append
        f = open(name+".txt", "a")

        # Saving to file separated by tab and |
        f.write(""+username+"\t|" + ""+secret+"\t|"+url+"\n")
        f.close()


# Chekcing if choice is V
    elif choice == 'V':
        # Opening file to read
        f = open(name+".txt", "r")

     # Readlines reads all lines and stores as list in rows.
    #  List["first line","2nd line","3rd line"] etc
        rows = f.readlines()

        # Going through each items in a list
        for everyrow in rows:

            # Spliting everyrow using tab and |
            column = everyrow.split("\t|")

            # Password was stored on 2nd position-assigning that to secret_pswd
            secret_pswd = column[1]
            # Decrpty the password
            encrptKey = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@\'#,\"$!&\\"
            decrpted_pswd = "".join([encrptKey[(encrptKey.find(character)-3) % 71]
                                     for character in secret_pswd])

            # Print username, decrypted password and url
            print(column[0] + "\t|\t" + decrpted_pswd+"\t|\t"+column[2])

# Exit application if any other choice
    else:
        print("Invalid choice")

# Exiting the application when choice is Q
print("Exiting application")
