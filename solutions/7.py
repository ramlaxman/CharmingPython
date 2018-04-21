class student:
    def __init__(self, name, rollno, subjectList):
        self.name = name
        self.rollno = rollno
        self.subjectList = subjectList

    def addSubject(self, subjectName):
        self.subjectList.append(subjectName)

    def removeSubject(self, subjectName):
        if len(self.subjecList)!=0:
            if subjectName in self.subjectList:
                self.subjectList.remove(subjectName)

class division:
    def __init__(self, name):
        self.name = name
        self.studentList = []

    def addStudent(self, student):
        self.studentList.append(student)

div1 = division('bca')
<<<<<<< HEAD
print(vars(div1))
stud1 = student('narendra', 10, ['network, python'])
print(vars(stud1))
div1.addStudent(stud1)
print(vars(div1))
stud2 = student('samadhan', 20, ['network, python', 'database'])
div1.addStudent(stud2)
print(vars(div1))

for student in div1.studentList:
    print(vars(student))
=======
print (vars(div1))
stud1 = student('narendra', 10, ['network, python'])
print (vars(stud1))
div1.addStudent(stud1)
print (vars(div1))
stud2 = student('samadhan', 20, ['network, python', 'database'])
div1.addStudent(stud2)
print (vars(div1))

for student in div1.studentList:
    print (vars(student))
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd
