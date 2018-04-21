class Parent:        # define parent class
   def myMethod(self):
<<<<<<< HEAD
      print('Calling parent method')

class Child(Parent): # define child class
   def myMethod(self):
      print('Calling child method')
=======
      print ('Calling parent method')

class Child(Parent): # define child class
   def myMethod(self):
      print ('Calling child method')
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd

# another class which does not write its own method
class Chlid2(Parent):
    pass

c = Child()          # instance of child
c.myMethod()         # child calls overridden method

c2 = Chlid2()
c2.myMethod()
