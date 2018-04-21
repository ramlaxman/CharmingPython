"""
The transfer of the characteristics of a class to other classes that are derived from it.
"""

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
<<<<<<< HEAD
      print("Calling parent constructor")

   def parentMethod(self):
      print('Calling parent method')
=======
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
<<<<<<< HEAD
      print("Parent attribute :", Parent.parentAttr)
=======
      print ("Parent attribute :", Parent.parentAttr)
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd

class Child(Parent): # define child class
   def __init__(self):
       Parent.__init__(self)
<<<<<<< HEAD
       print("Calling child constructor")

   def childMethod(self):
      print('Calling child method')
=======
       print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

<<<<<<< HEAD
print("############################ \n multiple inheritance : ")
=======
print ("############################ \n multiple inheritance : ")
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd
class School:
    def __init__(self):
        self.schoolname = "Elegent school, Pune"

    def printSchool(self):
<<<<<<< HEAD
        print(self.schoolname)
=======
        print (self.schoolname)
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd

class boy(Parent, School):
    def __init__(self, name):
        Parent.__init__(self)
        School.__init__(self)
        self.name = name

    def getName(self):
<<<<<<< HEAD
        print(self.name)
=======
        print (self.name)
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd

b1 = boy('rohit')

b1.getName()
b1.printSchool()
b1.parentMethod()
