# write different methods of printing and print formatting

print "Hello World"

print "Hello"
print "World"

print "First Line \n Second Line at next position"

paramValue = 20

print "printing variables : %d" % paramValue
print "printing variables : %s" % paramValue
print "printing variables : %f" % paramValue
print "printing variables : %.3f" % paramValue

print "concatenation of string and variable : ", paramValue

print "combining string 1 and ", "string 2"

print "double inverted commas", 'single inverted commas'

print "Multi line printing"

print """
This is the way to print strings that are formatted in code
    -- avoids tabs
    -- avoids next lines
"""

complexPrint = ('Put several strings within parentheses '
        'to have them joined together.')

print complexPrint


# using format string as a variable :
formatter = "%d.%d.%d.%d"
print "ip address is : " + formatter % (192, 168, 0, 100)


