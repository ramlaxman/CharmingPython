"""
3. Write a Python program to count the occurrences of each word in a given sentence
"""

paragraph = "To be, or not to be, that is the question: \
        Whether 'tis nobler in the mind to suffer \
        The slings and arrows of outrageous fortune, \
        Or to take Arms against a Sea of troubles, \
        And by opposing end them: to die, to sleep \
        No more; and by a sleep, to say we end \
        the heart-ache, and the thousand natural shocks \
        that Flesh is heir to? 'Tis a consummation \
        devoutly to be wished."

listOfwords = paragraph.split()

freqDict = {}

for w in listOfwords:
    if w in freqDict:
        freqDict[w] = freqDict[w]+1
    else:
        freqDict[w]=1

for k,v in freqDict.items():
    print (k,v)

