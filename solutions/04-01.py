"""
1. Write a Python program to calculate the length of a string without using library function
"""

sampleString = "this is my sample string"

count = 0

for ch in sampleString:
    count = count+1

print ("length : ", count)
