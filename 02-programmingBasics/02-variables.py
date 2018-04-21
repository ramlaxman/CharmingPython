# write a program to show the behaviour of variables in python

"""
Variables are Storage containers. they provide space to store data
"""

var1 = 20

print ("printing variable : ", var1)
print ("the variable has %d value " % var1)

var1 = 10
print ("The value of variable has been reassigned to : ", var1)

var2 = 30
print ("Simple arithmatic with variables : ")
print ("\tAddition : ", (var1 + var2))
print ("\tSubstraction : ", (var1 - var2))
print ("\tMultiplication : ", (var1 * var2))
print ("\tDivision : ", (var1 / var2))

VAR1 = 33
print ("Same names yet different value due to Case sensitive names : %d -- %d " % (var1, VAR1))
