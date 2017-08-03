dt1 = {'name': 'micheal'}
dt2 = {'name': 'micheal'}
dt3 = {'name': 'narendra'}

# compare two dictionaries
print dt1 == dt2
print dt1 == dt3

# lenght of dictionary
student = {
    'name':'narendra',
    'DOB':'02061988',
    'address':'pune',
    'class':'B'
}

print "length : ", len(student)

# does the dict have this key
print "has_key DOB ? ", student.has_key('DOB')
print "has_key subject ? ", student.has_key('subject')

# add one dict into another
newD = {'subject':'programming'}
student.update(newD)

print "updated dictionary : ", student
print "has_key subject ? ", student.has_key('subject')


# creating a dict with tuples as key

classes = ['mca', 'mcs']
divisions = ['a', 'b']
roll_no = [1, 2, 3, 4, 5]

stud1 = classes[0], divisions[0], roll_no[0]
stud2 = classes[0], divisions[0], roll_no[1]

stud3 = classes[0], divisions[1], roll_no[0]
stud4 = classes[0], divisions[1], roll_no[1]

studsOfMCA = {
    stud1 : "Jai",
    stud2 : "Viru",
    stud3 : "Thakur",
    stud4 : "Gabbar"
}

for k,v in studsOfMCA.iteritems():
    print k , " : ", v