"""
1. write a program to emulate calculator functionality
    -- define functions for various arithmatic and logical operation
    -- prompt user for operation as long as user does not want to exit
    -- accept proper imput from user for a particular operation
    e.g. addition takes two numbers, square takes only one
    -- additionally, format the output to look good
"""

def addition():
    n1 = int(input('operand1 : '))
    n2 = int(input('operand2 : '))
    print((n1+n2))
    print (n1+n2)


def substraction():
    n1 = int(input('operand1 : '))
    n2 = int(input('operand2 : '))
    print((n1-n2))
    print (n1-n2)


def multiplication():
    n1 = int(input('operand1 : '))
    n2 = int(input('operand2 : '))
    print((n1*n2))
    print (n1*n2)


def division():
    n1 = int(input('operand1 : '))
    n2 = int(input('operand2 : '))
    print((float(n1)/float(n2)))
    print (float(n1)/float(n2))


def main():
    ch = 0
    while(ch != 99):

        print("""

        print ("""

        select operation :
            1. addition
            2. substraction
            3. multiplication
            4. division
            99. quit
        """)
        ch = int(input())

        if ch == 1:

            print("addition")
            addition()
        elif ch==2:
            print("substraction")
            substraction()
        elif ch==3:
            print("multiplication")
            multiplication()
        elif ch==4:
            print("division")
            division()
        elif ch==99:
            print("quitting the calculator")
            quit()
        else:
            print("wrong choice of option")

            print ("addition")
            addition()
        elif ch==2:
            print ("substraction")
            substraction()
        elif ch==3:
            print ("multiplication")
            multiplication()
        elif ch==4:
            print ("division")
            division()
        elif ch==99:
            print ("quitting the calculator")
            quit()
        else:
            print ("wrong choice of option")
        """)

main()
