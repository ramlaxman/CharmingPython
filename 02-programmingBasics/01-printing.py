# write different methods of printing and print formatting

print ("Hello World")
print ("Hello")
print ("World")

print ("First Line \n Second Line at next position.") #\n for next line and one space looks like paragraph

paramValue = 20

# For details, refer "printf style formatting" [https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting ]
print ("Printing Variables: %d" %paramValue)  # integer
print ("Printing Variables: %s" %paramValue)  # string
print ("Printing Variables: %f" %paramValue)  # float
print ("Printing Variables: %.3f" %paramValue)# float with decimal digits set by user
print ("Printing Variables: %g" % paramValue) # float

print ("\nConcatenation of string and var:", paramValue)

# Any pair of inverted/double inverted commas,which is string, disappears in result.
print ("\ncombining string 1 and", 'string 2')

#If you won't write print before """, python interpreter will treat it as multiline comment.
print ("\nMulti line printing")
print ("""
This is the way to print strings that are formatted in code
    -- avoids tabs
    -- avoids next lines
""")

complexPrint = ('Put several strings within parentheses''to have them joined together.')

print (complexPrint)

# using format string as a variable : 
formatter = ("%d.%d.%d.%d")
print ("\nIP address is:" + formatter %(192, 168, 0, 100))
