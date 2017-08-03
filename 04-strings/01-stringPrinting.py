"""
strings in python
    -- single quotes
    -- double quotes

    within single quotes you dont need to escape double quote (but you have to escape single quote) and vice versa.
"""

print "sample string"

print 'sample string'

print len("sample string")

print "include 'single' quote"

print 'include "double" quote'

print 'including \'single\' in single'

print "including \"double\" in double"

print "special\n new line"

print "special\t TAB"

print r"printing raw string c:\name\target"

stringVar = "the duration of the day is 24hrs"

#Strings can be indexed (subscripted), with the first character having index 0.
print "printing index locations : "
print stringVar[0], stringVar[1], stringVar[2]

#Indices may also be negative numbers, to start counting from the right
# Note that since -0 is the same as 0, negative indices start from -1.
print "printing index locations : "
print stringVar[-1], stringVar[-2], stringVar[-3]

# slicing of strings
print stringVar[5:20]

# print chars of string from index 20 onwards
print stringVar[20:]

# print chars of string before index 20
print stringVar[:20]

