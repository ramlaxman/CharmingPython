# odd even with if-elif-else condition
print("Enter two numbers: ")
num1 = input()
num2 = input()

# simple if else

if (int( num1 ) % 2)==0:
	print("num1 is even")
else:
    print("num1 is odd")

# nested if else conditions

if num1 == num2:
    print("same numbers")
elif num1 > num2:
    print("num1 is greater")
else:
    print("num2 is greater")
