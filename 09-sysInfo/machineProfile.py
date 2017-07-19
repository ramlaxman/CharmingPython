"""
machine profile
"""

import platform

class machineProfile:

    def __init__(self):
        self.osName = self.getOSName()
        self.nodeName = self.getNodeName()
        self.kernelRelease = self.getKernelRelease()
        self.version = self.getVersionString()
        self.arch = self.getArch()

    def getOSName(self):
        return platform.system()

    def getNodeName(self):
        return platform.node()

    def getKernelRelease(self):
        return platform.release()

    def getVersionString(self):
        return  platform.version()

    def getArch(self):
        return platform.machine()
