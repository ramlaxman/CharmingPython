"""
This program imports sys module to make use of command line arguments
"""

import sys

print("the command Line aruments are : ", sys.argv)

print("0th argument is always the program file iteself : ", sys.argv[0])

if len(sys.argv) > 1:
    print("always have valid check for number of arguments : ", sys.argv[1])
if len(sys.argv)>2:
    print("accessing multiple arguments : ")
    for i in range(0, len(sys.argv)):
        print(i, " : ", sys.argv[i])
print ("the command Line aruments are : ", sys.argv)

print ("0th argument is always the program file iteself : ", sys.argv[0])

if len(sys.argv) > 1:
    print ("always have valid check for number of arguments : ", sys.argv[1])
if len(sys.argv)>2:
    print ("accessing multiple arguments : ")
    for i in range(0, len(sys.argv)):
        print (i, " : ", sys.argv[i])

"""
print sys.stderr
print sys.stdin
print sys.stdout
"""
