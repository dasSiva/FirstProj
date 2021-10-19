# Hi Siva,
# Simple comments such as "# Checking if choice is A" are not needed as the code is self explanatory,
# Comment to explain sections of code or functions, and provide comments where the code is complicated rather than comment each step.
# for example, "".join([encrptKey[(encrptKey.find(character)-3) % 71]for character in secret_pswd]), is complicated so comment about how it works
# note that there are more than 71 symbols on the keyboard

# importing os library
import os

# global variable assigned with characters that will be used to encrypt and decrypt password
encrptKey = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@\'#,\"$!&\\~%^*()_+=-?/><;:|.{}![] "

name = input("Welcome to Apps2U. Please enter your name: ")


# Verifying if file exists for the user
if os.path.exists(name+".txt"):
    print("Welcome back")

# Creating new file if new user
else:
    f = open(name+".txt", "x")


def add_details():

    username = input("Enter username: ")
    password = input("Enter password: ")
    url = input("Enter url: ")

    # Encrypting password- For every character in password, find the character in the "encryptKey" string and replace it with the character which is located at the 3rd position from that character
    secret = "".join([encrptKey[(encrptKey.find(character)+3) % 95]
                      for character in password])

    f = open(name+".txt", "a")

    # Saving to file separated by tab and |
    f.write(""+username+"\t|" + ""+secret+"\t|"+url+"\n")
    f.close()


def view_details():

    f = open(name+".txt", "r")

    # Readlines reads all lines and stores as list in rows.
    rows = f.readlines()

    f.close()

    #  print header
    print("==========================================")
    # Left aligning
    print('{:12}  {:12}  {:12}'.format(
        "Username", "Password", "url"))
    print("==========================================")

    for everyrow in rows:
        # Spliting everyrow using tab and | and storing in local variable
        column = everyrow.split("\t|")

        # Password was stored on index 1. Assigning that to secret_pswd
        secret_pswd = column[1]

        # Decrypt the password- For every character in the encrypted password, find the character in the "encryptKey" string and replace it with the character which is located 3rd positions to the left

        decrpted_pswd = "".join([encrptKey[(encrptKey.find(character)-3) % 95]
                                 for character in secret_pswd])

        print('{:12}  {:12}  {:12}'.format(
            column[0], decrpted_pswd, column[2]))
        print("----------------------------------------")


choice = ""
while choice != 'Q':

    print("Enter your selection from the menu")
    print("Enter A for adding details")
    print("Enter V for viewing the details")
    print("Enter Q for exiting the applciation")

    choice = input("Enter your choice: ")

    if choice == 'A':
        add_details()

    elif choice == 'V':
        view_details()

    elif choice != 'Q':
        print("Invalid choice")


print("Exiting application")
