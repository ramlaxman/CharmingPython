# more operations on string

sampleString = "this is my input sample string."

# concatanation
print("attach a string to other : " + sampleString)


# repetition
smallString = "testString"
times = 20
print("printing %s into %d times" % (smallString, times))
print(smallString*times)

# checking content of string
if "this" in sampleString:
    print("this is present")

# negetive check
resultStatement = "I have failed this exam"
if "pass" not in resultStatement:
    print("you are doomed")

# string formatting
formatter = "%d.%d.%d.%d"
print("ip address is : " + formatter % (192, 168, 0, 100))

# formatting with more options
print('{0}, {1}, {2}'.format('a', 'b', 'c'))

print('{}, {}, {}'.format('a', 'b', 'c'))  # 2.7+ only

print('{2}, {1}, {0}'.format('a', 'b', 'c'))

print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))

# For Py 3.6+,
name = 'Ram'
print(f"His name is {name}")   #warn:there must not be any gap bet'n f & "

# text alignment
print('{:<30}'.format('left aligned'))
print('{:>30}'.format('right aligned'))
print('{:^30}'.format('centered'))
print('{:*^30}'.format('centered'))  # use '*' as a fill char
