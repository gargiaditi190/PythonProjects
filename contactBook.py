class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    # Add a new contact
    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("✅ Contact added successfully!\n")

    # View all contacts
    def view_contacts(self):
        if not self.contacts:
            print("📭 No contacts found.\n")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact}")
            print()

    # Search contact by name or phone
    def search_contact(self, keyword):
        found = [c for c in self.contacts if c.name == keyword or c.phone == keyword]
        if found:
            for contact in found:
                print(contact)
        else:
            print("❌ Contact not found.")
        print()

    # Update contact
    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_phone: contact.phone = new_phone
                if new_email: contact.email = new_email
                if new_address: contact.address = new_address
                print("✅ Contact updated successfully!\n")
                return
        print("❌ Contact not found.\n")

    # Delete contact
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("🗑️ Contact deleted successfully!\n")
                return
        print("❌ Contact not found.\n")


# ---------- User Interface ----------
def main():
    book = ContactBook()

    while True:
        print("📒 Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            book.add_contact(name, phone, email, address)

        elif choice == "2":
            book.view_contacts()

        elif choice == "3":
            keyword = input("Enter name or phone to search: ")
            book.search_contact(keyword)

        elif choice == "4":
            name = input("Enter name of the contact to update: ")
            phone = input("Enter new phone (leave blank if no change): ")
            email = input("Enter new email (leave blank if no change): ")
            address = input("Enter new address (leave blank if no change): ")
            book.update_contact(name, phone if phone else None,
                                email if email else None,
                                address if address else None)

        elif choice == "5":
            name = input("Enter name of the contact to delete: ")
            book.delete_contact(name)

        elif choice == "6":
            print("👋 Exiting Contact Book. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
