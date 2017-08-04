

def areaCircle(r, pi=3.1415):
    return pi*(r**2)

print "passing only required argument"
print areaCircle(3)

print "specifying value of all arguments"
print areaCircle(3, 3.14159265)

print "sequence of parameters is not important as long as names are known"
def areaRectangle(length, breadth):
    return length*breadth

print "area of rectangle of 4x3" , areaRectangle(breadth=3, length=4)


# multiple return values :

def addNsub(x, y):
    return (x+y), (x-y)

print addNsub(3,4)