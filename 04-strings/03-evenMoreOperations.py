inputString = "This is an input string"

print inputString.count('This')

print '\n'*2

paragraph = "To be, or not to be, that is the question: \
Whether 'tis nobler in the mind to suffer \
The slings and arrows of outrageous fortune, \
Or to take Arms against a Sea of troubles, \
And by opposing end them: to die, to sleep \
No more; and by a sleep, to say we end \
the heart-ache, and the thousand natural shocks \
that Flesh is heir to? 'Tis a consummation \
devoutly to be wished."

print paragraph

print '\n'*2
print "count of 'to' in the given paragraph : ", paragraph.count('to')

print '\n'*2
print "list of words in given paragraph split by space : \n", paragraph.split()

print '\n'*2
print "number of words in the given paragraph : ", len(paragraph.split())

print '\n'*2
stringToLocate = 'not'
print "first occurance of %s in given paragraph : " % stringToLocate, paragraph.find(stringToLocate)

print "all paragraph in UPPERCASE : \n", paragraph.upper()

# read more at https://docs.python.org/2/library/string.html