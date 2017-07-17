"""
machine profile
"""

import os

class machineProfile:

    def __init__(self):
        self.unameVar = os.uname()

        self.osName = self.getOSName()
        self.nodeName = self.getNodeName()
        self.kernelName = self.getKernelRelease()
        self.version = self.getVersionString()
        self.arch = self.getArch()

    def getOSName(self):
        return self.unameVar[0]

    def getNodeName(self):
        return self.unameVar[1]

    def getKernelRelease(self):
        return self.unameVar[2]

    def getVersionString(self):
        return  self.unameVar[3]

    def getArch(self):
        return self.unameVar[4]