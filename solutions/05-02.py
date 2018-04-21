"""
2. write set of functions to manage dictionary of students of a class
    -- key should be a tuple of (branch, division and roll_number)
    -- value should be a list of attributes of a student (name, gender, address, DOB, email)
    -- write a functions to create, access, delete, add and update the students data
"""


classOfStuds = []

def displayClass():
    print("printing all students")
    print(classOfStuds)
    print ("printing all students")
    print (classOfStuds)

def addStudent(branch, div, rollNo, name, gender, address, dob, email):
    key = branch, div, rollNo
    stud = {
        'key' : key,
        'name': name,
        'gender':gender,
        'address': address,
        'dob':dob,
        'email': email
    }

    classOfStuds.append(stud)

def deleteStudent(key):
    print("deleting stud : ", key)
    print ("deleting stud : ", key)
    for stud in classOfStuds:
        if stud['key']==key:
            toDelete = stud

    classOfStuds.remove(toDelete)


displayClass()
addStudent('mca','a',4,'narendra', 'm', 'pune', '02061988', 'narendra@mca.com')
displayClass()
addStudent('mca','a',5,'dhanashri', 'f', 'pune', '04051988', 'dhanashri@mca.com')
displayClass()
studToDelete = 'mca','a',4
deleteStudent(studToDelete)
print("after delete")
displayClass()
print ("after delete")
displayClass()
