# simple for loop

# range (i,j) prints from i to j-1
# end = "" at the end of given sentence
for i in range(0,10):
    print(i, end=' ')

print("\niterating over list elements")

farm = ["cat", "dog", "cow"]
for animal in farm:
    print(animal, end=' ')

print("\n")

# for(i=0;i<10;i++)
# i = 0 1st line
# check value of i is less than 10
# now increase counter by 1.

for i in range(0,10):    # check value of i i.e.0
    for n in range(0, i):  # compare (0,0)
        print(" n: ",n,end=' ')
    else:
        print(" i: ",i,"\n",end='')
