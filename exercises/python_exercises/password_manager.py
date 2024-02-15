pwd = input("What is the master password? ")

def view():


while True:
    mode = input("Would you like to a new password or view existing ones (view, add, Q)? ").lower()
    if mode == 'q':
        break
        
    if mode == "view":
        print()
    elif mode == "add":
        print()
    else:
        print("Not a valid option")