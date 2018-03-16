class Parent:        # define parent class
   def myMethod(self):
      print ('Calling parent method')

class Child(Parent): # define child class
   def myMethod(self):
      print ('Calling child method')

# another class which does not write its own method
class Chlid2(Parent):
    pass

c = Child()          # instance of child
c.myMethod()         # child calls overridden method

c2 = Chlid2()
c2.myMethod()
