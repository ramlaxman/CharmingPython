class badValue(RuntimeError):
   def __init__(self, arg):
<<<<<<< HEAD
      print(arg, "is not accepted")
=======
      print (arg, "is not accepted")
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd

try:
    v = 10
    if v ==10:
        raise badValue(v)

except badValue:
<<<<<<< HEAD
    print("error raised")

finally:
    print("this part of the code executes after everything")
=======
    print ("error raised")

finally:
    print ("this part of the code executes after everything")
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd
