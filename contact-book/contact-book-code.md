
Contact Book Application
------------------------------------
A simple command-line contact management app.
It allows the user to:
1. Add new contacts
2. View all contacts
3. Search for a contact
4. Delete a contact

All contacts are saved in a local file ('contacts.txt') for persistence.

Concepts used:
- File handling
- Lists and dictionaries
- Loops and conditionals
- Input validation
"""

import os  # Used to check file existence and handle deletions

# Utility Functions


def load_contacts():
    """Reads all contacts from 'contacts.txt' and returns them as a list of dictionaries."""
    contacts = []
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, email = line.strip().split("|")
                contacts.append({"name": name, "phone": phone, "email": email})
    return contacts


def save_contacts(contacts):
    """Saves all contacts to 'contacts.txt'."""
    with open("contacts.txt", "w") as file:
        for c in contacts:
            file.write(f"{c['name']}|{c['phone']}|{c['email']}\n")



# Core Functionality


def add_contact(contacts):
    """Adds a new contact to the list and saves it."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if not name or not phone:
        print("Name and phone number are required!")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.\n")


def view_contacts(contacts):
    """Displays all contacts."""
    if not contacts:
        print("No contacts found.\n")
        return

    print("\nYour Contacts:")
    print("-" * 40)
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. Name: {c['name']}")
        print(f"   Phone: {c['phone']}")
        print(f"   Email: {c['email']}\n")
    print("-" * 40)


def search_contact(contacts):
    """Searches for a contact by name or phone number."""
    keyword = input("Enter name or phone number to search: ").strip().lower()
    results = [c for c in contacts if keyword in c["name"].lower() or keyword in c["phone"]]

    if not results:
        print("No matching contacts found.\n")
        return

    print("\nSearch Results:")
    print("-" * 40)
    for c in results:
        print(f"Name: {c['name']}")
        print(f"Phone: {c['phone']}")
        print(f"Email: {c['email']}\n")
    print("-" * 40)


def delete_contact(contacts):
    """Deletes a contact by name."""
    name = input("Enter the name of the contact to delete: ").strip().lower()
    for c in contacts:
        if c["name"].lower() == name:
            contacts.remove(c)
            save_contacts(contacts)
            print(f"Contact '{c['name']}' deleted successfully.\n")
            return
    print("Contact not found.\n")


# Main Application Loop


def main():
    """Main menu loop."""
    contacts = load_contacts()

    while True:
        print("""
CONTACT BOOK =========
1. View all contacts
2. Add a new contact
3. Search for a contact
4. Delete a contact
5. Exit
)
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye! Your contacts are saved.")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.\n")


# Run the program
if __name__ == "__main__":
    main()
