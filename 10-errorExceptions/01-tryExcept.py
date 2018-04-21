# handle code breaking scenarios
x = 10
try:
    print(int(x)/0)
    print("this was an example to show ZeroDivisionError")
except ZeroDivisionError:
    print("cannot devide by zero")
