"""
The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (lastIn, firstOut). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index
"""

stack = [3, 4, 5]
print "printing stack : ", stack

stack.append(6)
stack.append(7)
print "print stack after append : ", stack
[3, 4, 5, 6, 7]


stack.pop()
print "stack after pop : ", stack

stack.pop()
print "stack after pop : ", stack

stack.pop()
print "stack after pop : ", stack

