# A while loop statement in Python programming language
# repeatedly executes a target statement as long as a given condition is true.

# simple example of a while loop

count = 0

while count <= 9:
    print count
    count = count+1


"""
infinite loop :

var = 1

while var==1:
    print var
"""
print '#'*50
"""
If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating the list.
"""

count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"


# Single statement
"""
flag = 1

while (flag): print 'Given flag is really true!'

print "Good bye!"
"""

print '#'*50
"""
nested while loop
"""
demoList = [0, 0, 2, 2, 4, 4, 6, 6, 8, 8]
count = 0
while count < 9:
    print "count value : ", count
    count = count +1
    while count in demoList:
        print "count exists in list"
        demoList.remove(count)
    else:
        print "count not seen"
