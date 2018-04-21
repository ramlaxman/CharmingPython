"""
All parameters (arguments) in the Python language are passed by reference.
It means if you change what a parameter refers to within a function,
the change also reflects back in the calling function.
"""

# pass by reference

list1 = [1, 2, 3]

print("before the function call")
print(list1)

def changeList(paramList):
    paramList.append(4)
    return

changeList(list1)

print("after the function call")
print(list1)

def replaceList(paramList):
    print("inside the function : ", paramList)
    paramList = [6,5,4]
    print("after the update : ", paramList)
    return

replaceList(list1)
print("list after replacement : ")
print(list1)
