"""
Break keyword: Terminates the current loop and resumes execution at the next statement, just like the traditional break statement in C.
"""

for letter in 'Python':  # First Example
    if letter == 'h': # if result not found it continues until condition executes
    # When condition is false, it won't enter in if block
        break
    print('Current Letter: ',letter)

print('@'*50)

var = 10  # Second Example
while var > 0:
    print('Current variable value :', var)
    var -= 1
    if var == 5:  #Here condition satisfies hence it has stopped before 5
        break