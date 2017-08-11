"""
4. Write a Python function to reverses a string without using a library function
"""

sampleString = "this is my sample String"

for i in range(len(sampleString),0,-1):
    print sampleString[i-1],
