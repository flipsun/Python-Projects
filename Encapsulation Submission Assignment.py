
# Protected / Non-Public Method: Outputs "34"
class Protected:
    def __init__(self):
        self.protectedVar = 0

obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar)

# Private Method: Outputs "12" and "23"

class Private:
    def __init__(self):
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Private()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()

