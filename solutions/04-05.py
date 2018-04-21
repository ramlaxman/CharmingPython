"""
5. Write a program to
    1. encrypt a string with Ceaser Cypher with a key
    2. decrypt the string with same key
"""
inputText = "abcd"
key = 5

print("inputText : ", inputText)

def encrypt(ch, key):
    #get ascii value of character
    x = ord(ch)
    e = 97+(x+key-97)%26
    return chr(e)

def decrypt(ch, key):
    y = ord(ch)
    d = 97+(y+(-key)-97)%26
    return chr(d)


cipher = ""

for c in inputText:
    if c != ' ':
        c = encrypt(c,key)
    cipher = cipher+c

print("cipher : ", cipher)

plain = ""
for c in cipher:
    if c!=' ':
        c = decrypt(c, key)
    plain = plain+c

print("plain : ", plain)
