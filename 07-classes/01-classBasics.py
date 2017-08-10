
# class statements must be executed before use
class myFriend:
    """a simple class example"""
    def sayHi(self):
        print "hi from the function sayHi"

# creating an object of a class
# assigns this object to variable f1
f1 = myFriend()

# calling a class method with this object
f1.sayHi()

# some surgery on the class
print "printing documentation : ", myFriend.__doc__

print "everything defined by the class as a dictionary"
for k,v in myFriend.__dict__.iteritems():
    print k,v


print '#'*50
# a class with custom constructor
class student:
    """student example class"""
    def __init__(self):
        self.branch = "MCA"

    def whichBranch(self):
        return self.branch

s1 = student()
print s1.whichBranch()

# method object can be stored
print "call after store"
xx = s1.whichBranch
print xx()

print '#'*50
# create an object with custom parameters
class person:
    """for some vital stats"""
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculateBMI(self):
        return (float(self.weight)/float(self.height**2))

p1 = person(65, 1.72)
print "BMI for p1 is : ", p1.calculateBMI()

p2 = person(50, 1.80)
print "BMI for p2 is : ", p2.calculateBMI()

print '#'*50
# class can have variable shared by all instances
print "example of shared variable"
class cat:
    family = "feline"
    def __init__(self,color):
        self.color = color

kitty = cat('white')
print kitty.family
print kitty.color

anotherKitty = cat('black')
print anotherKitty.family
print anotherKitty.color

print '#'*50
#