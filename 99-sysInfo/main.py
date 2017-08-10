"""
objective of this app is to create a profile of a machine

hardware
software
users
network interface info

"""

from osDetails import *
from machineProfile import *
from networkInfo import *

def main():
    myMachine = machineProfile()
    print vars(myMachine)

    networkDetails = networkInfo()

    print vars(networkDetails)

main()