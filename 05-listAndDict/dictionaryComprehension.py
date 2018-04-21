# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
numbers = {x:x*x for x in range (1, 11)}
print(numbers)

# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
squares = {x:x**2 for x in range(1,11)}
print(squares)

# given the list of keys and values write the shortest possible program to create a dictionary from this
keys = {"name", "age", "rollno"}
values = {"narendra", 25, 42}
student = {i[0]:i[1] for i in list(zip(keys, values))}
print(student)
