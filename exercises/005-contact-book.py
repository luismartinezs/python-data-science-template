import json
from typing import List, Dict, Optional


class Contact:
    def __init__(self, name: str, phone: str, email: str, address: str):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
        }


class ContactBook:
    def __init__(self):
        self.contacts: List[Contact] = []

    def add_contact(self, contact: Contact) -> None:
        self.contacts.append(contact)

    def remove_contact(self, name: str) -> None:
        self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]

    def search_contacts(self, query: str) -> List[Contact]:
        query = query.lower()
        return [
            c
            for c in self.contacts
            if query in c.name.lower()
            or query in c.phone
            or query in c.email.lower()
            or query in c.address.lower()
        ]

    def display_contacts(self) -> None:
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone: {contact.phone}")
            print(f"Email: {contact.email}")
            print(f"Address: {contact.address}")
            print("-" * 20)

    def save_to_file(self, filename: str) -> None:
        with open(filename, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f)

    def load_from_file(self, filename: str) -> None:
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.contacts = [Contact(**c) for c in data]
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty contact book.")


def main():
    contact_book = ContactBook()
    contact_book.load_from_file("contacts.json")

    while True:
        print("\n1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contacts")
        print("4. Display All Contacts")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(Contact(name, phone, email, address))
        elif choice == "2":
            name = input("Enter name to remove: ")
            contact_book.remove_contact(name)
        elif choice == "3":
            query = input("Enter search query: ")
            results = contact_book.search_contacts(query)
            if results:
                for contact in results:
                    print(f"{contact.name}: {contact.phone}")
            else:
                print("No contacts found.")
        elif choice == "4":
            contact_book.display_contacts()
        elif choice == "5":
            contact_book.save_to_file("contacts.json")
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
