class user:
    """
    Base class representig user
    """
    def __init__(self,user_id:int,name:str,email:str):
        self.user_id = user_id
        self.name = name
        self.email = email
    
    def get_details(self) ->dict:
        return{
            "id":self.user_id,
            "name":self.name,
            "email":self.email,
        }
    
    
    def __str__(self):
        return f"{self.user_id} - ({self.name}) - {self.email}"   


class CompanyUser(user):
    """
    Inherits from user and add company details
    """
    def __init__(self, user_id:int, name:str, email:str,company_name:str,):
        super().__init__(user_id, name, email)
        self.company_name = company_name

    def get_details(self)->dict:
        data = super().get_details()
        data["company"] = self.company_name
        
        return data 
    

    def __str__(self):
            return (
                f"{self.name} works at {self.company_name} "
            )   

