def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. View Contacts")
    print("4. Exit")
    print("-------------------------")

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print(f"Contact '{name}' added successfully.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\n--- Contacts ---")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
    print("----------------")

def main():
    contacts = {}
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            delete_contact(contacts)
        elif choice == '3':
            view_contacts(contacts)
        elif choice == '4':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()