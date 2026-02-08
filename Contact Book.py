import os

contact_file = "contacts.txt"


def create_contact_file():
    if not os.path.exists(contact_file):
        with open(contact_file, "w") as file:
            file.write("")


def add_contacts():
    name = input("Enter Contact name: ")
    number = int(input("Enter number: "))

    contact_data = f"{name}, {number}"

    with open(contact_file, "a") as file:
        file.write(contact_data)
        print(f"Contact saved: {name} - {number}")

    return name, number


def view_contacts():
    try:
        with open(contact_file, "r") as file:

            contacts = file.readlines()

        if not contacts:
            print("No contacts found")
            return

        for i, contact in enumerate(contacts, start=1):
            parts = contact.strip().split(",")

            if len(parts) >= 2:
                name, phone = parts[0], parts[1]
                print(f"{i}. Name: {name:10} | Phone: {phone}")
            else:
                print("Invalid contact format")
    except FileNotFoundError:
        print("No contacts found. Add some contacts first.")


def search_contact():
    search = input("Enter name: ")
    try:
        with open(contact_file, "r") as file:
            contacts = file.readlines()
            found = False
            for contact in contacts:
                parts = contact.strip().split(",")
                if len(contact) >= 2 and parts[0] == search:
                    name, phone = parts[0], parts[1]
                    print("✓ Contact Found!")
                    print(f"   Name: {name}")
                    print(f"   Phone: {phone}")
                    found = True
                    break

            if not found:
                print(f"No contact found with name: {search}")
    except FileNotFoundError:
        print("No contacts found. Add some contacts first.")


def delete_contact():
    delete_name = input("Enter name to delete: ")

    try:
        with open(contact_file, "r") as file:
            contacts = file.readlines()

            new_contacts = []
            deleted = False

            for contact in contacts:
                part = contact.strip().split(",")

                if part and part[0] != delete_name:
                    new_contacts.append(contact)

                else:
                    deleted = True

            if deleted:
                with open(contact_file, "w") as file:
                    file.writelines(new_contacts)
                print(f"Contact {deleted} is deleted successfully")
    except FileNotFoundError:
        print("No contacts found. Add some contacts first.")


def contact_menu():

    create_contact_file()

    while True:
        print("=" * 10, "Contacts Menu", 10 * "=")
        print("1- Add Contact")
        print("2- View All Contacts")
        print("3- Search For a Contact")
        print("5- To Quite")
        print()

        print("-" * 20)
        user = int(input("Enter (1-5): "))
        if user == 1:
            print("=" * 10, "Add Contact", 10 * "=")
            add_contacts()
        if user == 2:
            print("=" * 10, "View Contacts", 10 * "=")
            view_contacts()
        if user == 3:
            print("=" * 10, "Search For a Contacts", 10 * "=")
            search_contact()
        if user == 5:
            break


if __name__ == "__main__":
    contact_menu()
