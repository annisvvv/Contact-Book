# WELCOME

import os

contacts_file = "contacts.txt"

#########################################################################
def load_contacts():
    contacts = []

    if not os.path.exists(contacts_file):
        return contacts
    
    # encoding fixed -> "utf-8"
    with open(contacts_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 3:
                print(f"⚠️ Skipping bad line in file: {line}")
                continue
            name, phone, email = parts
            contacts.append({
                "name": name.strip(),
                "phone": phone.strip(),
                "email": email.strip()
            })
    return contacts

#########################################################################
def save_contacts(contacts):
    with open(contacts_file, "w", encoding="utf-8") as f:
        for c in contacts:
            line = f"{c['name']},{c['phone']},{c['email']}\n"
            f.write(line)

#########################################################################
def add_contact(contacts):
    print("\nAdd a new contact")
    name = input("Enter name = ").strip()
    phone = input("Enter phone number : ").strip()
    email = input("Enter email : ").strip()

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("✅ Contact added successfully!\n")

#########################################################################
def view_contacts(contacts):
    print("\nAll contacts")
    if not contacts:
        print("No contacts found.\n")
        return
    
    for i, c in enumerate(contacts, start=1):
        # use single quotes inside f-string for dict keys
        print(f"{i}. {c['name']} - {c['phone']} - {c['email']}")
    print()

#########################################################################
def search_contacts(contacts):
    query = input("\nEnter name to search: ").strip().lower()
    found = [c for c in contacts if query in c["name"].lower()]

    if not found:
        print("No matching contacts found.\n")
        return
    
    print("matches:")
    for c in found:
        print(f"- {c['name']} - {c['phone']} - {c['email']}")
    print()

#########################################################################
def delete_contacts(contacts):
    target = input("\nEnter exact name to delete: ").strip().lower()

    for c in contacts:
        if c["name"].lower() == target:
            contacts.remove(c)
            save_contacts(contacts)
            print("🗑️ Contact deleted.\n")
            return
    print("Contact not found.\n")

#########################################################################
def main():
    contacts = load_contacts()
    print(f"(Your contacts file will be here): {os.path.abspath(contacts_file)}\n")

    while True:
        print("📒 Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            delete_contacts(contacts)
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()