dt1 = {'name': 'micheal'}
dt2 = {'name': 'micheal'}
dt3 = {'name': 'narendra'}

# compare two dictionaries
print(dt1 == dt2)
print(dt1 == dt3)

# length of dictionary
student = {
    'Name':'narendra',
    'DOB':'02061988',
    'Address':'pune',
    'Class':'B'
}

print("Length: ", len(student))

# does the dict have this key
print("has_key DOB ? ", 'DOB' in student)
print("has_key subject ? ", 'subject' in student)

# add one dict into another
sub = {'subject':'Python'}
student.update(sub)

print("updated dictionary:", student)
print("Is there key named as subject?", 'subject' in student)

# creating a dict with tuples as key

classes = ['mca','mcs']
divisions = ['a','b']
roll_no = [1, 2, 3, 4, 5]

stud1 = classes[0],divisions[0],roll_no[0]
stud2 = classes[0],divisions[0],roll_no[1]
stud3 = classes[0],divisions[1],roll_no[0]
stud4 = classes[0],divisions[1],roll_no[1]

studsOfMCA = {
    stud1 : "Jai",
    stud2 : "Viru",
    stud3 : "Thakur",
    stud4 : "Gabbar"
}

for k,v in studsOfMCA.items():
    print(k,":",v)
