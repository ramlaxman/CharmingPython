## this program parses the file specified by the below path


filetoOpen = "fileParser.py"

f = open(filetoOpen, 'r')

print("printing fileObject : ")
print(f)
print ("printing fileObject : ")
print (f)

lines = f.readlines()

for eachLine in lines:
    print("line : ", eachLine, "length : ", len(eachLine))
    print ("line : ", eachLine, "length : ", len(eachLine))

f.close()
