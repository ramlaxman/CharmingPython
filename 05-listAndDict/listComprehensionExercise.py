# create a list of cubes of all numbers upto 10
cubes = [x**3 for x in range(0,11)]
print(cubes)


# return a list of only uppercase letters in a given string
inputString = "This is Sample Statement For List CompreHension"
caps = [x for x in inputString if x.isupper()]
print(caps)


# create a list of integers which specify the length of each word in a certain sentence, but only if the word is not the word "the".
para = "This is not the sample string that needs the testing"
word_len = [len(word) for word in para.split() if word.lower()!="the"]
print(word_len)


# create a new list called "newlist" out of the list "numbers", which contains only the positive integer numbers from the list.
numbers = [23, 33.44, -33, 87.900, 55, 91]
positive_ints = [i for i in numbers if i>0 and type(i)==type(1)]
print(positive_ints)

# create a list of ip addresses in the range 192.168.1.100 to 192.168.1.110
ip_addrs = ["192.168.1.%d" % i for i in range(100, 111)]
print(ip_addrs)
