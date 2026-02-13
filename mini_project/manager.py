import json
import os

from model import Contact


class ContactManager:
    """
    handles the add,view,find,update,delete contacts
    """

    def __init__(self, file_path="contacts.json"):
        self.file_path = file_path
        self.contacts = self._load_contacts()

    def _load_contacts(self):
        """
        Load contacts from the JSON file.

        Returns:
            list: A list of Contact objects.
                  Returns an empty list if the file does
                  not exist
        """
        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return [Contact.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError):
            return []

    def _save_contact(self):
        """
        Save all contacts to the JSON file.

        Converts Contact objects into dictionaries
        before writing them to the file.
        """
        with open(self.file_path, "w") as file:
            json.dump([c.to_dict() for c in self.contacts], file, indent=4)

    def add_contact(self, contact: Contact):
        """
        Add a new contact to the contact list.

        :param contact: The Contact object to be added.
        :type contact: Contact
        """

        self.contacts.append(contact)
        self._save_contact()

    def view_contact(self):
        """
        Retrieve all stored contacts.
        """
        return self.contacts

    def find_contact(self, name: str, email: str):
        """
        Search for a contact by name and email.

        :param name: Name of the contact.
        :type name: str
        :param email: Email of the contact.
        :type email: str
        """
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if contact.email == email:
                    return contact
        return None

    def update_contact(self, name: str, email: str, new_contact: Contact):
        """
        Update an existing contact.

        :param name: Current name of the contact.
        :type name: str
        :param email: Current email of the contact.
        :type email: str
        :param new_contact: Updated Contact object.
        :type new_contact: Contact
        """
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                if contact.email == email:
                    self.contacts[i] = new_contact
                    self._save_contact()
                    return True
        return False

    def delete_contact(self, name: str, email: str):
        """
        Delete a contact from the contact list.

        :param name: Name of the contact.
        :type name: str
        :param email: Email of the contact.
        :type email: str
        """
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if contact.email == email:
                    self.contacts.remove(contact)
                    self._save_contact()
                    return True
        return False
