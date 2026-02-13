from manager import ContactManager
from model import Contact


def options_menu():
    print("Contact management system")
    print("1.Add Contact")
    print("2.View Contact")
    print("3.Update Contact")
    print("4. Delete contact")
    print("5.Exit")


def main():
    """
    main program for executing contact manager
    """
    manager = ContactManager()

    while True:
        options_menu()
        choice = input("select an option(1-5): ")

        try:
            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")

                contact = Contact(name, phone, email)
                manager.add_contact(contact)
                print("contact added successfully")

            elif choice == "2":
                contact = manager.view_contact()
                if not contact:
                    print("No contact found")
                else:
                    for contact in contact:
                        print(contact)

            elif choice == "3":
                name = input("Enter name of contact to update: ")
                email = input("Enter email of contact to update: ")
                if manager.find_contact(name, email):
                    new_name = input("Enter new name: ")
                    new_phone = input("Enter new phone: ")
                    new_email = input("Enter new email: ")

                    updated_contact = Contact(new_name, new_phone, new_email)
                    manager.update_contact(name, email, updated_contact)
                    print("contact updated successfully.")
                else:
                    print("Contact not found.")

            elif choice == "4":
                name = input("Enter the name of contact to delete: ")
                email = input("Enter email of contact to delete: ")

                if manager.delete_contact(name, email):
                    print("contact deleted successfully")
                else:
                    print("contact not found")
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid option. please choose between 1-5")

        except ValueError as e:
            print(f"validation error: {e}")

        except Exception as e:
            print(f"An error occured: {e}")


if __name__ == "__main__":
    main()
