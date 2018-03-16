"""
1. create a list of dictionaries of students with basic fields
    -- add a list of 5 marks values as a field to each student
    -- these would be marks of each student in each of five subjects
    -- calculate the average marks obtained by the class in each subject
"""

stud1 = {
    "name" : "narendra",
    "rollno" : '1',
    "marks" : [50, 60, 70, 80, 75]
}

stud2 = {
    "name" : "rahul",
    "rollno" : '2',
    "marks" : [55, 65, 65, 70, 70]
}

stud3 = {
    "name" : "micheal",
    "rollno" : 3,
    "marks" : [60, 70, 90, 88, 77]
}

listOfStuds = [stud1, stud2, stud3]

SubTotal = []

for i in range(0,5):
    SubTotal.append(0)
    for stud in listOfStuds:
        SubTotal[i] = SubTotal[i] + stud["marks"][i]

print (SubTotal)

averageList = [float(x)/len(listOfStuds) for x in SubTotal]

print (averageList)
