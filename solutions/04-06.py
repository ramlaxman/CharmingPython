"""
6. Write a Python program to reverse words in a string (DO NOT REVERSE THE STRING).
"""
sampleString = "this is my sample string"

# define word reversing function
def reverseString(word):
    for i in range(len(word), 0, -1):
<<<<<<< HEAD
        print(word[i-1], end=' ')
=======
        print (word[i-1],)
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd

# split the string into words
words = sampleString.split()

# for each word, reverse the word and print
for w in words:
    reverseString(w)
