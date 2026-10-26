
import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not load saved contacts.")
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def user_info():
    name = input("Enter your name: ").strip()
    phone = input("Enter your phone number: ").strip()
    email = input("Enter your email: ").strip()

    if not name or not phone or not email:
        print("All fields are required.")
        return None

    return {
        "name": name,
        "phone": phone,
        "email": email
    }


def contact_list():
    contacts = load_contacts()

    while True:
        command = input(
            "Commands: add / search / list / quit >>> "
        ).strip().lower()

        if command == "add":
            contact = user_info()

            if contact:
                contacts.append(contact)
                save_contacts(contacts)
                print("Contact added successfully.")

        elif command == "search":
            search_name = input("Enter a name to search: ").strip()

            matches = [
                contact for contact in contacts
                if search_name.lower() in contact["name"].lower()
            ]

            if matches:
                for contact in matches:
                    print(
                        f"{contact['name']} - "
                        f"{contact['phone']} - "
                        f"{contact['email']}"
                    )
            else:
                print("No matching contacts found.")

        elif command == "list":
            if not contacts:
                print("Your contact list is empty.")
            else:
                for contact in contacts:
                    print(
                        f"{contact['name']} - "
                        f"{contact['phone']} - "
                        f"{contact['email']}"
                    )

        elif command == "quit":
            print("Goodbye!")
            break

        else:
            print("Invalid command. Try again.")


contact_list()
