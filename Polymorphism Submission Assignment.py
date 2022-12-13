

#Parent Clas User
class User:
    name = "Broman"
    email = "broman@gmail.com"
    password = "1234abcd"
    
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        
        

#Child Class Employee            
class Employee(User):
    base_pay = 16.00
    department = 'General'
    pin_number = '8130'

# Same method in the parent class "User"
# Difference = Instead of using entry_password, we're using entry_pin.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect. Please enter your info to create a new account")

#Child Class Customer           
class newCustomer(User):
    name = "Barry"
    email = "b.allen@gmail.com"

    def getNewLoginInfo():
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        if (entry_name == new.name and entry_email == new.email):
            print("Thank you for creating your account, {}!".format(entry_name))
        else:
            print("You did not enter the correct information!")
            
    def __init__(name,email):
        User.name = name
        User.email = email

# Following code invokes methods inside each class for User and Employee

customer = User("Broman", "broman@gmail.com", "1234abcd", 1234)
customer.getLoginInfo()

manager = Employee("Roman", "roman.bran@gmail.com", "password", 1234)
manager.getLoginInfo()

newCustomer = User("Barry", "b.allen@gmail.com", "password1", 2345)
newCustomer.getLoginInfo()
