class User:
    """Creating a user class for new app with user personal info"""

    def __init__(self, name, email, driver_license_number):
        self.name = name
        self._email = email
        self._driver_license_number = driver_license_number

    @property
    def email(self):
        return self._email

    @email.setter
    def set_email(self, new_email):
        if type(new_email) == str and "@newapp.com" in new_email:
            self._email = new_email

    @property
    def driver_license_number(self):
        return self._driver_license_number
    
    @driver_license_number.setter
    def set_driver_license_number(self, new_driver_license_number):
        if len(new_driver_license_number) == 8:
            self._driver_license_number = new_driver_license_number
    
    
    def __str__(self):
        return f"{self.name} is a new user and can be contacted at {self._email} and their driver's license number is {self._driver_license_number}"
    
    

user1 = User(name="Maple", email="maple@.com", driver_license_number="1234")
user2 = User(name="Moab", email="moab@.com", driver_license_number="5678")
user3 = User(name="Mickey", email="mickey@.com", driver_license_number="9101")
user4 = User(name="Tottie", email="tottie@.com", driver_license_number="2345")

user1.welcome_message()
print(user2.email)
user2.set_email = "moab@newapp.com"
print(user2.email)
print(user3.driver_license_number)
user3.set_driver_license_number = "88888888"
print(user3.driver_license_number)
print(user4)

