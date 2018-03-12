# write different methods of printing and print formatting

print ("Hello World")

print ("Hello")
print ("World")

print ("First Line \n Second Line at next position.")  #\n for next line and one space looks like paragraph

paramValue = 20

# For details, refer ```printf```style formatting [https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting ]
print ("printing variables : %d" %paramValue)       # integer
print ("printing variables : %s" %paramValue)       # 
print ("printing variables : %f" % paramValue)      # float
print ("printing variables : %.3f" % paramValue)    # float with decimal values set by user
print ("printing variables : %g" % paramValue)      # 

print ("concatenation of string and variable: ", paramValue)

# Any pair of inverted commas -- which is string disappears after compilation.
print ("combining string 1 and", 'string 2')

#  #If you are not going to write ```print``` before """, python interpreter will treat it as multiline comment.
print ("Multi line printing")
print ("""
This is the way to print strings that are formatted in code
    -- avoids tabs
    -- avoids next lines
""")

complexPrint = ('Put several strings within parentheses'
                'to have them joined together.')

print (complexPrint)

# using format string as a variable : 
formatter = ("%d.%d.%d.%d")
print ("ip address is : " + formatter % (192, 168, 0, 100))
