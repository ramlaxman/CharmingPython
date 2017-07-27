print "Enter two numbers : "
num1 = raw_input()
num2 = raw_input()

# simple if else

if (int(num1)%2)==0:
    print "num1 is even"
else:
    print "num1 is odd"

# nested if else conditions

if num1 == num2:
    print "same numbers"
elif num1>num2:
    print "num1 is greater"
else:
    print "num2 is greater"