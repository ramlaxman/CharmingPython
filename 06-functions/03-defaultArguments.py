
def areaRectangle(length, breadth):
    return length*breadth

def areaCircle(r, pi=3.1415):
    return pi*(r**2)

<<<<<<< HEAD
print("passing only required argument")
print(areaCircle(3))

print("specifying value of all arguments")
print(areaCircle(3, 3.14159265))

print("sequence of parameters is not important as long as names are known")
def areaRectangle(length, breadth):
    return length*breadth

print("area of rectangle of 4x3" , areaRectangle(breadth=3, length=4))
=======
print ("passing only required argument")
print (areaCircle(3))

print ("specifying value of all arguments")
print (areaCircle(3, 3.14159265))

print ("sequence of parameters is not important as long as names are known")


print ("area of rectangle of 4x3" , areaRectangle(breadth=3, length=4))
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd


# multiple return values :

def addNsub(x, y):
    return (x+y), (x-y)

<<<<<<< HEAD
print(addNsub(3,4))
=======
print (addNsub(3,4))
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd
