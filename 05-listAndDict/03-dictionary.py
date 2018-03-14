"""
Rules
    -- More than one entry per key not allowed.
    -- keys should be such that they cannot be changed
"""

# creating a dictionary
dictVar = {"name":"rahul", "age":5}
print(type(dictVar))

# creating a student dictionary
student = {
    'name':'narendra',
    'DOB':'02061988',
    'address':'pune',
    'class':'B'
}

# accessing the value from the key
print("name : ", student['name'])

# accessing entire dictionary
print(student)

# looping over elements
for key, value in student.items():
    print(key, value)

# updating values
student['address'] = 'Mumbai'
print(student)

# adding a field
student['subjects'] = "python"
print(student)

# deleting a field
del student['DOB']
print(student)

# deleting entire dictionary
student.clear()
print(student)
