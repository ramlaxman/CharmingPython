"""
sample file that shows how to use APIs
"""

import os

dirOfOS = dir(os)

for singleThing in dirOfOS:
<<<<<<< HEAD
    print(singleThing)

print("OS Name : " + os.name)

print("creating directory : " + str(os.mkdir("./thisDir")))

returnValue = os.system("ls -l")

print("printing returnValue : ")
print(returnValue)
=======
    print (singleThing)

print ("OS Name : " + os.name)

print ("creating directory : " + str(os.mkdir("./thisDir")))

returnValue = os.system("ls -l")

print ("printing returnValue : ")
print (returnValue)
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd
