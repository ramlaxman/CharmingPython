class badValue(RuntimeError):
   def __init__(self, arg):
      print(arg, "is not accepted")

try:
    v = 10
    if v ==10:
        raise badValue(v)

except badValue:
    print("error raised")

finally:
    print("this part of the code executes after everything")