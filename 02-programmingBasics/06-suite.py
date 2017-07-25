"""
a suite is a set of statements clubbed together

suite is necessary for if, while, class and fun defn
"""

print " Enter two numbers : "
num1 = raw_input()
num2 = raw_input()

if (num1>num2):
    print "first number is greater"
    print "num1 comes later in the number series"
    print "substracting num2 from num 1 will yield positive value"
elif(num1<num2):
    print "num2 is greater"
else:
    print "num1 and num2 are equal"