#Hi Siva,
#Simple comments such as "# Checking if choice is A" are not needed as the code is self explanatory,
#Comment to explain sections of code or functions, and provide comments where the code is complicated rather than comment each step.
#for example, "".join([encrptKey[(encrptKey.find(character)-3) % 71]for character in secret_pswd]), is complicated so comment about how it works
#note that there are more than 71 symbols on the keyboard

# importing os library
import os

# global variable assigned with characters that will be used to encrypt and decrypt password
encrptKey = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@\'#,\"$!&\\"

# Getting username
name = input("Welcome to Apps2U. Please enter your name: ")


# Verifying if file exists for the user
if os.path.exists(name+".txt"):
    print("Welcome back")

# Creating new file if new user
else:
    f = open(name+".txt", "x")


# defining the function that saves username,password and url
def add_details():
    # Requesting user for username,password and url
    username = input("Enter username: ")
    password = input("Enter password: ")
    url = input("Enter url: ")

    # Encrypting password
    secret = "".join([encrptKey[(encrptKey.find(character)+3) % 71]
                      for character in password])
    # Opening file to append
    f = open(name+".txt", "a")

    # Saving to file separated by tab and |
    f.write(""+username+"\t|" + ""+secret+"\t|"+url+"\n")
    f.close()


# defining the function that reads file and display content
def view_details():
    # Opening file to read
    f = open(name+".txt", "r")

    # Readlines reads all lines and stores as list in rows.
    rows = f.readlines()

    # Closing file after read
    f.close()
    #  print header
    print("==========================================")
    # Left aligning
    print('{:12}  {:12}  {:12}'.format(
        "Username", "Password", "url"))
    print("==========================================")
    # Going through each items in a list
    for everyrow in rows:
        # Spliting everyrow using tab and | and storing in local variable
        column = everyrow.split("\t|")

        # Password was stored on index 1. Assigning that to secret_pswd
        secret_pswd = column[1]

        # Decrypt the password

        decrpted_pswd = "".join([encrptKey[(encrptKey.find(character)-3) % 71]
                                 for character in secret_pswd])

        # Print username, decrypted password and url formating to be left aligned
        print('{:12}  {:12}  {:12}'.format(
            column[0], decrpted_pswd, column[2]))
        print("----------------------------------------")


# Assigning empty string to choice
choice = ""
while choice != 'Q':
    # Displaying the options menu
    print("Enter your selection from the menu")
    print("Enter A for adding details")
    print("Enter V for viewing the details")
    print("Enter Q for exiting the applciation")

  # Requesting input from user
    choice = input("Enter your choice: ")

   # Checking if choice is A
    if choice == 'A':
        add_details()

    # Checking if choice is V
    elif choice == 'V':
        view_details()

    # Exit application if any other choice
    elif choice != 'Q':
        print("Invalid choice")

# Exiting the application when choice is Q
print("Exiting application")
