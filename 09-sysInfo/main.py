"""
objective of this app is to create a profile of a machine

hardware
software
users
network interface info

"""

from osDetails import *
from machineProfile import *

def main():
    print "starting machine profiler"
    myMachine = machineProfile()

    print "printing obtained info"
    print myMachine.arch

main()