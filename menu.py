# Give the user some context.
print("\nThis program encrypts and decrypts files?")

# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] Enter 1 to create an encryption key.")
    print("[2] Enter 2 to …….")
    print("[3] Enter 3 to……")
    print("[q] Enter q to quit.")

    # Ask for the user's choice.
    choice = input("\nMake your choice ")

    # Respond to the user's choice.
    if choice == '1':
        print("\nEnter a name for the encryption key\n")
    elif choice == '2':
        print("\nEnter …….\n")
    elif choice == '3':
        print("\nEnter ……\n")
    elif choice == 'q':
        print("\nExiting the menu\n")
    else:
        print("\nInvalid option, please try again.\n")

# Print a message that we are all finished.
print("Program exit.")
1
