# creating a dictionary
dictVar = {"name":"rahul", "age":5}
print type(dictVar)

# creating a student dictionary
student = {
    'name':'narendra',
    'DOB':'02061988',
    'address':'pune',
    'class':'B'
}

# accessing the value from the key
print "name : ", student['name']

# accessing entire dictionaly
print student

# looping over elements
for key, value in student.iteritems():
    print key, value


# updating values
student['address'] = 'Mumbai'
print student

# adding a field
student['subjects'] = "python"
print student