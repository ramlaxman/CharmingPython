## this program parses the file specified by the below path


filetoOpen = "fileParser.py"

f = open(filetoOpen, 'r')

<<<<<<< HEAD
print("printing fileObject : ")
print(f)
=======
print ("printing fileObject : ")
print (f)
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd

lines = f.readlines()

for eachLine in lines:
<<<<<<< HEAD
    print("line : ", eachLine, "length : ", len(eachLine))
=======
    print ("line : ", eachLine, "length : ", len(eachLine))
>>>>>>> c3ac379fca6dc807a4f148dfcfcc453a176335dd

f.close()

