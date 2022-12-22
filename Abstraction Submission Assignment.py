

from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ",amount)
# Function tells us to pass in argument, but won't say how or what kind
# of data it'll be
    @abstractmethod
    def payment(self,amount):
        pass

class DebitCardPayment(car):
# Defined how to implement payment function from parent paySlip class
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit ' .format(amount))

obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")
    
