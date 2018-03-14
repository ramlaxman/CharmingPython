# declaring a list variable
emptyList = []
print(type(emptyList))
print("empty list", emptyList)

print('\n', '# #'*30)
# populating a list
listOfDays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(type(listOfDays))
print(listOfDays)
print("no of elements in list: ", len(listOfDays))

print('\n', '#'*30)
# accessing elements by indexes
# list index starts with 0
i=4
print("Element at position %d is" %i, listOfDays[i])

print('\n', '#'*30)
# updating the list
animalFarm = ['dog', 'cat', 'cow', 'hen', 'rat']
print("default list : ", animalFarm)

print('\n', '#'*30)
#adding element at the end
animalFarm.append('pig')
print("added element 'pig' : ", animalFarm)

print('\n', '#'*30)
# updating list element
animalFarm[1] = 'horse'
print("updated element at location [1]", animalFarm)

print('\n', '#'*30)
# removing element from the list
animalFarm.remove('rat')
print("removing element 'rat'", animalFarm)

print('\n', '#'*30)
# looping over list elements
for eachDay in listOfDays:
    print("day is : ", eachDay)

for everyAnimal in animalFarm:
    print("animal is : ", everyAnimal)

print('\n', '#'*30)