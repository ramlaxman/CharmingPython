"""
some more exercise with modules
"""

import os

# The built-in dir() and help() functions are useful as interactive aids for working with large modules like os:
print(dir(os))

# helpVar = help(os)

print(os.getcwd())

os.chdir("/usr/bin")

print(os.getcwd())
print (dir(os))

# helpVar = help(os)

print (os.getcwd())

os.chdir("/usr/bin")

print (os.getcwd())
