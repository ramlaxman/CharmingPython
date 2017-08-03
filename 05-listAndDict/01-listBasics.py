# declaring a list variable
emptyList = []
print type(emptyList)
print "empty list", emptyList

print '\n\n', '#'*50
# populating a list
listOfDays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print type(listOfDays)
print listOfDays
print "no of elements in list : ", len(listOfDays)

print '\n\n', '#'*50
# accessing elements by indexes
# list index starts with 0
i=4
print "element at position %d " % i , listOfDays[i]

print '\n\n', '#'*50
# updating the list
animalFarm = ['dog', 'cat', 'cow', 'hen', 'rat']
print "default list : ", animalFarm

print '\n\n', '#'*50
#adding element at the end
animalFarm.append('pig')
print "added element 'pig' : ", animalFarm

print '\n\n', '#'*50
# updating list element
animalFarm[1] = 'horse'
print "updated element at location [1]", animalFarm

print '\n\n', '#'*50
# removing element from the list
animalFarm.remove('rat')
print "removing element 'rat'", animalFarm

print '\n\n', '#'*50
# looping over list elements
for eachDay in listOfDays:
    print "day is : ", eachDay

for everyAnimal in animalFarm:
    print "animal is : ", everyAnimal

print '\n\n', '#'*50