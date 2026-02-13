import re

class Contact:
    """
    Represents a single contact entry
    """

    def __init__(self,name:str,phone:str,email:str):
        self.name = self._validate_name(name)
        self.phone = self._validate_phone(phone)
        self.email =self._validate_email(email)

    def _validate_name(self,name:str)->str:
        if not name.strip():
            raise ValueError("enter the name")
        return name.strip().title()
    
    def _validate_phone(self,phone:str)->str:
        print(phone)
        if not phone.isdigit():
            raise ValueError("phone must contain digits only")
        return phone
        
    def _validate_email(self,email:str)->str:
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern,email):
            raise ValueError("Invalid email format")
        return email
    
    def to_dict(self)->dict:
        """
        convert contact details to dictionary.
        :return: contact details
        :rtype: dict
        """
        return {
            "name":self.name,
            "phone":self.phone,
            "email":self.email
        }
    

    @staticmethod
    def from_dict(data:dict):
        """
        create contact object from dictionary
        
        """
        return Contact(data['name'],data['phone'],data['email'])
    
    def __str__(self):
        return f"{self.name} , {self.phone} , {self.email}"
    
    
    


        