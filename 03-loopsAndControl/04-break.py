"""
It terminates the current loop and resumes execution at the next statement, just like the traditional break statement in C.
"""

for letter in 'Python':  # First Example
    if letter == 'h':
        break
    print 'Current Letter :', letter

print '#'*50
print '#'*50

var = 10  # Second Example
while var > 0:
    print 'Current variable value :', var
    var = var - 1
    if var == 5:
        break