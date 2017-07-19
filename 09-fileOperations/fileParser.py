## this program parses the file specified by the below path


filetoOpen = "./inputFile"

f = open(filetoOpen, 'r')

print "printing fileObject : "
print f

lines = f.readlines()

for eachLine in lines:
    print "line : ", eachLine, "length : ", len(eachLine)
