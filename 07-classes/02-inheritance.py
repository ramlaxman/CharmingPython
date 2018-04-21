"""
The transfer of the characteristics of a class to other classes that are derived from it.
"""

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
       Parent.__init__(self)
       print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

print ("############################ \n multiple inheritance : ")
class School:
    def __init__(self):
        self.schoolname = "Elegent school, Pune"

    def printSchool(self):
        print (self.schoolname)

class boy(Parent, School):
    def __init__(self, name):
        Parent.__init__(self)
        School.__init__(self)
        self.name = name

    def getName(self):
        print (self.name)

b1 = boy('rohit')

b1.getName()
b1.printSchool()
b1.parentMethod()
