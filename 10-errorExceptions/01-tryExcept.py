# handle code breaking scenarios
x = 10
try:
<<<<<<< HEAD
    print(int(x)/0)
    print("this was an example to show ZeroDivisionError")
except ZeroDivisionError:
    print("cannot devide by zero")
=======
    print (int(x)/0)
    print ("this was an example to show ZeroDivisionError")
except ZeroDivisionError:
    print ("cannot devide by zero")
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd
