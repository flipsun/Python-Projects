
class User:
    #Define attributes of the class
    name = "No name provided"
    email = ""
    password = "1234abcd"
    account = 0

    #Define methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")
            
    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account

            
class Employee(User):
     base_pay = 16.00
     department = 'General'

class Customer(User):
    mailing_address = ' '
    mailing_list = True

#Outside of the class you would create an isntance of the User class
new_user = User("Brandon Roman", "roman.bran@gmail.com", "password", 1234)

#Call the login method using the new object
new_user.login()


