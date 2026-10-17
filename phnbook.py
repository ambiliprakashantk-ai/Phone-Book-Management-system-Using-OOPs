
class PhoneBook():
    def __init__(self):
        self.contacts={}

    def add_contact(self,name,phone_number):
        # Add a new contact if the name does not already exist
        if name in self.contacts:
            print(f"{name} already exists")
        else:
            self.contacts[name]=phone_number
            print(f"{name} is added succuesfully")

    def update_condacts(self,name,new_phone_number):
        if name in self.contacts:
            self.contacts[name]=new_phone_number
            print(f"{name} number is upated")
        else:
            print(f"{name} is not found")

    def delete_contacts(self,name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} deleted succesfully")
        else:
            print(f"{name} is not found")

    def display_contacts(self):
        if not self.contacts:
            print("The phone book is empty")
        else:
            print("\n---Phone Book Contacts---")
            for name,phone in self.contacts.items():
                print(f"Name :{name} | Phone :{phone}")

p1=PhoneBook()
p1.add_contact("ambly",8767854362)
p1.add_contact("sona",8767854362)
p1.update_condacts("ambly",65432123464)
p1.update_condacts("ameesha",654323776)
p1.delete_contacts("ambly")
p1.display_contacts()
