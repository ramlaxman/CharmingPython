"""
sample file that shows how to use APIs
"""

import os

dirOfOS = dir(os)

for singleThing in dirOfOS:
    print (singleThing)

print ("OS Name : " + os.name)

print ("creating directory : " + str(os.mkdir("./thisDir")))

returnValue = os.system("ls -l")

print ("printing returnValue : ")
print (returnValue)
