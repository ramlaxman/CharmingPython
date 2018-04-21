"""
by default everything in python class is public

Python does not have mandatory access control like some other languages you may be used to.
"""

class person:
    __aadharNumer = '1234567890'

    def __init__(self, name):
        self.name = name

    def printAadhar(self):
        print (self.__aadharNumer)

p1 = person('narendra')

print ("name : ", p1.name)

p1.printAadhar()

# this is a negetive check error is expected :
print ("aadhar : ", p1.__aadharNumer)
