"""
2. Write a Python program to count the number of characters (character frequency) in a string.
e.g. for a string "this" : t=1, h=1, i=1, s=1
"""

sampleString = "this is sample string of chars"

freqDict = {}

for ch in sampleString:
    if ch in freqDict:
        freqDict[ch] = freqDict[ch]+1
    else:
        freqDict[ch]=1

<<<<<<< HEAD
print(freqDict)
=======
print (freqDict)
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd
