def display_menu():
    print("1. Add a note")
    print("2. View notes")
    print("3. Delete a note")
    print("4. Exit")

def add_note():
    notes = input("Enter your note: ")
    with open('notes.txt', "a") as file:
        file.write(notes + "\n")
    print("Note added succesfully")

def view_note():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if notes:
                print("\nYour notes :")
                for idx, note in enumerate(notes, start=1):
                    print(f'{idx}. {note.strip()}')
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No File Found")
    

def delete_note():
    view_note()

    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()

        if notes:
            note_number = input("Enter a note number to delete: ")
            if 1 <= note_number <= len(notes):
                del notes[note_number-1]
                with open("notes.txt", "w") as file:
                    file.writelines(notes)
                print("Note deleted succesfully.")
            else:
                print("No Notes found.")
    except FileNotFoundError:
        print("No File Found.")




def main():
    display_menu()
    while True:
        choice  = input("Enter your choice")
        if choice == '1':
            add_note()
        elif choice == '2':
            view_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print("Exiting....")
            break
        
        else:
            print("Invalid Choice")



main()