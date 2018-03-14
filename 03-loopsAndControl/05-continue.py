"""
As name indicates break keyword stops giving result as soon as condition comes 
true. On contrary, continue keyword continues to give result, even if condition 
comes true, until entire argument is over.
"""

for letter in 'Python':     # First Example
   if letter == 'h':        
      continue
   print('Current Letter :', letter)

print('#'*50)

var = 10                    # Second Example
while var > 0:
   var -= 1
   # replace while with if will take into @@ infinity
   if var == 5:
       print("not printing")
       continue
   print('Current variable value :', var)