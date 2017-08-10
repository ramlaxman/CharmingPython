"""
collect all info about network
"""

import socket


class networkInfo:

    def __init__(self):
        self.loopBackAddr = self.getLoopbackAddress()


    def getLoopbackAddress(self):
        return socket.INADDR_LOOPBACK